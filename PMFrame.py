from tkinter import *
import random
import string

#function for the manage password page
def managepassword():
    #hides the original frame & widgets
    mainMenu.pack_forget()
    #shows new frame & widgets
    manpass.pack()

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
    npFrame.pack

#fucntion for returning to the main menu
def mmreturn2():
    #hides the password generator page
    npFrame.pack_forget()
    #shows main menu
    mainMenu.pack()

#function for the password generator - still in progress
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
    """
    extra code
    When the button is pressed, it generates a message. When it's pressed multiple
    times, the message stacks instead of being replaced. I can fix this
    within the main code easily, but I'm trying to make this fix
    within a defined function.

    def labelUpdate():
        #lbl2 = passwordLabel()
        #lbl2.config(text= lbl1)
    lambda: [passwordLabel(), labelUpdate()]
    """

#mainwindow setup
PMWin = Tk()
PMWin.geometry("500x400")
PMWin.title('Super Cool Password Manager')

#main menu page
mainMenu = Frame(PMWin)
mainMenu.pack()

welcomeMes = Label(mainMenu, text = "Welcome to the Super Cool Password Manager")
welcomeMes.pack()

managePassButton = Button(mainMenu, text = "Current Passwords", command = managepassword)
managePassButton.pack()

newPass = Button(mainMenu, text = "Password Generator", command = newpassword)
newPass.pack()

#password manager page
manpass = Frame(PMWin)
manpass.pack()

manlabel = Label(manpass, text = "Here are your current passwords")
manlabel.pack()

returnMM1 = Button(manpass, text = "Return to Main Menu", command = mmreturn1)
returnMM1.pack()


#password generator page
npFrame = Frame(PMWin)
npFrame.pack()

introMes = Label(npFrame, text = "Click below to generate your new password!")
introMes.pack()

superCoolButton = Button(npFrame, text = 'Press me', width= 27, command= generateRanPassword)
superCoolButton.pack()

returnMM2 = Button(npFrame, text = "Main Menu", command = mmreturn2)
returnMM2.pack()

PMWin.mainloop()