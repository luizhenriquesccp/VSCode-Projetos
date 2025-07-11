import tkinter as tk
from tkinter import messagebox
import csv

# Function to register clien
def register_client():
    name = name_entry.get()
    surname = surname_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    if not (name and surname and email and phone):
        messagebox.showwarning("Missing Data", "All fields must be filled!")
        return

    with open("clients.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, surname, email, phone])

    messagebox.showinfo("Success", "Client registered successfully!")

    name_entry.delete(0, tk.END)
    surname_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Function to export database
def export_database():
    try:
        with open("clients.csv", "r", encoding="utf-8") as file:
            content = file.read()

        with open("exported_clients.csv", "w", encoding="utf-8") as export_file:
            export_file.write(content)

        messagebox.showinfo("Export Success", "Database exported successfully!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No database found to export!")

# Create main application window
root = tk.Tk()
root.title("Ferramenta de Cadastro de Clientes")
root.geometry("400x300")

# Labels and Entries
name_label = tk.Label(root, text="Nome")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

surname_label = tk.Label(root, text="Sobrenome")
surname_label.pack()
surname_entry = tk.Entry(root)
surname_entry.pack()

email_label = tk.Label(root, text="E-mail")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

phone_label = tk.Label(root, text="Telefone")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

# Buttons
register_button = tk.Button(root, text="Cadastrar Cliente", command=register_client)
register_button.pack(pady=10)

export_button = tk.Button(root, text="Exportar Base de Clientes", command=export_database)
export_button.pack(pady=5)

# Run the application
root.mainloop()
