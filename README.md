# QR Code Generator

A lightweight and user-friendly Python application that instantly converts text, URLs, contact information, or any other input into a QR code image. This project demonstrates the use of external Python libraries, user input handling, and image generation in a simple yet practical way.

---

## Features

✨ Generate QR codes from any text or URL  
💾 Save generated QR codes as PNG images  
⚡ Fast and easy terminal-based interface  
🎯 Beginner-friendly and easy to understand  
📚 Great project for learning Python libraries and file handling

---

## How It Works

1. The user enters text, a URL, or any information.
2. The program converts the input into a QR code.
3. The user provides a filename.
4. The QR code is saved as a PNG image in the current directory.

---

## Requirements

- Python 3.x
- qrcode library
- Pillow (PIL)

---

## Installation

Install the required package using:

```bash
pip install qrcode[pil]
```

---

## Source Code

```python
import qrcode

print("=== QR Code Generator ===")

data = input("Enter text or URL: ")

img = qrcode.make(data)

filename = input("Enter file name: ")
img.save(filename + ".png")

print("QR Code generated successfully!")
```

---

## Usage

Run the program:

```bash
python qr_generator.py
```

Example:

```text
=== QR Code Generator ===

Enter text or URL: https://www.instagram.com
Enter file name: IG

QR Code generated successfully!
```

Generated file:

```text
IG.png
```

---

## Applications

- Website sharing
- Contact information sharing
- Event invitations
- Product labeling
- Digital payments
- Educational projects

---

## Learning Outcomes

Through this project, you will learn:

- Python user input handling
- Working with third-party libraries
- Image generation and saving files
- Basic project structure and documentation

---

## Future Improvements

- Custom QR code colors
- QR code size selection
- Logo embedding
- Graphical User Interface (GUI)
- Batch QR code generation
- QR code scanning functionality

---

## Project Information

**Project Title:** QR Code Generator

**Language:** Python

**Library Used:** qrcode, Pillow


Developed as a beginner-friendly Python project to demonstrate QR code generation and image handling using Python.
