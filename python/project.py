import keyword

print("following are the keywords of python")
print(keyword.kwlist)

<!--print(ord('#'))
print(ord('$'))
print(ord('R'))
print(ord('A'))
print(ord('M'))


95 to 112   ->lower case alphaets

118 to 126  ->upper case alphabets



# Default function to implement conditions to check leap year  
def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
  # Else it is not a leap year  
  else:  
    print ("Given Year is not a leap Year")  

# Taking an input year from user  
Year = int(input("Enter the number: "))  
# Printing result  
CheckLeap(Year)  


#Homework
#========
print("Enter a Character: ", end="")
c = input()
if len(c)>1:
    print("\nInvalid Input!")
else:
    if c>='a' and c<='z':
        print("\n\"" +c+ "\" is an alphabet.")
    elif c>='A' and c<='Z':
        print("\n\"" +c+ "\" is an alphabet.")
    else:
        print("\n\"" +c+ "\" is not an alphabet!")


age = int(input("how old are you?:"))
if age >10:
    if age>=10 and age<=20:
        print("you are allowed in class age limit in between 10 and 20")
    else:
        print("you are not allowed in class")
else:
    print("you are too young for the class")
    


import math
number=int(input("tell a no"))
power=int(input("enter the power no"))
print(math.pow(number,power))


num = int(input("Enter any number\n"))


count = 0

while num != 0:
  count+=1
  num=num//10

print(count)


