from tkinter import *
import string
import random

path = ""

def finalScreenPickUp(nameOfPerson):

    lastpg = Tk()

    lastpg.title("Smart Car Parking System")
    lastpg.iconbitmap('car.ico')
    lastpg.configure(background = "black")

    frame = LabelFrame(lastpg,padx = 100, pady = 50)
    frame.grid(padx = 10, pady = 10)
    frame.configure(background = "white")

 
    number = random.choice([1, 2, 3, 4, 6, 7, 8, 9, 10])
    alpha = random.choice(string.ascii_uppercase)

    stringInfo = "Thank you for using our application " + nameOfPerson + "." + "\n\nYou may take your car "

    ty_label = Label(frame, text = stringInfo,padx = 100, pady = 120,font = "Perpetua 24", bg="white")
    ty_label.grid(row = 0,column = 0)

    lastpg.mainloop()

def finalScreenDropOff(nameOfPerson):
    
    lastpg = Tk()  

    lastpg.title("Smart Car Parking System")
    lastpg.iconbitmap('car.ico')
    lastpg.configure(background = "black")

    frame = LabelFrame(lastpg,padx = 100, pady = 50)
    frame.grid(padx = 10, pady = 10)
    frame.configure(background = "white")

 
    number = random.choice([1, 2, 3, 4, 6, 7, 8, 9, 10])
    alpha = random.choice(string.ascii_uppercase)

    stringInfo = "Thank you for using our application " + nameOfPerson + "." + "\n\nThe Parking Slot generated for your car is: " + alpha + str(number)

    ty_label = Label(frame, text = stringInfo,padx = 100, pady = 120,font = "Perpetua 24", bg="white")
    ty_label.grid(row = 0,column = 0)

    lastpg.mainloop()
    
def FinalScreenRegister(nameOfPerson):
    
    lastpg = Tk()  

    lastpg.title("Smart Car Parking System")
    lastpg.iconbitmap('car.ico')
    lastpg.configure(background = "black")

    frame = LabelFrame(lastpg,padx = 100, pady = 50)
    frame.grid(padx = 10, pady = 10)
    frame.configure(background = "white")

 
    number = random.choice([1, 2, 3, 4, 6, 7, 8, 9, 10])
    alpha = random.choice(string.ascii_uppercase)

    stringInfo = "Thank you for using our application " + nameOfPerson + "."

    ty_label = Label(frame, text = stringInfo,padx = 100, pady = 120,font = "Perpetua 24", bg="white")
    ty_label.grid(row = 0,column = 0)

    lastpg.mainloop()

# finalScreenRegister()