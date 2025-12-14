import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import qrcode
from PIL import ImageTk

window = tk.Tk()
window.title("Make Your QR")
window.minsize(400, 400)

link_label = ttk.Label(window, text="Enter Your Link Here", font=("Arial", 20, "roman"))

input_link = ttk.Entry()


link_label.pack(padx=8, pady=8)
input_link.pack(padx=8, pady=8)
input_link.config(width=50)

image = ttk.Label(image="")

save_button = ttk.Button(text="Save Image")


image.pack()
img = ""
photo = ""

def save_as_qr():
    global img

    if img is None:
        messagebox.showwarning("Warning", "Creat QR Firstly")
        return

    file_path = filedialog.asksaveasfilename(
        title="Save Your QR",
        initialfile="qr_code.png",
        defaultextension=".png",
        filetypes=[
            ("PNG File", "*.png"),
            ("JPEG File", "*.jpg"),
            ("BMP File", "*.bmp")
        ]
    )

    if not file_path:
        return

    try:
        img.save(file_path)
        messagebox.showinfo(title="Saved", message="File Saved")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def make_qr():
    try:
        input_link.update()
        data = input_link.get().strip()
        global img, photo
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        photo = ImageTk.PhotoImage(img)
        image.config(image=photo)

        save_button.config(state=tk.NORMAL, command=save_as_qr)
        
    except Exception as error:
        return messagebox.showerror(title="Error", message= error)



making_qr_button = ttk.Button(window, text="Make Your QR", command=make_qr)
making_qr_button.pack(padx=8, pady=8)

save_button.pack(padx=8, pady=8)
save_button.config(state=tk.DISABLED)

window.mainloop()