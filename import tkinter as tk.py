import tkinter as tk
from tkinter import messagebox

# Sample accounts
accounts = {
    '97686655': {'pin': '4276', 'balance': 5000},
    '68576488': {'pin': '6467', 'balance': 3000},
    '76465385': {'pin': '6758', 'balance': 10000},
}

current_user = None

# Main App Window
app = tk.Tk()
app.title("ATM Simulation")
app.geometry("400x400")

# Frames
login_frame = tk.Frame(app)
menu_frame = tk.Frame(app)

# ==== Login Screen ====
def show_login():
    menu_frame.pack_forget()
    login_frame.pack()

def login():
    global current_user
    card = card_entry.get()
    pin = pin_entry.get()

    if card in accounts and accounts[card]['pin'] == pin:
        current_user = card
        messagebox.showinfo("Success", "Login successful!")
        show_menu()
    else:
        messagebox.showerror("Error", "Invalid card number or PIN.")

tk.Label(login_frame, text="Card Number").pack()
card_entry = tk.Entry(login_frame)
card_entry.pack()

tk.Label(login_frame, text="PIN").pack()
pin_entry = tk.Entry(login_frame, show='*')
pin_entry.pack()

tk.Button(login_frame, text="Login", command=login).pack()

# ==== ATM Menu ====
def show_menu():
    login_frame.pack_forget()
    menu_frame.pack()

def check_balance():
    balance = accounts[current_user]['balance']
    messagebox.showinfo("Balance", f"Your balance is Rs. {balance}")

def deposit():
    amount = simple_input("Enter amount to deposit:")
    if amount:
        accounts[current_user]['balance'] += amount
        messagebox.showinfo("Deposit", "Deposit successful!")

def withdraw():
    amount = simple_input("Enter amount to withdraw:")
    if amount:
        if amount > accounts[current_user]['balance']:
            messagebox.showerror("Error", "Insufficient balance.")
        else:
            accounts[current_user]['balance'] -= amount
            messagebox.showinfo("Withdraw", "Withdrawal successful!")

def logout():
    global current_user
    current_user = None
    messagebox.showinfo("Logout", "You have been logged out.")
    show_login()

tk.Button(menu_frame, text="Check Balance", command=check_balance).pack(pady=5)
tk.Button(menu_frame, text="Deposit", command=deposit).pack(pady=5)
tk.Button(menu_frame, text="Withdraw", command=withdraw).pack(pady=5)
tk.Button(menu_frame, text="Logout", command=logout).pack(pady=5)

# ==== Helper Input Window ====
def simple_input(prompt):
    def submit():
        try:
            value = float(entry.get())
            top.destroy()
            result[0] = value
        except:
            messagebox.showerror("Invalid", "Please enter a valid number.")

    top = tk.Toplevel(app)
    top.title("Input")
    tk.Label(top, text=prompt).pack()
    entry = tk.Entry(top)
    entry.pack()
    result = [None]
    tk.Button(top, text="Submit", command=submit).pack()
    app.wait_window(top)
    return result[0]

# Start at login
show_login()
app.mainloop()
