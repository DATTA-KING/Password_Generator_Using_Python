import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Length should be at least 4")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)

# Title
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Length input
tk.Label(root, text="Enter password length:").pack()
length_entry = tk.Entry(root, width=10, font=("Arial", 12))
length_entry.pack(pady=5)

# Generate button
tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=10)

# Password display
password_entry = tk.Entry(root, width=30, font=("Arial", 12))
password_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_password).pack(pady=10)

root.mainloop()