import qrcode
from tkinter import Tk, Label, Entry, Button, messagebox

# just a simple qr generator function
def make_qr():
    data = entry.get()
    if data.strip() == "":
        messagebox.showerror("Error", "Please write something!")
        return

    qr = qrcode.QRCode(
        version=1,
        box_size=8,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("myqr.png")

    messagebox.showinfo("Done", "QR saved as myqr.png")
    print("QR created for:", data)  # just to check in terminal

# GUI part
root = Tk()
root.title("My First QR Generator")
root.geometry("400x200")

Label(root, text="Type text or link here:").pack(pady=10)
entry = Entry(root, width=40)
entry.pack(pady=5)

Button(root, text="Generate QR", command=make_qr).pack(pady=20)

root.mainloop()