def converttobinary(n):
  if n > 1:
    converttobinary(n//2 )
  print(n%2 , end=" " )

dec=float(input("enter a number to find it's binary value"))
converttobinary(dec)
print()

dec=float(input("enter a number to find it's binary value"))

def converttobinary(n):
  if n > 1:
    converttobinary(n//2 )
  print(n%2 , end=" " )


converttobinary(dec)
print()


r = int(input(" Enter the Total Number of Rows  : "))

print("Mirrored Right Triangle Star Pattern") 
for i in range(1,r+1):
    for j in range(1,r+1):
        if(j <= r -i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
    print()



import turtle
t = turtle.Turtle()
s = int(input("Enter the length of the side of the Square: "))  
for i in range(4):
  # drawing first side
  t.forward(50) # Forward turtle by s units
  t.left(90) # Turn turtle by 90 degree


import math

radius = float (input("enter the radius of a circle:"))

circumference= 2*math.pi* radius
print("circumference of a circle is :%.2f "% circumference)

import os

shutdown = input("do you wish to shutdown your computer ? (yes or no):")

if shutdown == 'no':
 exit()
else:
  os.system("shutdown /s /t 1")

price = 2.50
#define a function to calculate the difference between the amount given and price mentioned
def calculate_change(amount_given):
	return amount_given - price

c = calculate_change(4.00)
print("Change the customer is due", c)


def enterage(age):

#define function to take input as natural number
    if age < 0:  #condition 1
        raise ValueError("Only positive integers are allowed")
    if age % 2 == 0: #condition 2
        print("age is even")
    else:
        print("age is odd")

try: 
    num = int(input("Enter your age: "))
    enterage(num)

#handles value error exception    
except ValueError:
    print("Only positive integers are allowed")
	
except:
    print("something is wrong")


#importing math
#using maths function for calculating trignometric values
import math 

a = math.sin(0.5)
b = math.cos(0.5)
c = math.tan(0.5)

print("value of sin(0.5)= ",a)
print("value of cos(0.5)= ",b)
print("value of tan(0.5)= ",c)


# importing calendar module
import calendar

yy = 2021 # year
mm = 12    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


Find Symmetric Difference for :

A. Set1 = {'blue', 'green'} Set2 = {'blue', 'yellow'}
B. Set1 = {1, 2, 3, 4, 5} Set2 = {1, 5, 6, 7, 8, 9}


# create a class
class pair_elements:
	
	def twoSum(self, nums, target):
		# create an empty dictionary
		lookup = {}

		# Iterate through the tuple
		for i, num in enumerate(nums):
			if target - num in lookup:
				return (lookup[target - num], i )
			lookup[num] = i

# take input of dum from the user
value = int(input("Enter sum for which you want to make this search : "))
print("index1=%d, index2=%d" % pair_elements().twoSum((10,20,30,40,50,60,70),value))

# Python program to demonstrate
# issubclass()


# Defining Parent class
class Vehicles:

	# Constructor
	def __init__(vehicleType):
		print('Vehicles is a ', vehicleType)

# Defining Child class
class Car(Vehicles):

	# Constructor
	def __init__(self):
		Vehicles.__init__('Car')

# Driver's code
print(issubclass(Car, Vehicles))
print(issubclass(Car, list))
print(issubclass(Car, Car))
print(issubclass(Car, (list, Vehicles)))



class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()



class Animal:
 
    def __init__(self, age):
        self.__age = age
 
    def setage(self, age):
        self.__age = age
  
    def getage(self):
        return self.__age
 
 
    def __add__(self, predict):
        return Animal( self.__age + predict.__age )
 
    def __gt__(self, predict):
        return self.__age > predict.__age
 
    def __lt__(self, predict):
        return self.__age < predict.__age
 
    def __str__(self):
        return "Combined age of the two animals " + str(self.__age)
 
c1 = Animal(5)
print(c1.getage())
 
c2 = Animal(6)
print(c2.getage())
 
c3 = c1 + c2
print(c3.getage())
 
print( c3 > c2) 
 
print( c1 < c2) 
 
print(c3) 

import pygame  
pygame.init()  
grey = (58,58,58)  

# Clock
clock = pygame.time.Clock()
  
display_surface = pygame.display.set_mode((500, 500))  
  
# set the pygame window name   
pygame.display.set_caption('My First Game Screen')  
  
image = pygame.image.load('Pokemon.jpg')  

# Set the size for the image
DEFAULT_IMAGE_SIZE = (300,300)
  
# Scale the image to your needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

# Set a default position
DEFAULT_IMAGE_POSITION = (100,100)

# infinite loop   
while True:  
	display_surface.fill(grey)  
	display_surface.blit(image, DEFAULT_IMAGE_POSITION)  

	for event in pygame.event.get():  
		if event.type == pygame.QUIT:  
			pygame.quit()  
			# quit the program.   
			quit()  
		
	# Part of event loop
	pygame.display.flip()
	clock.tick(30)



import pygame  
pygame.init()  
screen = pygame.display.set_mode((640, 480))  
done = False  
  
#load the fonts  
font = pygame.font.SysFont("Times new Roman", 36)  
# Render the text in new surface  
text = font.render("My first Game Screen", True, (158, 16, 16))  

while not done:  

	for event in pygame.event.get():  
		if event.type == pygame.QUIT:  
			done = True  

	screen.fill((255, 255, 255))  

	#We will discuss blit() in the next topic  
	screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))  
	pygame.draw.rect(screen, (28,171,226), pygame.Rect(30, 30, 60, 60))
	pygame.display.flip()  



# Import necessary libraries
from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

# Add widgets
# Add Label 
lbl = Label(text="Let's Multiply Two Numbers", fg="white", bg="#072F5F", height=1, width=300)

# Add Label for getting name as input from user
# Use Entry Widget to create a text box for user to enter details
n1_lbl = Label(text="Enter Number 1", bg="#3895D3")
n1_entry = Entry()

n2_lbl = Label(text="Enter Number 2", bg="#3895D3")
n2_entry = Entry()

# Function to calculate the product
def multiply():
	# Fetch the numbers from entry boxes
	n1 = int(n1_entry.get())
	n2 = int(n2_entry.get())
	product = n1*n2

	# Display details in a text box
	# Specify where to add the details inside the text box
	text_box.insert(END, "Here's the final product...\n")
	text_box.insert(END, product)

# Add a Text Widget to display information/messages
text_box = Text(height=3)

# Add button and give value of command as name of the function
# Press button, display function will be called automatically
btn = Button(text="Calculate", command=multiply, height=1, bg="#1261A0", fg='white')

# Organize the widgets
lbl.pack()
n1_lbl.pack()
n1_entry.pack()
n2_lbl.pack()
n2_entry.pack()
btn.pack()
text_box.pack()



# Import necessary libraries
from tkinter import *
import datetime

# Create Window
root = Tk()
root.title('Age Calculator App')
root.geometry('400x400')

# Create a frame to organize elements better
frame = Frame(master=root, height=200, width=360, bg="#FAB072")

# Add widgets
# Add Label 
lbl1 = Label(frame, text = "Name", bg="#CA3433", fg='white', width=12)
lbl2 = Label(frame, text = "Year", bg="#CA3433", fg='white', width=12)
lbl3 = Label(frame, text = "Month", bg="#CA3433", fg='white', width=12)
lbl4 = Label(frame, text = "Date", bg="#CA3433", fg='white', width=12)

# Use Entry Widget to create a text box for user to enter details
name_entry = Entry(frame)
year_entry = Entry(frame)
month_entry = Entry(frame)
date_entry = Entry(frame)

# Function to display message
def calculate():
	name = name_entry.get()
	year = int(year_entry.get())
	today = datetime.date.today()
	age = today.year - year
	greet = "Hey "+name
	message =  "\nYour age is: "+str(age)
	textbox.insert(END, greet)
	textbox.insert(END, message)

# Textbox to display message
textbox = Text(bg="#BEBEBE", fg="black")

# Add Button, when pressed, message will be displayed
btn = Button(text = "Calculate", command=calculate, bg="red")

# Arrange all widgets
frame.place(x=20,y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=50)
year_entry.place(x=150, y=50)
lbl3.place(x=20, y=80)
month_entry.place(x=150, y=80)
lbl4.place(x=20, y=110)
date_entry.place(x=150, y=110)
btn.place(x=140, y=210)
textbox.place(y=250)


# Import Required Library
from tkinter import *
import random

# Create Object
root = Tk()

# Set geometry
root.geometry("300x300")

# Set title
root.title("Rock Paper Scissor Game")
root.attributes('-fullscreen', True)

# Computer Value
computer_value = {
	"0":"Rock",
	"1":"Paper",
	"2":"Scissor"
}

# Reset The Game
def reset_game():
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	l1.config(text = "Player			 ")
	l3.config(text = "Computer")
	l4.config(text = "")

# Disable the Button
def button_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"

# If player selected rock
def isrock():
	c_v = computer_value[str(random.randint(0,2))]
	if c_v == "Rock":
		match_result = "Match Draw"
	elif c_v=="Scissor":
		match_result = "Player Win"
	else:
		match_result = "Computer Win"
	l4.config(text = match_result)
	l1.config(text = "Rock		 ")
	l3.config(text = c_v)
	button_disable()

# If player selected paper
def ispaper():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Paper":
		match_result = "Match Draw"
	elif c_v=="Scissor":
		match_result = "Computer Win"
	else:
		match_result = "Player Win"
	l4.config(text = match_result)
	l1.config(text = "Paper		 ")
	l3.config(text = c_v)
	button_disable()

# If player selected scissor
def isscissor():
	c_v = computer_value[str(random.randint(0,2))]
	if c_v == "Rock":
		match_result = "Computer Win"
	elif c_v == "Scissor":
		match_result = "Match Draw"
	else:
		match_result = "Player Win"
	l4.config(text = match_result)
	l1.config(text = "Scissor		 ")
	l3.config(text = c_v)
	button_disable()

# Add Labels, Frames and Button
Label(root,
	text = "Rock Paper Scissor",
	font = "normal 20 bold",
	fg = "blue").pack(pady = 20)

frame = Frame(root)
frame.pack()

l1 = Label(frame,
		text = "Player			 ",
		font = 10)

l2 = Label(frame,
		text = "VS			 ",
		font = "normal 10 bold")

l3 = Label(frame, text = "Computer", font = 10)

l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()

l4 = Label(root,
		text = "",
		font = "normal 20 bold",
		bg = "white",
		width = 15 ,
		borderwidth = 2,
		relief = "solid")
l4.pack(pady = 20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text = "Rock",
			font = 10, width = 7,
			command = isrock)

b2 = Button(frame1, text = "Paper ",
			font = 10, width = 7,
			command = ispaper)

b3 = Button(frame1, text = "Scissor",
			font = 10, width = 7,
			command = isscissor)

b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(padx = 10)

Button(root, text = "Reset Game",
	font = 10, fg = "red",
	bg = "black", command = reset_game).pack(pady = 20)

# Excecute Tkinter
root.mainloop()



















