import tkinter as tk
from tkinter import messagebox, simpledialog, font

# Initial data
names = ["Vansh", "Sarthak", "Ritesh", "Anshul", "Prateek"]
contacts = ["1", "2", "3", "4", "5"]
n1 = []
c1 = []

# Function definitions
def search():
    user = simpledialog.askstring("Search", "Enter name to be searched for:", parent=root)
    if user in names:
        idx = names.index(user)
        messagebox.showinfo("Search Result", f"Contact: {contacts[idx]}", parent=root)
    else:
        messagebox.showerror("Error", "Name not found in repository", parent=root)

def display():
    if len(names) == len(contacts):
        display_text = ""
        for i in range(len(names)):
            display_text += f"Name: {names[i]}\nContact: {contacts[i]}\n\n"
        messagebox.showinfo("Display", display_text, parent=root)
    else:
        messagebox.showerror("Error", "ERROR404", parent=root)

def update():
    user = simpledialog.askstring("Update", "Enter name to be updated:", parent=root)
    if user in names:
        idx = names.index(user)
        c = simpledialog.askstring("Update", "Enter your contact number to get access:", parent=root)
        if c == contacts[idx]:
            update_choice = simpledialog.askinteger("Update", "What do you want to update?\n1. Name\n2. Contact number\n3. Exit", parent=root)
            if update_choice == 1:
                new_name = simpledialog.askstring("Update", "Enter updated name:", parent=root)
                names[idx] = new_name
                messagebox.showinfo("Update", "Name updated successfully", parent=root)
            elif update_choice == 2:
                new_contact = simpledialog.askstring("Update", "Enter updated number:", parent=root)
                contacts[idx] = new_contact
                messagebox.showinfo("Update", "Contact updated successfully", parent=root)
        else:
            messagebox.showerror("Error", "Incorrect contact number", parent=root)
    else:
        messagebox.showerror("Error", "Name not found in repository", parent=root)

def add():
    while True:
        new_name = simpledialog.askstring("Add", "Enter name:", parent=root)
        new_contact = simpledialog.askstring("Add", "Enter contact number:", parent=root)
        names.append(new_name)
        contacts.append(new_contact)
        messagebox.showinfo("Add", "Added successfully", parent=root)
        more = messagebox.askquestion("Add", "Do you want to add more?", icon='question', parent=root)
        if more == 'no':
            break

def delete():
    user = simpledialog.askstring("Delete", "Enter name to be deleted:", parent=root)
    if user in names:
        idx = names.index(user)
        c = simpledialog.askstring("Delete", "Enter your contact number to get access:", parent=root)
        if c == contacts[idx]:
            sure = messagebox.askquestion("Delete", "Are you sure you want to delete?", icon='warning', parent=root)
            if sure == 'yes':
                del names[idx]
                del contacts[idx]
                messagebox.showinfo("Delete", "Deleted successfully", parent=root)
        else:
            messagebox.showerror("Error", "Incorrect contact number", parent=root)
    else:
        messagebox.showerror("Error", "Name not found in repository", parent=root)

def extract_multiple():
    n1.clear()
    c1.clear()
    while True:
        m = simpledialog.askstring("Extract", "Enter name:", parent=root)
        if m in names:
            n1.append(m)
            more = messagebox.askquestion("Extract", "Do you want to add more?", icon='question', parent=root)
            if more == 'no':
                break
        else:
            messagebox.showerror("Error", f"Name {m} not found in the repository", parent=root)
    
    for name in n1:
        idx = names.index(name)
        c1.append(contacts[idx])
    
    display_multiple()

def display_multiple():
    display_text = ""
    for i in range(len(n1)):
        display_text += f"Name: {n1[i]}\nContact: {c1[i]}\n\n"
    messagebox.showinfo("Multiple Contacts", display_text, parent=root)

# GUI setup
root = tk.Tk()
root.title("Contact Management System")
root.geometry("400x500")
root.minsize(400, 500)

# Custom Font
custom_font = font.Font(family="Helvetica", size=12)

# Title Label
title_label = tk.Label(root, text="Contact Management System", font=("Helvetica", 16, "bold"))
title_label.pack(pady=20)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(pady=20)

button_font = font.Font(family="Helvetica", size=12)

tk.Button(frame, text="Search", command=search, width=20, font=button_font).grid(row=0, column=0, pady=10)
tk.Button(frame, text="Display", command=display, width=20, font=button_font).grid(row=1, column=0, pady=10)
tk.Button(frame, text="Update", command=update, width=20, font=button_font).grid(row=2, column=0, pady=10)
tk.Button(frame, text="Add", command=add, width=20, font=button_font).grid(row=3, column=0, pady=10)
tk.Button(frame, text="Delete", command=delete, width=20, font=button_font).grid(row=4, column=0, pady=10)
tk.Button(frame, text="Extract Multiple", command=extract_multiple, width=20, font=button_font).grid(row=5, column=0, pady=10)
tk.Button(frame, text="Exit", command=root.quit, width=20, font=button_font).grid(row=6, column=0, pady=10)

root.mainloop()