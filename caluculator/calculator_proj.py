import customtkinter as ctk



root= ctk.CTk()
root.title("Calculator")
root.geometry("300x420")
root.resizable(0, 0)
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'bt_clear' function :This is used to clear 
# the input field

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 
# 'bt_equal':This method calculates the expression 
# present in input field
 
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
 
expression = ""
 
# 'StringVar()' :It is used to get the instance of input field
 
input_text = ctk.StringVar()


entry_int = ctk.IntVar()
frame1= ctk.CTkFrame(root, width= 300, height= 60)
frame1.pack()
entry= ctk.CTkEntry(frame1, textvariable=input_text, font=("roboto", 24),width= 300, height= 60)
entry.pack(pady=5,padx=5, anchor=ctk.W)

frame2= ctk.CTkFrame(root)
frame2.pack(padx =5, pady= 5)
button7 = ctk.CTkButton(frame2, text = 7, width=60, height=50, command = lambda: btn_click(7))
button7.grid(row=0, column=1, padx = 5, pady=10)
button8 = ctk.CTkButton(frame2, text = 8, width=60, height=50, command = lambda: btn_click(8))
button8.grid(row=0, column=2, padx = 5, pady=10)
button9 = ctk.CTkButton(frame2, text = 9, width=60, height=50, command = lambda: btn_click(9))
button9.grid(row=0, column=3, padx = 5, pady=10)
buttondiv = ctk.CTkButton(frame2, text = "/", width=60, height=50, command = lambda: btn_click("/"))
buttondiv.grid(row=0, column=4, padx =5, pady=10)


button4 = ctk.CTkButton(frame2, text = 4, width=60, height=50, command = lambda: btn_click(4))
button4.grid(row=1, column=1, padx = 5, pady=10)
button5 = ctk.CTkButton(frame2, text = 5, width=60, height=50, command = lambda: btn_click(5))
button5.grid(row=1, column=2, padx = 5, pady=10)
button6 = ctk.CTkButton(frame2, text = 6, width=60, height=50, command = lambda: btn_click(6))
button6.grid(row=1, column=3, padx = 5, pady=10)
buttonmul = ctk.CTkButton(frame2, text = "*", width=60, height=50, command = lambda: btn_click("*"))
buttonmul.grid(row=1, column=4, padx =5, pady=10)


button1 = ctk.CTkButton(frame2, text = 1, width=60, height=50, command = lambda: btn_click(1))
button1.grid(row=2, column=1, padx = 5, pady=10)
button2 = ctk.CTkButton(frame2, text = 2, width=60, height=50, command = lambda: btn_click(2))
button2.grid(row=2, column=2, padx = 5, pady=10)
button3 = ctk.CTkButton(frame2, text = 3, width=60, height=50, command = lambda: btn_click(3))
button3.grid(row=2, column=3, padx = 5, pady=10)
buttonsub = ctk.CTkButton(frame2, text = "-", width=60, height=50, command = lambda: btn_click("-"))
buttonsub.grid(row=2, column=4, padx =5, pady=10)


button0 = ctk.CTkButton(frame2, text = 0, width=60, height=50, command = lambda: btn_click(0))
button0.grid(row=3, column=1, padx = 5, pady=10)
buttondot = ctk.CTkButton(frame2, text = ".", width=60, height=50, command = lambda: btn_click("."))
buttondot.grid(row=3, column=2, padx = 5, pady=10)
buttonequ = ctk.CTkButton(frame2, text ="=", width=60, height=50, command = lambda: bt_equal())
buttonequ.grid(row=3, column=3, padx = 5, pady=10)
buttonadd = ctk.CTkButton(frame2, text = "+", width=60, height=50, command = lambda: btn_click("+"))
buttonadd.grid(row=3, column=4, padx =5, pady=10)


buttonmod = ctk.CTkButton(frame2, text = "%", width=60, height=30, command = lambda: btn_click("%"))
buttonmod.grid(row=4, column=1, padx = 5, pady=10)
buttonpi = ctk.CTkButton(frame2, text = "π", width=60, height=30, command = lambda: btn_click(3.14159265359))
buttonpi.grid(row=4, column=2, padx = 5, pady=10)
buttonint = ctk.CTkButton(frame2, text = "//", width=60, height=30, command = lambda: btn_click("//"))
buttonint.grid(row=4, column=3, padx = 5, pady=10)
buttondel = ctk.CTkButton(frame2, text = "Clear", width=60, height=30, command = lambda: bt_clear())
buttondel.grid(row=4, column=4, padx = 5, pady=10)



root.mainloop()
