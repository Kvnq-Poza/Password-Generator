from string import printable
import pyperclip, random
from tkinter import *
# The pyperclip module endbles copying of generated results
# The random module enables generation of random figures
# the tkinter module enables creation of an application window
# the string - printable module contains values (A-Z and other characters which can be used)

root = Tk()

root.geometry('500x700') #Setting width and height of the tkinter window
passstr = StringVar() # stores the value as a string type variable
passlen = IntVar() # stores the value as an Int type

passlen.set(0) # setting initial length of the password to 0

def generate():
    password_key = list(printable) # takes key values from the string - printable module for password generation
    password = "" # open varialbe for taking the password key
    
    for p in range(passlen.get()): 
        password = password + random.choice(password_key)
    passstr.set(password) # setting the password

def clipboardcopy():
    generated_password = passstr.get()
    pyperclip.copy(generated_password)

#GUI for application
#Label = description/direction in the GUI
#Entry = Box for user to input values
#Button = To pass the command and run function above
Label(root, text = 'Password Generator', font = '"agency fb" 27 bold', background="#F0FFFF").pack()
Label(root, text = 'Enter Password Length: ', background="#89CFF0").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text = 'Generate Password', command=generate, background='#00FFFF').pack(pady=7)
Entry(root, textvariable=passstr).pack(pady=3)
Button(root, text='Copy Password', command=clipboardcopy, background='#00FFFF').pack()

root.mainloop() #Loops the program so users can keep generating more passwords


