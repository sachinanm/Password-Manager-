from tkinter import *

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
email_label = Label(text="Username/Email")  # Changed the variable name to email_label
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="w", padx=(0, 10))  # Align left and add padding

add_button = Button(text="Add Password", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
