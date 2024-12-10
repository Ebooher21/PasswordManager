from tkinter import *
import random
import string

#function for the manage password page
def managepassword():
    #hides the original frame & widgets
    mainMenu.pack_forget()
    #shows new frame & widgets
    manpass.pack()

    #replaces label and button when returned to frame
    if hasattr(manpass, 'manlabel') and hasattr(manpass, 'returnMM1'):
        manpass.manlabel.destroy()
        manpass.returnMM1.destroy()

    manpass.manlabel = Label(manpass, text = "Here are your current passwords")
    manpass.manlabel.pack()

    manpass.returnMM1 = Button(manpass, text = "Return to Main Menu", command = mmreturn1)
    manpass.returnMM1.pack()

def mmreturn1():
    #hides the password page
    manpass.pack_forget()
    #shows main menu
    mainMenu.pack()

#function for the generate password page
def newpassword():
    #hides the main menu
    mainMenu.pack_forget()
    #shows password page
    npFrame.pack()

    #replaces widgets when returned to page
    global npLabel
    global superCoolButton
    global returnMM2
    global npLbl
    if hasattr(npFrame, 'npLabel') and hasattr(npFrame, 'superCoolButton') and hasattr(npFrame, 'returnMM2') and hasattr(npFrame, 'npLbl'):
        npFrame.npLabel.destroy()
        npFrame.superCoolButton.destroy()
        npFrame.returnMM2.destroy()
        npFrame.npLbl.destroy()

    npFrame.npLabel = Label(npFrame, text = "Click below to generate your new password!")
    npFrame.npLabel.pack()

    npFrame.superCoolButton = Button(npFrame, text = "Press me", width= 27, command= generateRanPassword)
    npFrame.superCoolButton.pack()

    npFrame.returnMM2 = Button(npFrame, text = "Main Menu", command = mmreturn2)
    npFrame.returnMM2.pack()

#fucntion for returning to the main menu
def mmreturn2():
    #hides the password generator page
    npFrame.pack_forget()
    #shows main menu
    mainMenu.pack()

#function for the password generator
def generateRanPassword():
    pw = ""
    while len(pw) < 18:
        digit = random.randint(0, 9)
        Uletter = random.choice(string.ascii_uppercase)
        Lletter = random.choice(string.ascii_lowercase)
        RCharacter = random.choice("!@#$%&*?")
        PUse = [str(digit), Uletter, Lletter, RCharacter]
        pw += random.choice(PUse)

    #replaces label when returned to frame - I may mess with this in the future
    global npLbl
    if hasattr(npFrame, 'npLbl'):
        npFrame.npLbl.destroy()
    
    npFrame.npLbl = Label(npFrame, text="Your new password is " + pw)
    npFrame.npLbl.pack(side=TOP, pady=20)

#mainwindow setup
PMWin = Tk()
PMWin.geometry("500x400")
PMWin.title('Super Cool Password Manager')

#welcome page
#welcome = Frame(PMWin)

#main menu page
mainMenu = Frame(PMWin)
mainMenu.pack()

welcomeMes = Label(mainMenu, text = "Welcome to the Super Cool Password Manager")
welcomeMes.pack()

managePassButton = Button(mainMenu, text = "Current Passwords", command = managepassword)
managePassButton.pack()

newPass = Button(mainMenu, text = "Password Generator", command = newpassword)
newPass.pack()

#password manager frame
manpass = Frame(PMWin)
manpass.pack()

#password generator frame
npFrame = Frame(PMWin)
npFrame.pack()

PMWin.mainloop()