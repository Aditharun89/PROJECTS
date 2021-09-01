from tkinter import *
import sqlite3


data = Tk()
data.title('data storage')
data.geometry("600x600")


# creating data base
database = sqlite3.connect('address_storage.db')
c = database.cursor()



# Function for the database

def submit():
        database = sqlite3.connect('address_storage.db')
        c = database.cursor()

        c.execute("INSERT INTO address VALUES(:NAME, :EMAIL, :contact)",
                  {
                      'NAME': NAME.get(),
                      'EMAIL': email.get(),
                      'CONTACT': CONTACT.get()
                  })
        database.commit()
        database.close()
        NAME.delete(0, END)
        email.delete(0, END)
        CONTACT.delete(0, END)
        
        
# creating table

'''
c.execute("""CREATE TABLE address (
            NAME text,
            EMAIL text,
            CONTACT integer)""")
'''


def que():
    database = sqlite3.connect('address_storage.db')
    c = database.cursor()
    c.execute("SELECT *,oid FROM address")
    record = c.fetchall()
    print(record)
    for records in record:
        record += str(records[0]) + '\n'

    que_labels = Label(data, text=record)
    que_labels.grid(row=7, column=0, columnspan=2)

    database.commit()
    database.close()


# Text Lables

NAME_labels = Label(data, text='NAME')
NAME_labels.grid(row=2, column=0)

email_labels = Label(data, text='EMAIL')
email_labels.grid(row=3, column=0)

CONTACT_labels = Label(data, text='NUMBER')
CONTACT_labels.grid(row=4, column=0)

    

# Text Boxes

NAME = Entry(data, width=40)
NAME.grid(row=2, column=3, padx=25)

email = Entry(data, width=40)
email.grid(row=3, column=3)

CONTACT = Entry(data, width=40)
CONTACT.grid(row=4, column=3)



# Buttons

submit_btn = Button(data, text="ADD DATA", command=submit)
submit_btn.grid(row=5, column=0, columnspan=3, pady=30, padx=30, ipadx=50)

que_btn = Button(data,text="VIEW DATA",command=que)
que_btn.grid(row=6, column=0,  columnspan=3, pady=20, padx=20, ipadx=50)



database.commit()
database.close()
data.mainloop()