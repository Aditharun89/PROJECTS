from tkinter import *
from PIL import Image,ImageTk
from random import randint
# main window
root = Tk()
root.title("rock paper scissors")
root.configure(background="red")


# pictures
rockimg = ImageTk.PhotoImage(Image.open("rock.jpeg"))
paperimg = ImageTk.PhotoImage(Image.open("paper.jpeg"))
scissorsimg = ImageTk.PhotoImage(Image.open("scissors.jpeg"))
rockimgcomp = ImageTk.PhotoImage(Image.open("rock.jpeg"))
paperimgcomp = ImageTk.PhotoImage(Image.open("paper.jpeg"))
scissorsimgcomp = ImageTk.PhotoImage(Image.open("scissors.jpeg"))

#insert image
userlabel = Label(root, image=rockimg,bg="red")
complabel = Label(root, image=rockimgcomp,bg="red")
complabel.grid(row=1, column=0)
userlabel.grid(row=1, column=4)

#scores
playerscore = Label(root,text=0,font=100,bg="red",fg="white")
computerscore = Label(root,text=0,font=100,bg="red",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

#indicators
userindicator = Label(root,font=50,text="USER",bg="red",fg="white")
compindicator = Label(root,font=50,text="COMPUTER",bg="red",fg="white")
userindicator.grid(row=0,column=3)
compindicator.grid(row=0,column=1)

#messages
msg = Label(root, font=50,bg="red",fg="white")
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
    msg["text"] = x

#update user score
def updateUserScore():
    score = int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)
#update computer score             
def updateCompScore():
    score = int(computerscore["text"])
    score +=1
    computerscore["text"] = str(score)
 
 #check winner
 
def checkWin(player,computer):
    if player == computer:
        updateMessage("ITS A TIE") 
    elif player == "rock":
        if computer == "paper":
            updateMessage("YOU LOSE")
            updateCompScore()
        else:
            updateMessage("YOU WIN")
            updateUserScore()
    elif player == "paper":
        if computer == "scissors":
            updateMessage("YOU LOSE")
            updateCompScore()
        else:
            updateMessage("YOU WIN")
            updateUserScore()
    elif player =="scissors":
        if computer == "rock":
            updateMessage("YOU LOSE")
            updateCompScore()
        else:
            updateMessage("YOU WIN")
            updateUserScore()
    else:
        pass              
             
             
             
                        

#update choices
choices = ["rock","paper","scissors"]
def updateChoice(x):
#for the computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        complabel.configure(image=rockimgcomp)
    elif compChoice == "paper":
        complabel.configure(image=paperimgcomp) 
    elif compChoice == "scissors":
        complabel.configure(image=scissorsimgcomp)      

#for the user
    if x=="rock":
        userlabel.configure(image=rockimg)
    elif x=="paper":
        userlabel.configure(image=paperimg)
    else:
        userlabel.configure(image=scissorsimg)        
           
    checkWin(x,compChoice) 



#buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissors = Button(root,width=20,height=2,text="SCISSORS",bg="#0ABDE3",fg="white",command=lambda:updateChoice("scissors")).grid(row=2,column=3)



root.mainloop()
