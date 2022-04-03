# All imports
import datetime as dt
import random
import string
from tkinter import *
from tkinter import filedialog
import pyperclip
import tkinter.font as font

window = Tk()

window.title('Password Generator')
window.geometry("600x400")
frame_tool = Frame(window, bg='white')
frame_tool.pack(fill='x')
myFont = font.Font(family="Helvetica", size=15)

# Welcome message
welcome_msg = Label(window, text='Password Generator', font=('Helvetica', 16), height=5)
welcome_msg.pack(side=TOP)

# All data Labels in the GUI
password_information = Label(window, text='Password for what ?', font='Helvetica 10 bold')
password_information.pack()
password_information_entry = Entry(window)
password_information_entry.pack()
password_label = Label(window, text='Password Length', font='Helvetica 10 bold')
password_label.pack()
password_length = IntVar()
length = Spinbox(window, from_=8, to=32, textvariable=password_length, width=15)
length.pack()
date = dt.datetime.now()
date_label = Label(window, text=date.strftime("%Y-%m-%d | %H:%M:%S"))
format_date = date.strftime("%Y-%m-%d | %H:%M:%S")

password = StringVar()


# Function to generate a random password
def generatePassword():
    last_password = ""
    password_group = list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(
        string.punctuation)
    for gen in range(password_length.get()):
        last_password += random.choice(password_group)
        password.set(last_password)


# Function to create a text file and save the data to it
def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[
        ("Text File", ".txt"),
        ("HTML file", ".html"),
        ("All files", ".*"),
    ])
    if file is None:
        return
    date_text = str(date_entry.get())
    pass_text = str(password_information_entry.get())
    file_text = str(password_entry.get())
    file.write(f"Password Created at: {date_text}")
    file.write('\n')
    file.write(f"Password usage for: {pass_text}")
    file.write('\n')
    file.write(f"Password is: {file_text}")
    file.close()


# Function to copy the generated password to clipboard
def copyToClipboard():
    pyperclip.copy(password.get())


# All inputs data in the GUI
gen_btn = Button(window, text='Generate', command=generatePassword)
gen_btn.pack(pady=5)
password_entry = Entry(window, textvariable=password)
password_entry.pack()
date_entry = Entry(window)
date_entry.insert(END, format_date)
save_btn = Button(text="Save", font=myFont, command=lambda: [saveFile(), copyToClipboard()])
save_btn.place(x=180, y=300, height=30, width=75)
btn_exit = Button(window, text="Exit", font=myFont, fg='red', command=window.destroy)
btn_exit.place(x=330, y=300, height=30, width=75)

# Show GUI
window.mainloop()
