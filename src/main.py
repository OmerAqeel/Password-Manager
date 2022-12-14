from tkinter import *
from tkinter import messagebox
import json

def findPassword():
    website = web_input.get()       # Getting the text from the entry (web_input)
    try:                            # Trying the below line of code to get the data (content) from data.json file
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:       # if the program faces FileNotFoundError 
        messagebox.showinfo(title="Error", message="No data file found.")   # Display the error message to the user 
    else:
        if website not in data:     # If the user entered a website that was not in the data.json file then follow the below code
            messagebox.showinfo(title="Information Missing", message="This website password is not in the data file, please click add to add it. ")
        if website in data:         # If the website is included in the data.json file than 
            email = data[website]["email"] 
            password = data[website]["password"] # Get the password 
            messagebox.showinfo(title=f"{website}", message=f"email: {email}\n password: {password}")

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
    global confirmed
    web = get_web()
    user = get_email()
    password = get_password()
    info_missing = False
    new_data = {
        web: {
            "email": user,
            "password": password,
        }
    }

    if len(web) == 0:
        messagebox.showinfo(title="Info missing", message="Please enter the website.")
        info_missing = True
    elif len(user) == 0:
        messagebox.showinfo(title="Info missing", message="Please enter the email address.")
        info_missing = True
    elif len(password) == 0:
        messagebox.showinfo(title="Info missing", message="Please enter the password.")
        info_missing = True
    if info_missing == False:
        confirmed = messagebox.askokcancel(title="Confirmation", message=f"Can you please confirm that the details are correct ? \nWebsite: "
                                                      f"{web} \nEmail: {user} \nPassword: {password}")

    if confirmed:
        try:
            with open("data.json", "r") as file:
                # Reading the data
                data = json.load(file)
                # Updating the data
                data.update(new_data)
            with open("data.json", "w") as file:
                # Saving the data to the data.json
                json.dump(data, file, indent=4)  # dumping the data into the file (data.txt)
                web_input.delete(0, END)
                password_input.delete(0, END)
        except FileNotFoundError:
            file = open("data.json", "a")
        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving the data to the data.json
                json.dump(data, file, indent=4)  # dumping the data into the file (data.txt)

        finally:
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

web_input = Entry(width=21)
web_input.focus()  # As soon as the program is ran the cursor will be on the website entry.
web_input.grid(row=2, column=1, columnspan=3)

user_input = Entry(width=35)
user_input.insert(0, "omrraqeel@gmail.com")
user_input.grid(row=3, column=2, columnspan=2)

password_input = Entry(width=35)
password_input.grid(row=4, column=2, columnspan=2)

# Buttons

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=5, column=2, columnspan=2)

search_btn = Button(text="Search", width="14", command=findPassword)
search_btn.grid(row=2, column=3, columnspan=2)

window.mainloop()
