﻿# file-integrity-checker

*COMPANY NAME*:CODETECH IT SOLUTIONS

*NAME*:PUNITH Y S

*INTERN ID*:CT06DA127

*DOMAIN NAME*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*:6 WEEKS

*MENTOR*:NEELA SANTHOSH

# File Encryption Tool: Secure Your Data with Advanced Encryption

## Project Overview

The File Encryption Tool is a robust, user-friendly desktop application designed to provide secure file encryption and decryption capabilities using industry-standard cryptographic algorithms. This tool empowers users to protect sensitive information by encrypting files with a password, making them unreadable to unauthorized parties. The application features a modern graphical user interface that makes the encryption process accessible to users of all technical backgrounds.

## Key Features

### Strong Encryption Standards
- Implements AES-256 encryption, the same standard used by governments and security professionals worldwide
- Utilizes secure key derivation (PBKDF2) with 100,000 iterations to transform user passwords into cryptographic keys
- Incorporates random initialization vectors (IV) and salt values to enhance security against brute force attacks
- Employs PKCS7 padding to handle data of varying lengths

### Intuitive User Interface
- Clean, modern graphical interface built with Tkinter
- Simple workflow for selecting input files and specifying output locations
- Real-time progress tracking during encryption and decryption operations
- File preview functionality to examine content before and after processing
- Password visibility toggle for easier password entry
- Comprehensive error handling with user-friendly messages

### Versatile File Handling
- Support for encrypting and decrypting any file type (text, images, documents, etc.)
- Automatic suggestion of output filenames based on the operation
- Smart detection of encrypted files to suggest appropriate actions
- Preview capability for text files to verify content

### Multithreaded Processing
- Background processing of encryption and decryption operations
- Responsive UI that remains interactive during file operations
- Progress monitoring with visual feedback
- Operation cancellation support

## Technical Implementation

The project is structured into three main components:

1. **Main Application (app.py)**
   - Implements the graphical user interface using Tkinter
   - Manages the workflow for file selection and processing
   - Handles user interactions and provides feedback
   - Orchestrates the encryption and decryption operations

2. **Encryption Utilities (encryption_utils.py)**
   - Provides core cryptographic functionality
   - Implements secure key derivation from passwords
   - Handles the encryption and decryption of data using AES-256
   - Manages file I/O operations for encrypted content
   - Includes utilities for file content preview and type detection

3. **Testing Module (test_encryption.py)**
   - Validates the encryption and decryption functionality
   - Tests both in-memory data operations and file-based operations
   - Verifies that decrypted content matches the original data
   - Provides diagnostic information about the encryption process

## Security Considerations

The File Encryption Tool implements several security best practices:

- **No Password Storage**: Passwords are never stored; they are only used temporarily in memory during encryption/decryption
- **Key Derivation**: Uses PBKDF2 with SHA-256 and high iteration count to derive encryption keys from passwords
- **Unique Salt Values**: Generates random salt for each encryption operation to prevent rainbow table attacks
- **Initialization Vectors**: Employs random IVs to ensure identical files encrypt to different ciphertexts
- **Error Handling**: Implements secure error messages that don't leak sensitive information
- **Memory Management**: Processes files in chunks to handle large files efficiently

## Use Cases

This tool is ideal for:

- Protecting sensitive personal documents (financial records, identification documents)
- Securing confidential business information
- Encrypting backup files before cloud storage
- Protecting intellectual property and research data
- Ensuring privacy when sharing files through potentially insecure channels
- Safeguarding medical and health records
- Securing academic and educational materials

## Future Enhancements

The project has potential for several enhancements:

- Implementation of asymmetric encryption for public/private key functionality
- Addition of file shredding capabilities for secure deletion
- Integration with cloud storage services
- Support for encrypting entire directories
- Implementation of digital signatures for file authenticity verification
- Creation of a portable version that requires no installation
- Development of mobile companion applications

## Technical Requirements

- Python 3.6 or higher
- Dependencies: cryptography, tkinter (included in standard Python distribution)
- Works on Windows, macOS, and Linux platforms

## Conclusion

The File Encryption Tool represents a powerful yet accessible solution for data protection needs. By combining strong cryptographic algorithms with a user-friendly interface, it makes advanced encryption technology available to everyone. Whether for personal privacy or business security, this tool provides a reliable method to keep sensitive information secure in an increasingly digital world.

OUTPUT:

![Image](https://github.com/user-attachments/assets/75e35051-d7f6-439d-8c0f-9ec04d6106de)

![Image](https://github.com/user-attachments/assets/fefb29f4-e533-4e8c-b50d-0b5df20dc994)

![Image](https://github.com/user-attachments/assets/2c9714fd-0cc4-4f1f-a6b2-606b304eff84)

![Image](https://github.com/user-attachments/assets/d72647c9-3e0f-453d-9f24-17425a157064)

![Image](https://github.com/user-attachments/assets/b7aec82d-5c8f-4b17-acca-c00bce239dfd)
