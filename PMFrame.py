from tkinter import *
import random
import string

def generateRanPassword():
    pw = ""
    while len(pw) < 18:
        digit = random.randint(0, 9)
        Uletter = random.choice(string.ascii_uppercase)
        Lletter = random.choice(string.ascii_lowercase)
        RCharacter = random.choice("!@#$%&*?")
        PUse = [str(digit), Uletter, Lletter, RCharacter]
        pw += random.choice(PUse)
    msg1 = Message(PMWin, text="Your new password is " + pw)
    msg1.pack(side=TOP, pady=20)

PMWin = Tk()
PMWin.geometry("400x200")
PMWin.title('Super Cool Password Manager')

introMes = Label(PMWin, text = "Click below to generate your new password!")
introMes.pack()

superCoolButton = Button(PMWin, text = 'Press me', width= 27, command= generateRanPassword)
superCoolButton.pack()

PMWin.mainloop()


#extra code
#def labelUpdate():
    #lbl2 = passwordLabel()
    #lbl2.config(text= lbl1)
#lambda: [passwordLabel(), labelUpdate()]