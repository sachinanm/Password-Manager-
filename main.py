import string
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    length = 12  # You can adjust the length as needed
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user_name = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        new_data = {website: {
            "email": user_name,
            "password": password,
        }
        }
        try:
            with open("password.json", "r") as file:
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("password.json", "w") as file:
                # updating old data with new data
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("password.json", "w") as file:
                # saving new data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
password_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_png)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_entry = Label(text="Username/Email")
email_entry.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Entries

website_entry = Entry(width=53)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=53)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "sachin@gmail.com")

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add Password", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
