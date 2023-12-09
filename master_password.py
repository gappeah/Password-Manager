from tkinter import messagebox

def verify_master_password():
    entered_password = master_password_entry.get()
    # Replace 'YourMasterPassword' with your desired master password
    if entered_password == 'YourMasterPassword':
        login_window.destroy()  # Close login window
        open_main_window()  # Open the main window
    else:
        messagebox.showerror("Error", "Incorrect Master Password")

def open_main_window():
    # This function should contain the code for displaying the main window with password manager functionality
    root = Tk()
    root.title('Password Manager')
    root.geometry("400x300")
    # ... (Rest of the code for the main window)

login_window = Tk()
login_window.title('Login')
login_window.geometry("300x150")

master_password_label = Label(login_window, text="Enter Master Password:")
master_password_label.pack()

master_password_entry = Entry(login_window, show="*")
master_password_entry.pack()

login_button = Button(login_window, text="Login", command=verify_master_password)
login_button.pack()

login_window.mainloop()

