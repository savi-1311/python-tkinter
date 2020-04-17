from tkinter import *

top = Tk()

def display1():
	 x = E1.get()
	 y = E2.get()
	 v = int(var.get())

	 if v == 1:
	  z = int(int(x)+int(y))
	  k = str(z)
	  L3 = Label(top, text="The Sum is "+ k)
	 elif v == 2:
	  z = int(int(x)-int(y))
	  k = str(z)
	  L3 = Label(top, text="The Difference is "+ k)
	 elif v == 3:
	  z = int(int(x)*int(y))
	  k = str(z)
	  L3 = Label(top, text="The Product is "+ k)
	 else:
	  z = int(int(x)/int(y))
	  k = str(z)
	  L3 = Label(top, text="The Quotient is "+ k)
	  
	 L3.pack()
  
var = IntVar()  
R1 = Radiobutton(top, text="Addition", variable=var, value=1)
R2 = Radiobutton(top, text="Subtraction", variable=var, value=2)
R3 = Radiobutton(top, text="Multiplication", variable=var, value=3)
R4 = Radiobutton(top, text="Division", variable=var, value=4)
L1 = Label(top, text="Enter the numbers-")
E1 = Entry(top, bd =5, justify = CENTER)
E2 = Entry(top, bd =5, justify = CENTER)
B2 = Button(top, text ="SUBMIT", command = display1)
R1.pack()
R2.pack()
R3.pack()
R4.pack()
L1.pack()
E1.pack()
E2.pack()
B2.pack()
top.mainloop()
