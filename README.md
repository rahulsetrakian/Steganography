# Image-Based Steganography (Encryption & Decryption)

## Overview
This project is a **capstone project** for the **IBM Edunet Foundation Internship**. It implements image-based steganography using Python, allowing users to securely embed and extract secret messages within images using password-based encryption.

## Features
- **Image-Based Steganography**: Hides messages within image pixels without altering its visual integrity.
- **Password-Protected Encryption**: Uses **SHA-256 hashing** to secure access to hidden messages.
- **Dynamic Pixel Manipulation**: The message is distributed across different pixels and color channels (RGB) to enhance security.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux using Python and OpenCV.
- **Non-Destructive Encryption**: The modified image remains visually identical to the original.
- **Efficient Data Storage**: Embeds text in an image without increasing its file size significantly.

## Technologies Used
- **Python** – Core programming language for the project.
- **OpenCV (`cv2`)** – Image processing for reading and modifying images.
- **Hashlib** – SHA-256 password hashing for secure encryption.
- **OS Module** – Handles file management and execution.
- **ASCII Encoding** – Converts text characters into numeric values for pixel manipulation.

## Installation
1. Clone the repository or download the scripts.
```sh
 git clone https://github.com/rahulsetrakian/Steganography.git
```
2. Install the required dependencies:
```sh
 pip install opencv-python
```

## Usage
### **Encryption**
1. Run the `encryption.py` script.
2. Enter the path of the image to hide the message in.
3. Input the secret message and a password.
4. The modified image (`encryptedImage.jpg`) will be saved in the same directory.

```sh
python encryption.py
```

### **Decryption**
1. Run the `decryption.py` script.
2. Enter the password used during encryption.
3. The hidden message will be displayed on the terminal.

```sh
python decryption.py
```

## End Users
- **Cybersecurity Enthusiasts**: Learning and experimenting with steganography.
- **Journalists & Whistleblowers**: Securely share confidential data.
- **Government & Intelligence Agencies**: Covert communication techniques.
- **Researchers & Academics**: Study encryption, cybersecurity, and digital security.
- **Privacy-Conscious Users**: Hide personal messages or sensitive information.
- **Developers & Ethical Hackers**: Explore steganography and ethical hacking practices.

## Future Enhancements
- Implementing **AES encryption** for added security.
- Support for **multiple image formats** (PNG, BMP, etc.).
- Introducing **metadata protection** to avoid detection.
- **Graphical User Interface (GUI)** for a more user-friendly experience.

## License
This project is licensed under a **proprietary license** and is not for commercial use.

## Contributors
Developed as part of the **IBM Edunet Foundation Internship**.

---
Made with ❤️ by **Rahul Joriya**
