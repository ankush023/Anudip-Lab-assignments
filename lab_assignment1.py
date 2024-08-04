
#Q.1 print helloworld.

#Ans.1 
print("helloworld")

#Output:
#helloworld

#Q.2 describe local variable and global variable code.

#Ans.2
#local variable: Local variables are defined within a function and can only be accessed within that function.Let see an example with the help of code.
def my_function():
    #local variable
    y=10
    print("Local variable y inside function:",y)
    
my_function()

#Global variable: Global variables are defined outside of all functions and are accessible throughout the entire program,including inside functions(unless shadowed by local variables of the same name).Let see an example o global variable with the help of code.

#Global variable
x=100
def print_global():
    print("Global variable x:",x)
    
print_global()

#Output:
#Local variable y inside function: 10
#Global variable x: 100


#Q.3 Write a code that describe Indentation error.

#Ans.3 Indentation errors in Python occure when the code blocks are not properly indented.Python uses indentation to define the scope of loops, functions, conditionals, and other code blocks. Here's an example code that will raise an indentation error.Now, see a code that describe indentation error.

def text_function():
    x=10
    if x>5:
    print("x is greater than 5") #This line is not properly indented

text_function()

def text_function():
    x=10
    if x>5:
        print("x is greater than 5") #properly indented

text_function()


#Q.4 write a code that describe local and global variable with same name

#Ans.4 

#Global variable
x=10

def demo_example():
    #Local variable with the same name as the global variable.
    x=5
    print("Inside function,local variable x:",x) #This will print the local var x
    
#Calling the function
demo_example()

#Printing the global variable
print("Outside function,gloabl variable x:",x) 

#Output:
# Inside function,local variable x: 5   
# Outside function,gloabl variable x: 10


#Q.5 Write a code for string, int and float input.

#Ans.5
#string input
string_input = input("Enter a string: ")

#integer input
int_input = int(input("Enter the integer: "))

#float input
float_input = float(input("Enter the float no: "))

#printing all the inputs
print("String no is:",string_input)
print("Integer no is:",int_input)
print("Float no is:",float_input)

#Output:
# Enter a string: Ankush
# Enter the integer: 12
# Enter the float no: 23
# String no is: Ankush
# Integer no is: 12   
# Float no is: 23.0   
