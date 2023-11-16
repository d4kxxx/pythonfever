import segno
import customtkinter as ctk
from PIL import Image



root = ctk.CTk()
root.title("QR Generator")
root.geometry("230x360")
root.resizable(0, 0)
ctk.set_appearance_mode("system")


frame=ctk.CTkFrame(root)
frame.grid(padx = 10, pady= 10, row=0, column=0)

frame1=ctk.CTkFrame(root)
frame1.grid(padx = 10, pady= 10, row=1, column=0)

image_label = None  # Initialize image label

def qr():
    global image_label
    qrcode = segno.make_qr(entry.get())
    qrcode.save("basic_qrcode.png", scale=100, border=1)
    my_image = ctk.CTkImage(light_image=Image.open("basic_qrcode.png"), size=(200, 200))
    if image_label:
        image_label.destroy()
    
    # Create a new image label and pack it
    image_label = ctk.CTkLabel(frame, image=my_image, text="")
    image_label.pack(padx=10, pady=10)
    entry.delete(0, ctk.END)
    
entry = ctk.CTkEntry(frame1, placeholder_text="Type Here")
entry.pack(padx=10, pady=10)

generate_btn= ctk.CTkButton(frame1, text = "Generate Qr Code",command = qr)
generate_btn.pack(padx=10, pady=10)



root.mainloop()