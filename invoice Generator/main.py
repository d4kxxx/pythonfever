import customtkinter as ctk
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
from datetime import date
from CTkMessagebox import CTkMessagebox
import subprocess
import sqlite3
import tkinter as tk

root= tk.Tk()
root.title("Invoice Generator")
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
root.resizable(0, 0)
root.configure(background='white')
def show_info():
    # Default messagebox for green some information
    CTkMessagebox(title="Info", message="Invoice Created Successfully\nDocument Sent To Printer")

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
    invoice_number = invoicee.get()
    tax_exempt = tax_var.get()
    subtotal = sum(item[3] for item in invoice_list)
    salestax = round(subtotal * 0.06, 2)
    if tax_exempt == "on":
        total= round(subtotal, 2)
    else:    
        total = round(subtotal + salestax, 2)
    
    #create  the invoice word document
    doc.render({"name" : name,
                "phone":phone,
                "company_name" : company_name,
                "company_address" : company_address,
                "invoice_number" : invoice_number,
                "invoice_list" : invoice_list,
                "subtotal" : "$" + str(subtotal),
                "salestax": "$" + str(salestax),
                "total" : "$" + str(total)})
    today = date.today()
    doc_name ="invoice" + name + today.strftime("%b-%d-%Y") + ".docx"
    doc.save(doc_name)

    #print Invoice .
    lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
    lpr.stdin.write(bytes(doc_name, "utf-8"))

    #save to database
    db = sqlite3.connect("invoices.db")
    cr = db.cursor()
    cr.execute("create table if not exists invoices(Date integer, Name text, Phone_Number integer, Company name Text, Total integer)")
    client_infos = (today, name , phone, company_name, total)
    cr.execute("insert into invoices values(?, ?, ?, ?, ?)", client_infos)
    db.commit()
    db.close()

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
    invoicee.delete(0, ctk.END)
    cnamee.delete(0, ctk.END)
    caddresse.delete(0, ctk.END)
    cphonee.delete(0, ctk.END)
    caccounte.delete(0, ctk.END)
    clear_entry()
    clear()
    invoice_list.clear()  

def checkbox_event():
    print("checkbox toggled, current value:", tax_var.get())

frame1 = tk.LabelFrame(root, height=100, width =800, text="From", bg= "white")
frame1.grid(row=0 , column=0, padx = 20, pady = 5)

#label1 = ctk.CTkLabel(frame1, text = "From :")
#label1.grid(padx=2, row= 0, column=0, sticky ="w")

cnamel = ctk.CTkLabel(frame1, text="Company Name :")
cnamel.grid(row=1, column = 0, sticky ="w", padx=5)
cnamee = ctk.CTkEntry(frame1)
cnamee.grid(row=2, column = 0, padx=5, pady=10, sticky ="w")

caddressl = ctk.CTkLabel(frame1, text="Company Address :")
caddressl.grid(row=1, column = 1, sticky ="w", padx=5)
caddresse = ctk.CTkEntry(frame1, width= 250)
caddresse.grid(row=2, column = 1, padx=5, pady=10, sticky ="w")

cphonel = ctk.CTkLabel(frame1, text="Phone Number :")
cphonel.grid(row=1, column = 3, sticky ="w", padx=5)
cphonee = ctk.CTkEntry(frame1)
cphonee.grid(row=2, column = 3, padx=5, pady=10, sticky ="w")

caccountl = ctk.CTkLabel(frame1, text="Account Number :")
caccountl.grid(row=1, column = 4, sticky ="w", padx=5)
caccounte = ctk.CTkEntry(frame1, width= 250)
caccounte.grid(row=2, column = 4, padx=5, pady=10, sticky ="w")


frame = tk.LabelFrame(root, text= "Bill To ", bg= "white", width =800)
frame.grid(row=1 , column=0, padx = 20, pady = 10)

#billl = ctk.CTkLabel(frame, text= "Bill To :")
#billl.grid(padx=2, row = 0, column = 0, sticky = "w")

