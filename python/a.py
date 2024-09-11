#Print a Sentence 
print("Welcome to the world of programming!")

#Print a Number
print(4)

#Next Line after print
print("Hello Python \n")

#Pass multiple arguments for printing
print("hello",5)

#End argument of Print Statement
print("welcome to ", end= "*")


# Creating different variables
x = 5
y = "John"
print(x)
print(y)

codingal = "codingal"
print(codingal)

# User Input
name = input("enter your name: ")

print("\nHello", name, "\nwelcome to codingal")



import keyword

# print all the Python keywords
print("Python keywords are...\n")
print(keyword.kwlist)



# Let's check the datatype of different values
a = 5
print("type of a: ", type(a))

b=2.5
print("type of b: ", type(b))

c= "coding"
print("type of c: ", type(c))

d= True
print("type of d: ", type(d))



# Assigning Different Variables
name = "Penguin"
age = 15
is_student = True
weight = 38.5

# Printing Different Variables and their Data Type
print("Name :", name)
print("Data Type of Name is", type(name))

print("Age :", age)
print("Data Type of Age is", type(age))

print("is_student :", is_student)
print("Data Type of is_student is", type(is_student))

print("Weight :", weight)
print("Data Type of weight is", type(weight))

# Type casting to convert the datatype of variables
print("\n After Type Casting....")
age = str(age)
print(age)
print("Data Type of age is", type(age))
weight = int(weight)
print(weight)
print("Data Type of Weight is", type(weight))


#input a word
text = str(input("Enter a string: "))

# Reverse String 
# using step value as -1 to iterate in reverse
revText = text[::-1] 
text = revText

print("Reverse of Given String is:")
print(text)


# Take two strings as input from user
print("Enter the First String: ")
strOne = input()

print("Enter the Second String: ")
strTwo = input()

# Concatenate the two strings
# Using Addition Operator
strThree = strOne + strTwo
print("\nConcatenated String: ", strThree)



# Storing Values
tree1 = 98
tree2 = 94
tree3 = 41
tree4 = 95
tree5 = 11

# Finding the total of trees
sum = tree1+tree2+tree3+tree4+tree5
print("the sum of all the 5 trees is: ", sum)

# Finding the average of trees
average = sum/5
print("the average of all the tree is :", average)


# Taking total amount as input from user
Amount =int(input("Please Enter Amount for Withdraw :"))

# Calculating the number of notes of different denominations
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10


print( "notes of 100 rupee" , note_1)
print("notes of 50 rupee" , note_2)
print("notes of 10 rupee" , note_3)


# take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

# Let's calculate the percentage of marks
sum = math+english+science+hindi
print("sun of math,english,science and hindi")

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)


print("Enter the Number of Days: ")
num = int(input())

year = int(num/365)
week = int((num%365)/7)
days = int((num%365)%7)

print("Total Number of Year(s): ")
print(year)
print("Total Number of Week(s):")
print(week)
print("Total Number of Day(s):")
print(days)


# quiz.py

answer = input("When was the first known use of the word 'quiz'? ")
if answer == "1781":
    print("Correct!")
else:
    print(f"The answer is '1781', not {answer!r}")

answer = input("Which built-in function can get information from the user? ")
if answer == "input":
    print("Correct!")
else:
    print(f"The answer is 'input', not {answer!r}")

n=int(input("Enter the number:"))
if( n%2==0 ):
  print("The number is even")
else:
  print("The number is odd")


a = 23
b = 24
c = 22


if a > b or a < c:
    print("I am using or operator")
elif a < b and a > c:
    print("I am using and operator")



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



print("Enter the Number of Days: ")
num = int(input())

year = int(num/365)
week = int((num%365)/7)
days = int((num%365)%7)

print("Total Number of Year(s): ")
print(year)
print("Total Number of Week(s):")
print(week)
print("Total Number of Day(s):")
print(days)

#below statement takes input from user
number=int(input("Enter a number   "))

#below statement is conditional and check for the condition to be true or false
if number>0:
  print(number,"is a positive number")
elif number==0:
  print(number,"is a neutral number")
else:
  print("Negative number")
a=True
print(not a)
















