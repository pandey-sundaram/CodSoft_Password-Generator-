
import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import string
import csv
import os

# File to store passwords
password_file = 'saved_passwords.csv'
admin_password = 'admin123'  # Set your own secure admin password here

# Default theme colors
themes = {
    'light': {'bg': 'white', 'fg': 'black', 'entry_bg': 'white', 'entry_fg': 'black', 'button_bg': '#4CAF50', 'button_fg': 'white'},
    'dark': {'bg': '#1e1e2f', 'fg': 'white', 'entry_bg': 'white', 'entry_fg': 'black', 'button_bg': '#4CAF50', 'button_fg': 'white'}
}
current_theme = 'dark'

# Main window
root = tk.Tk()
root.title("Sundaram's Password Generator")
root.geometry("400x500")
root.config(bg=themes[current_theme]['bg'])

# Functions
def generate_password():
    length = int(length_entry.get())
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_numbers = number_var.get()
    include_symbols = symbol_var.get()
    purpose = purpose_entry.get()

    if not any([include_upper, include_lower, include_numbers, include_symbols]):
        messagebox.showwarning("Selection Error", "Select at least one character type.")
        return

    characters = ''
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

    if purpose:
        save_password(purpose, password)

def save_password(purpose, password):
    with open(password_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([purpose, password])

def view_passwords():
    pwd = simpledialog.askstring("Authentication", "Enter admin password:", show='*')
    if pwd != admin_password:
        messagebox.showerror("Access Denied", "Incorrect password.")
        return
    if not os.path.exists(password_file):
        messagebox.showinfo("No Records", "No passwords saved yet.")
        return

    view_win = tk.Toplevel(root)
    view_win.title("Saved Passwords")
    view_win.config(bg=themes[current_theme]['bg'])
    with open(password_file, 'r') as file:
        content = file.read()
    text_box = tk.Text(view_win, wrap=tk.WORD, bg=themes[current_theme]['entry_bg'], fg=themes[current_theme]['entry_fg'])
    text_box.insert(tk.END, content)
    text_box.pack(expand=True, fill='both')

def update_password():
    pwd = simpledialog.askstring("Authentication", "Enter admin password:", show='*')
    if pwd != admin_password:
        messagebox.showerror("Access Denied", "Incorrect password.")
        return

    purpose_to_update = simpledialog.askstring("Update", "Enter the purpose you want to update:")
    updated_password = simpledialog.askstring("Update", "Enter the new password:")

    if not os.path.exists(password_file):
        messagebox.showinfo("No Records", "No passwords saved yet.")
        return

    rows = []
    updated = False
    with open(password_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == purpose_to_update:
                row[1] = updated_password
                updated = True
            rows.append(row)

    if updated:
        with open(password_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        messagebox.showinfo("Updated", "Password updated successfully.")
    else:
        messagebox.showwarning("Not Found", "Purpose not found.")

def toggle_theme():
    global current_theme
    current_theme = 'light' if current_theme == 'dark' else 'dark'
    apply_theme()

def apply_theme():
    theme = themes[current_theme]
    root.config(bg=theme['bg'])
    for widget in root.winfo_children():
        try:
            widget.configure(bg=theme['bg'], fg=theme['fg'])
            if isinstance(widget, tk.Entry):
                widget.configure(bg=theme['entry_bg'], fg=theme['entry_fg'])
            if isinstance(widget, tk.Button):
                widget.configure(bg=theme['button_bg'], fg=theme['button_fg'])
        except:
            pass

# Widgets
tk.Label(root, text="Enter Password Length:").pack(pady=(10, 0))
length_entry = tk.Entry(root)
length_entry.insert(0, "8")
length_entry.pack()

tk.Label(root, text="Enter Purpose (e.g., Gmail, Bank):").pack()
purpose_entry = tk.Entry(root)
purpose_entry.pack()

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack()
tk.Checkbutton(root, text="Include Lowercase", variable=lower_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=number_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbol_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

tk.Label(root, text="Generated Password:").pack()
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Consolas", 12), justify='center')
password_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=lambda: root.clipboard_append(password_var.get())).pack(pady=5)
tk.Button(root, text="🔐 View Saved Passwords", command=view_passwords).pack(pady=5)
tk.Button(root, text="✏️ Update Existing Password", command=update_password).pack(pady=5)
tk.Button(root, text="🌗 Toggle Light/Dark Mode", command=toggle_theme).pack(pady=10)

apply_theme()
root.mainloop()