fnamel = ctk.CTkLabel(frame, text="First Name :")
fnamel.grid(row=1, column = 0, sticky ="w",padx=5)
fnamee = ctk.CTkEntry(frame)
fnamee.grid(row=2, column = 0, padx=5, sticky ="w")

lnamel = ctk.CTkLabel(frame, text="Last Name :")
lnamel.grid(row=1, column = 1, sticky ="w", padx=5)
lnamee = ctk.CTkEntry(frame)
lnamee.grid(row=2, column = 1, padx=5,sticky ="w")

companyl = ctk.CTkLabel(frame, text="Company Name :")
companyl.grid(row=1, column = 2, sticky ="w", padx=5)
companye = ctk.CTkEntry(frame)
companye.grid(row=2, column = 2, padx=5, sticky ="w")

phonel = ctk.CTkLabel(frame, text="Phone Number :")
phonel.grid(row=1, column = 3, sticky ="w", padx=5)
phonee = ctk.CTkEntry(frame)
phonee.grid(row=2, column = 3, padx=5, sticky ="w")

adressl = ctk.CTkLabel(frame, text="Company Address :")
adressl.grid(row=3, column = 0, pady = 10, sticky ="w", padx=5)
adresse = ctk.CTkEntry(frame, width=250)
adresse.grid(row=4, column = 0, padx=5, columnspan= 2, sticky ="w")

invoicel = ctk.CTkLabel(frame, text= "Invoice Number :")
invoicel.grid(row=3, column=3, sticky ="w", padx=5)
invoicee = ctk.CTkEntry(frame)
invoicee.grid(row=4, column =3, padx=5, sticky ="w")

qtyl = ctk.CTkLabel(frame, text= "Quantity :")
qtyl.grid(row=5, column=0, sticky ="w", padx=5)
qtye = ctk.CTkEntry(frame)
qtye.grid(row=6, column = 0, padx=5, sticky ="w")

descl = ctk.CTkLabel(frame, text="Product Description :")
descl.grid(row=5, column = 1, pady = 10, sticky ="w", padx=5)
desce = ctk.CTkEntry(frame)
desce.grid(row=6, column = 1, padx=5, sticky ="w")

pricel = ctk.CTkLabel(frame, text= "Price :")
pricel.grid(row=5, column=2, sticky ="w", padx=5)
pricee = ctk.CTkEntry(frame)
pricee.grid(row=6, column =2, padx=5, sticky ="w")

addb = ctk.CTkButton(frame, text="Add Item", command= add_item)
addb.grid(row=6, column= 3, padx=5)

columns = ("Qty", "Desc", "Price", "Total")
view = ttk.Treeview(frame, columns=columns, show="headings")
view.grid(row=8 , column= 0, columnspan=4, padx=5, pady=20)
view.heading("Qty", text="Quantity")
view.heading("Desc", text="Descrption")
view.heading("Price", text="Price")
view.heading("Total", text="Total")

#submit buton saves the document to .docx and saves it in the sqlite dtatbase and send the doc to the printer.
submit_invoice=ctk.CTkButton(frame, text="Submit Order", command=submit)
submit_invoice.grid(row=9,column=3, sticky="news", padx=10, pady = 10)

newinvoice=ctk.CTkButton(frame, text="New Order", command=new_invoice)
newinvoice.grid(row=9,column=2, sticky="news", padx= 10, pady=10)

clear_invoice=ctk.CTkButton(frame, text="Clear Order", command=clear)
clear_invoice.grid(row=9,column=1, sticky="news", padx =10, pady = 10)

tax_var = ctk.StringVar(value="off")
tax_box = ctk.CTkCheckBox(frame, text="Tax Exempt", command=checkbox_event,
                                     variable=tax_var, onvalue="on", offvalue="off")
tax_box.grid(row=9,column=0, sticky="news", padx =10, pady = 10)

#Submit Button already prints the document no need for a print Button.
#print_btn = ctk.CTkButton(frame, text= "Print")
#print_btn.grid(row = 9, column = 0 , sticky="news")

root.mainloop()