import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)
    password = ''.join(password_list)
    pyperclip.copy(password)

    password_entry.delete(9, 'end')
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def search():

    website = website_entry.get()
    try:
        with open('data.json', 'r') as f:
            data_dict = json.load(f)

    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No such data file exists')

    else:
        if website in data_dict:
            email = data_dict[website]['email']
            password = data_dict[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\n'
                                                       f'Password: {password}')
        else:
            messagebox.showerror(title='Error', message=f'No data for {website} found')



    # try:
    #     with open('data.json', 'r') as f:
    #         data_dict = json.load(f)
    #         for key, value in data_dict.items():
    #             if website_entry.get() == key:
    #                 messagebox.showinfo(title=key, message=f"Email: {data_dict[key]['email']}\n"
    #                                                        f"Password: {data_dict[key]['password']}")
    #                 website_entry.delete(0, 'end')
    #                 break
    #
    #             else:
    #                 messagebox.showerror(title='Error', message='No such data found')
    #                 website_entry.delete(0,'end')
    #                 break
    #
    # except FileNotFoundError:
    #     messagebox.showerror(title='Error', message='No data file exists.')



def save_password():

    new_data = {
        website_entry.get(): {
            'email': email_entry.get(),
            'password': password_entry.get(),
        }
    }

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title='Error', message='One or more fields are empty')

    else:
        try:
            with open('data.json', 'r') as f:
                # json.dump(new_data, f, indent=4)
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(new_data, f, indent=4)
        else:

            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# {
#     "test": {
#         "email": "mihyuniscute@irijori.com",
#         "password": "m9!)Du9HAsva8"
#     }
# }


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title('Password Manager')
window.config(bg='white', padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo_img = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website_label = tk.Label(text='Website:', bg='white', fg='black')
email_label = tk.Label(text='Email/Username:', bg='white', fg='black')
password_label = tk.Label(text='Password:',  bg='white', fg='black')

website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)


website_entry = tk.Entry(bg='white', fg='black', highlightthickness=0, width=21)
website_entry.focus()
email_entry = tk.Entry(bg='white', fg='black', highlightthickness=0, width=38)
email_entry.insert(0, 'irijori@irijori.com')
password_entry = tk.Entry(bg='white', fg='black', highlightthickness=0, width=21)

website_entry.grid(column=1, row=1)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)


generate_password_button = tk.Button(text='Generate Password', highlightthickness=0, highlightbackground='white', command=generate_password)
add_button = tk.Button(text='Add', highlightthickness=0, highlightbackground='white', width=36, command=save_password)
search_button = tk.Button(text='Search', highlightbackground='white', highlightthickness=0, width=13, command=search)

generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)
search_button.grid(column=2, row=1)








window.mainloop()