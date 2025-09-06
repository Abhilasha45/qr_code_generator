import qrcode

# Data for QR code
data = "https://www.example.com"  # Change this to your link or text

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_qr_code.png")

print("QR code generated successfully!")
