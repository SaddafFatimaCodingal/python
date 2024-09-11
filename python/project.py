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

























