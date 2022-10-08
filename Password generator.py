import pyperclip, random
from tkinter import *
# The pyperclip module endbles copying of generated results
# The random module enables generation of random figures
# the tkinter module enables creation of an application window

root = Tk()

root.geometry('500x700') #Setting width and height of the tkinter window
passstr = StringVar() # stores the value as a string type variable
passlen = IntVar() # stores the value as an Int type

passlen.set(0) # setting initial length of the password to 0

def generate():
    password_key = ['a', 'b', 'c', 'd', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', 
    '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', ',', '<', '>', '?', '/', '.',
    '|', '[', ']', '{', '}'] # key values for password generation
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
Label(root, text = 'Password Generator', font = 'arial 27 bold', background="#F0FFFF").pack()
Label(root, text = 'Enter Password Length: ', background="#89CFF0").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text = 'Generate Password', command=generate, background='#00FFFF').pack(pady=7)
Entry(root, textvariable=passstr).pack(pady=3)
Button(root, text='Copy Password', command=clipboardcopy, background='#00FFFF').pack()

root.mainloop() #Loops the program so users can keep generating more passwords


