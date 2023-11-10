import customtkinter as ctk
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
from datetime import date
from CTkMessagebox import CTkMessagebox

root= ctk.CTk()
root.title("Invoice Generator")
ctk.set_appearance_mode("light")
root.resizable(0, 0)

def show_info():
    # Default messagebox for showing some information
    CTkMessagebox(title="Info", message="Invoice Created Successfully")

invoice_list = []
def add_item():
    qty= int(qtye.get())
    desc= desce.get()
    price= float(pricee.get())
    total = round(qty * price, 2)
    invoice_items=[qty, desc, price, total]
    view.insert("", 0, values=invoice_items)
    clear_entry()
    invoice_list.append(invoice_items)
def submit():
    show_info()
    doc = DocxTemplate("invoice_template.docx")
    name = fnamee.get() + " " + lnamee.get()
    phone = phonee.get()
    company_name = companye.get()
    company_address = adresse.get()
    subtotal = sum(item[3] for item in invoice_list)
    salestax = round(subtotal * 0.06, 2)
    total = round(subtotal + salestax, 2)


    doc.render({"name" : name,
                "phone":phone,
                "company_name" : company_name,
                "company_address" : company_address,
                "invoice_list" : invoice_list,
                "subtotal" : "$" + str(subtotal),
                "salestax": "$" + str(salestax),
                "total" : "$" + str(total)})
    today = date.today()
    doc_name ="invoice" + name + today.strftime("%b-%d-%Y") + ".docx"
    doc.save(doc_name)
    

def clear():
    for i in view.get_children():
        view.delete(i)

def clear_entry():
    qtye.delete(0, ctk.END)
    pricee.delete(0, ctk.END)
    desce.delete(0, ctk.END)

def new_invoice():
    fnamee.delete(0, ctk.END)
    lnamee.delete(0, ctk.END)
    companye.delete(0, ctk.END)
    phonee.delete(0, ctk.END)
    adresse.delete(0, ctk.END)
    clear_entry()
    clear()
    invoice_list.clear()  


frame = ctk.CTkFrame(root)
frame.grid(row=0 , column=0, padx = 20, pady = 10)

fnamel = ctk.CTkLabel(frame, text="First Name :")
fnamel.grid(row=0, column = 0, sticky ="w",padx=5)
fnamee = ctk.CTkEntry(frame)
fnamee.grid(row=1, column = 0, padx=5, sticky ="w")

lnamel = ctk.CTkLabel(frame, text="Last Name :")
lnamel.grid(row=0, column = 1, sticky ="w", padx=5)
lnamee = ctk.CTkEntry(frame)
lnamee.grid(row=1, column = 1, padx=5,sticky ="w")

companyl = ctk.CTkLabel(frame, text="Company Name :")
companyl.grid(row=0, column = 2, sticky ="w", padx=5)
companye = ctk.CTkEntry(frame)
companye.grid(row=1, column = 2, padx=5, sticky ="w")

phonel = ctk.CTkLabel(frame, text="Phone Number :")
phonel.grid(row=0, column = 3, sticky ="w", padx=5)
phonee = ctk.CTkEntry(frame)
phonee.grid(row=1, column = 3, padx=5, sticky ="w")

adressl = ctk.CTkLabel(frame, text="Company Address :")
adressl.grid(row=2, column = 0, pady = 10, sticky ="w", padx=5)
adresse = ctk.CTkEntry(frame, width=250)
adresse.grid(row=3, column = 0, padx=5, columnspan= 2, sticky ="w")

qtyl = ctk.CTkLabel(frame, text= "Quantity :")
qtyl.grid(row=4, column=0, sticky ="w", padx=5)
qtye = ctk.CTkEntry(frame)
qtye.grid(row=5, column = 0, padx=5, sticky ="w")

descl = ctk.CTkLabel(frame, text="Product Description :")
descl.grid(row=4, column = 1, pady = 10, sticky ="w", padx=5)
desce = ctk.CTkEntry(frame)
desce.grid(row=5, column = 1, padx=5, sticky ="w")

pricel = ctk.CTkLabel(frame, text= "Price :")
pricel.grid(row=4, column=2, sticky ="w", padx=5)
pricee = ctk.CTkEntry(frame)
pricee.grid(row=5, column =2, padx=5, sticky ="w")

addb = ctk.CTkButton(frame, text="Add Item", command= add_item)
addb.grid(row=5, column= 3, padx=5)

columns = ("Qty", "Desc", "Price", "Total")
view = ttk.Treeview(frame, columns=columns, show="headings")
view.grid(row=7 , column= 0, columnspan=4, padx=5, pady=20)
view.heading("Qty", text="Quantity")
view.heading("Desc", text="Descrption")
view.heading("Price", text="Price")
view.heading("Total", text="Total")

submit_invoice=ctk.CTkButton(frame, text="Submit Order", command=submit)
submit_invoice.grid(row=8,column=3, sticky="news", padx=10)

newinvoice=ctk.CTkButton(frame, text="New Order", command=new_invoice)
newinvoice.grid(row=8,column=2, sticky="news", padx= 10)

clear_invoice=ctk.CTkButton(frame, text="Clear Order", command=clear)
clear_invoice.grid(row=8,column=1, sticky="news", padx =10)


root.mainloop()