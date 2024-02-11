import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate():
    try:
        length = int(entry_length.get())
        if length > 0:
            password = generate_password(length)
            entry_password.delete(0, tk.END)
            entry_password.insert(tk.END, password)
            entry_password.config(fg="green")
        else:
            messagebox.showerror("Error", "Please enter a positive length.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")

def reset():
    entry_length.delete(0, tk.END)
    entry_password.delete(0, tk.END)

root = tk.Tk()
root.title("Password Generator")

# Create labels and entry widgets
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_length = tk.Label(root, text="Password Length:")
label_length.grid(row=1, column=0, padx=10, pady=5)
entry_length = tk.Entry(root)
entry_length.grid(row=1, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Generated Password:")
label_password.grid(row=2, column=0, padx=10, pady=5)
entry_password = tk.Entry(root)
entry_password.grid(row=2, column=1, padx=10, pady=5)

# Create generate and reset buttons
generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")

root.mainloop()
