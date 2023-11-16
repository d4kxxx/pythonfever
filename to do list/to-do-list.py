import customtkinter as ctk
import tkinter as tk


root = ctk.CTk()
root.title("To Do List")
root.resizable(0, 0)
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


frame1 = tk.LabelFrame(root, width=300, height=500, text=" Tasks | List", bg="white")
frame1.grid(padx=10, pady=10)
frame1.grid_propagate(0)

frame = ctk.CTkFrame(root)
frame.grid(pady=10)


def add_todo_item():
    todo_text = entry.get()
    if not todo_text:
        return

    # Create a checkbox for each todo item
    checkbox = ctk.CTkCheckBox(frame1, text=todo_text)
    checkbox.grid(padx=5, pady=5, sticky='w')

    # Clear the input field after adding a todo item
    entry.delete(0, 'end')


def clear_list():
    for child in frame1.winfo_children():
        if isinstance(child, ctk.CTkCheckBox):
            child.destroy()
    

entry = ctk.CTkEntry(frame, width=300, placeholder_text="Type Your Task here")
entry.grid(row=2)

button = ctk.CTkButton(frame, text="Add Task| Item", width=300, command=add_todo_item)
button.grid(pady=10)

clear_btn = ctk.CTkButton(frame, text="Clear List", width=300, command=clear_list)
clear_btn.grid(pady=10)

root.mainloop()
