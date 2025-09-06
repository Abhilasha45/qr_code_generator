import qrcode

# simple qr code generator

# taking input from user
text = input("Enter text or link for QR: ")

# making qr object
qr = qrcode.QRCode(
    version=1,
    box_size=8,
    border=4   # kept small border
)

qr.add_data(text)
qr.make(fit=True)

# creating image
img = qr.make_image(fill_color="black", back_color="white")

# saving with fixed name
img.save("qr.png")

# open image to see
img.show()

print("QR generated and saved as qr.png")
