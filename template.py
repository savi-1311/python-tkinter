from tkinter import *
import random

top = Tk()
user_score = 0
pc_score = 0
def display1():
  global user_score
  global pc_score
  global run
  
  user = int(var.get())
  pc = int(random.randrange(1,3))
  if user == 1:
   L31 = Label(top, text = "User's Choice - Rock")
  elif user == 2: 
   L31 = Label(top, text = "User's Choice - Paper")
  else:
   L31 = Label(top, text = "User's Choice - Scissors")
  if pc == 1:
   L32 = Label(top, text = "System's Choice - Rock")
  elif pc == 2: 
   L32 = Label(top, text = "System's Choice - Paper")
  else:
   L32 = Label(top, text = "System's Choice - Scissors")


  if user == pc:
	  L4 = Label(top, text = "It's a TIE")
  elif user == 1 and pc == 2:
	  L4 = Label(top, text = "System WON!!")
	  pc_score = pc_score+1
  elif user == 2 and pc == 1:
	  L4 = Label(top, text = "Congratulations You WON!!")
	  user_score = user_score+1
  elif user == 2 and pc == 3:
	  L4 = Label(top, text = "System WON!!")
	  pc_score = pc_score+1
  elif user == 3 and pc == 2:
	  L4 = Label(top, text = "Congratulations You WON!!")
	  user_score = user_score+1
  elif user == 1 and pc == 3:
	  L4 = Label(top, text = "Congratulations You WON!!")
	  user_score = user_score+1
  elif user == 3 and pc == 1:
	  L4 = Label(top, text = "System WON!!")
	  pc_score = pc_score+1
  L5 = Label(top, text = "\n\n\n Scoreboard\n User -"+ str(user_score) + "\n System -" + str(pc_score) +"\n")	  
  L31.pack()
  L32.pack()
  L4.pack()
  L5.pack()
var = IntVar()  
R1 = Radiobutton(top, text="ROCK", variable=var, value=1)
R2 = Radiobutton(top, text="PAPER", variable=var, value=2)
R3 = Radiobutton(top, text="SCISSORS", variable=var, value=3)
L1 = Label(top, text= "Select Your Choice")
B2 = Button(top, text ="SUBMIT", command = display1)
R1.pack()
R2.pack()
R3.pack()
L1.pack()
B2.pack()
top.mainloop()
