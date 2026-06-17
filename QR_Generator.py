import qrcode

print("=== QR Code Generator ===")

data = input("Enter text or URL: ").strip()

if not data:
    print("Error: Input cannot be empty.")
    exit()

filename = input("Enter file name: ")

# Create QR code (important: use QRCode object for logo support)
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Save + show
img.save(filename + ".png")
img.show()

print("QR Code generated successfully!")