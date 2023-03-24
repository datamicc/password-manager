
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) ==0:
        messagebox.showerror(title='Oops', message="Please don't leave any fields empty!" )

    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?')
        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_input.get()
    try:
        with open('data.json', 'r') as data_file_saved:
            data = json.load(data_file_saved)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found.')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email} \nWPassword: {password}')
        else:
            messagebox.showinfo(title='Error', message=f'No details for {website} exists.')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=20, padx=20)
window.title('Password Manager')

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_input = Entry(width=24)
website_input.grid(column=1, row=1)
website_input.focus()

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

email_input = Entry(width=42)
email_input.grid(column=1, row=2,columnspan=2)
email_input.insert(0, 'simba@gmail.com')


password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_input = Entry(width=24)
password_input.grid(column=1, row=3)

gen_password = Button(text='Generate Password', command=generate_password)
gen_password.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()