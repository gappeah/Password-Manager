import sqlite3
import hashlib
from tkinter import *
import ttkbootstrap as ttk

# Function to hash passwords using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to create a database table for passwords
def create_table():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    website TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Function to add passwords to the database
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    encrypted_password = hash_password(password)
    
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)', (website, username, encrypted_password))
    conn.commit()
    conn.close()

# Function to display stored passwords
def display_passwords():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('SELECT * FROM passwords')
    rows = c.fetchall()
    conn.close()

    for row in rows:
        print(row)

# GUI Setup
root = ttk.Window(themename="pulse")
root.title("Password Manager")
root.geometry("720x250")



website_label = Label(root, text='Website:')
website_label.grid(row=0, column=0)
website_entry = Entry(root)
website_entry.grid(row=0, column=1)

username_label = Label(root, text='Username:')
username_label.grid(row=1, column=0)
username_entry = Entry(root)
username_entry.grid(row=1, column=1)

password_label = Label(root, text='Password:')
password_label.grid(row=2, column=0)
password_entry = Entry(root, show='*')
password_entry.grid(row=2, column=1)


add_button = Button(root, text='Add Password', font=("Helvetica", 9), command=add_password)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

display_button = Button(root, text='Display Passwords',font=("Helvetica", 9), command=display_passwords)
display_button.grid(row=4, column=0, columnspan=2, pady=10)

create_table()  # Create the table if not exists
root.mainloop()
