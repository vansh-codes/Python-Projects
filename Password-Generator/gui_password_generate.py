import tkinter as tk
from tkinter import messagebox
import string
import random as r

def generate_password():
    try:
        n = int(length_entry.get())
        if n < 12:
            messagebox.showerror("Error", "Password must have a minimum of 12 characters.")
            return
        
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        sc = "!#$%&*+,-./:;=?@`~"
        combine = lower + upper + digits + sc
        
        r_l = r.choice(lower)
        r_u = r.choice(upper)
        r_d = r.choice(digits)
        r_sc = r.choice(sc)
        
        T = r_l + r_u + r_d + r_sc
        
        for _ in range(n - 4):
            T += r.choice(combine)
        
        t = list(T)
        r.shuffle(t)
        
        password = ''.join(t)
        password_entry.config(state=tk.NORMAL)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state=tk.DISABLED)
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def exit_app():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Create widgets
welcome_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16))
welcome_label.pack(pady=10)

length_label = tk.Label(root, text="Enter number of characters (minimum 12):")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Generated Password:")
password_label.pack()

# Frame to center the password entry
password_frame = tk.Frame(root)
password_frame.pack(padx=10,pady=5, fill=tk.X, expand=True)

password_entry = tk.Entry(password_frame, state=tk.DISABLED, width=50)
password_entry.pack(pady=5, padx=10, fill=tk.X, expand=True)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=10)

# Run the main loop
root.mainloop()
