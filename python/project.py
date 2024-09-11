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













