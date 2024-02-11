import tkinter as tk
from tkinter import messagebox

def add_to_input(symbol):
    current_input = entry_input.get()
    entry_input.delete(0, tk.END)
    entry_input.insert(tk.END, current_input + symbol)

def clear_input():
    entry_input.delete(0, tk.END)

def calculate():
    try:
        expression = entry_input.get()
        result = eval(expression)
        entry_input.delete(0, tk.END)
        entry_input.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

root = tk.Tk()
root.title("Simple Calculator")

# Create input field
entry_input = tk.Entry(root, width=30, font=('Arial', 14))
entry_input.grid(row=0, column=0, columnspan=4)

# Define buttons for numbers (0-9) and operation symbols
button_symbols = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons for numbers and symbols
for symbol, row, column in button_symbols:
    if symbol == '=':
        button = tk.Button(root, text=symbol, width=5, height=2, command=calculate)
    elif symbol == 'C':
        button = tk.Button(root, text=symbol, width=5, height=2, command=clear_input)
    else:
        button = tk.Button(root, text=symbol, width=5, height=2, command=lambda s=symbol: add_to_input(s))
    button.grid(row=row, column=column)

root.mainloop()
