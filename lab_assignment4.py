# 1.Function without Parameters:

#Ans.1
def text():
    print("Hello, World!")

text()  
# Output: 
# Hello, World!


# 2.Function with Parameter:
#Ans.2
def text(name):
    print(f"Hello, {name}!")

text("Ankush")  
# Output: 
# Hello, Ankush!


# 3.Function with Default Parameter:
#Ans.3
def text(name="sir"):
    print(f"Hello, {name}!")

text("Aman")  
# Output: 
# Hello, Aman!
text()       
# Output: 
# Hello, sir!



# 4.Function with Return Keyword:
#Ans.4
def add(a, b):
    return a+b

result = add(3, 5)
print(result)  
# Output: 8

# 5.Recursion:
#a) WAP to print factorial value of a given number using recursion.
#Ans
def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Input from the user
number = int(input("Enter a number: "))

# Calculate factorial using the recursive function
result = factorial(number)

# Print the result
print(f"Factorial of {number} is {result}")
 

# Output: 
# Enter a number: 6
# Factorial of 6 is 720


#b) WAP to display Fibonacci series up to 10 iteration using recursion.
def fibonacci_recur(n, a=0, b=1, count=0):
    if count < n:
        print(a, end=" ")
        fibonacci_recur(n, b, a + b, count + 1)

fibonacci_recur(10) 
# Output: 
# 0 1 1 2 3 5 8 13 21 34

