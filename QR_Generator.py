import qrcode

print("=== QR Code Generator ===")

data = input("Enter text or URL: ")

img = qrcode.make(data)

filename = input("Enter file name: ")
img.save(filename + ".png")

print("QR Code generated successfully!")