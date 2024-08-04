# 1.Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

#Ans.2

num = int(input("Enter any number: "))
if num == 0:
    print("The number is zero")
elif num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Output1:
# Enter any number: 0
# The number is zero

#Output2:
# Enter any number: 56
# The number is even

#Output3:
# Enter any number: 33
# The number is odd
    


# 2.Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

#Ans.2
age = int(input("Enter age of a person: "))
if age < 0:
    print("Invalid age entered.")
elif age < 18:
    print("Person is not eligible to vote")
else:
    print("Person is eligible to vote")
    
#Output1:
# Enter age of a person: -2
# Invalid age entered.

#Output2:
# Enter age of a person: 15
# Person is not eligible to vote

#Output3:
# Enter age of a person: 19
# Person is eligible to vote


# 3. Write a Python program that determines if a given year is a leap year or not.

#Ans.3
year = int(input("Enter a year to be checked: "))
if year % 4 != 0:
    print("Not a leap year.")
elif year % 100 != 0:
    print("Leap year.")
elif year % 400 != 0:
    print("Not a leap year.")
else:
    print("Leap year.")
    
#Output1:
# Enter a year to be checked: 2023
# Not a leap year.

#Output2:
# Enter a year to be checked: 2024
# Leap year.

# 4.      Create a Python program that checks if a user-given number is positive, negative, or zero.

#Ans.4

num = int(input("Enter a number: "))

# if num > 0 :
#     print("No. is positive.")
# elif num = 0:
#     print("No. is zero.")
# else num < 0:
#     print("No. is negative.")
if num == 0:
    print("The number is zero.")
elif num > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

#Output1:
# Enter a number: 0
# The number is zero.

#Output2:
# Enter a number: 88
# The number is positive.

#Output3:
# Enter a number: -5
# The number is negative.


# 5.Write a Python program that determines the largest of three numbers entered by the user.

#Ans.5
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if num1 >= num2 and num1 >= num3:
   print("Largest no is :",num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest no is :",num2)
else:
    print("Largest no is :",num3)
    
#Output:
# Enter a number: 34
# Enter a number: 678
# Enter a number: 67