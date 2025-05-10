import hashlib
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile

def calculate_hash(file):
    hasher = hashlib.sha256()
    for chunk in file.chunks():
        hasher.update(chunk)
    return hasher.hexdigest()

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_hash = calculate_hash(uploaded_file)

            # Check for hash match in DB
            existing = UploadedFile.objects.filter(hash=file_hash).first()

            form.instance.hash = file_hash
            form.save()

            return render(request, 'result.html', {
                'hash': file_hash,
                'match': existing is not None,
            })
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})
