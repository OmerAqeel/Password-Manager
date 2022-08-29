from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_web():
    web = web_input.get()
    return web


def get_email():
    email = user_input.get()
    return email


def get_password():
    password = password_input.get()
    return password


def save():
    web = get_web()
    user = get_email()
    password = get_password()
    confirmed = messagebox.askokcancel(title="Confirmation", message=f"Can you please confirm that the details are correct ? \nWebsite: "
                                                      f"{web} \nEmail: {user} \nPassword: {password}")
    if confirmed:
        with open("data.txt", "a") as file:
            file.write(f"{web} | {user} | {password}\n")
            web_input.delete(0, END)
            password_input.delete(0, END)
        
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(height=400, width=200)
window.config(padx=200, pady=20)
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=2)

# Labels

web_label = Label(text="Website: ", font=("Helvetica", 14, "normal"))
web_label.grid(row=2, column=1)

email_label = Label(text="Email/Username: ", font=("Helvetica", 14, "normal"))
email_label.grid(row=3, column=1)

password_label = Label(text="Password: ", font=("Helvetica", 14, "normal"))
password_label.grid(row=4, column=1)

# Inputs

web_input = Entry(width=35)
web_input.focus()  # As soon as the program is ran the cursor will be on the website entry.
web_input.grid(row=2, column=2, columnspan=2)

user_input = Entry(width=35)
user_input.insert(0, "omrraqeel@gmail.com")
user_input.grid(row=3, column=2, columnspan=2)

password_input = Entry(width=21)
password_input.grid(row=4, column=1, columnspan=3)

# Buttons

generate_btn = Button(text="Generate Password", width=14)
generate_btn.grid(row=4, column=3)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=5, column=2, columnspan=2)

window.mainloop()
