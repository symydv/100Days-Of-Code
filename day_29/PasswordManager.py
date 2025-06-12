from tkinter import *
from tkinter import messagebox 
import json
#messagebox is not a class thats why it is not imported woth everything
#check documentation of messagebox for more information
import random
import pyperclip
'''pyperclip is used for instantly copying anything 
to your clipboard without you selecting the line and 
you can also paste it anytime '''

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def genrate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list) 
    #join keyword joins the elements of a list with  "" in between them
    pass_Entry.insert(0,password)
    pyperclip.copy(password) #it will copy generated password to clipboard

# ---------------------------- SEARCH PASSWORD ------------------------------#

def Search():
    website = Web_Entry.get()
    try:
        with open("day_29/data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(message="No data file found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(message=f"Email: {email}\nPassword: {password}", title=website)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



# ---------------------------- SAVE PASSWORD ------------------------------- #

def Save():
    website = Web_Entry.get()
    email = mail_Entry.get()
    password = pass_Entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(Web_Entry.get()) == 0 or len(pass_Entry.get()) == 0:
        messagebox.showinfo(title="Error", message="Please dont leave any fields empty")
    else:
        try:
            with open("day_29/data.json","r") as file: #using "with" automatically closes file
                
                #reading the old data
                data = json.load(file)  #used to read data

        except FileNotFoundError:
            data = new_data

        else:
            #Updating the old data
            data.update(new_data)   #used to update data

        with open("day_29/data.json","w") as file:
            #Saving updated data
            json.dump(data, file, indent=4)  #used to write new data


            Web_Entry.delete(0,END)
            pass_Entry.delete(0,END)
      
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

lock_image = PhotoImage(file="./day_29/logo.png")
canvas = Canvas(width=200,height=200,highlightthickness=0)
canvas.create_image(100,100,image = lock_image)
#100,100 are expected position of generated image
canvas.grid(column=1,row=0)

website = Label(text="Website:")
website.grid(column=0,row=1)

Web_Entry = Entry(width=25)
Web_Entry.grid(column=1,row=1)

Web_Entry.focus()

mail = Label(text="Email/Username:")
mail.grid(column=0,row=2)

mail_Entry = Entry(width=50)
mail_Entry.grid(column=1,row=2,columnspan=2) #columnspane = 2 allows the column to expand in two columns starting from given column
mail_Entry.insert(0, "shyam@gmail.com") #0 shows that the text is indexed at position 0


password = Label(text="Password:")
password.grid(column=0,row=3)

pass_Entry = Entry(width=27)
pass_Entry.grid(column=1,row=3)


search = Button(text = "Search",command=Search)
search.config(width=14)
search.grid(column=2,row=1)

gen_pass = Button(text="Generate Password",command=genrate_password)
gen_pass.config(width=14)
gen_pass.grid(column=2,row=3)

Add = Button(text="Add", command=Save)
Add.config(width=45)
Add.grid(column=1,row=4,columnspan=2)

window.mainloop()