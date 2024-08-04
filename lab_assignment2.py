                                                PYTHON PROGRAMMING
                                                 Lab Assignment-2
                                                    Operators

# Q.1 Write a program for arithmatic operators.

#Ans.1
a = 5
b = 3

addition = a + b  #This perform addition of two number
subtraction = a - b #This perform substraction of two number
multiplication = a * b #This perform multiplication of two number
division = a / b  #This perform division of two number
floor_division = a // b  #This perform floor division of two number
modulus = a % b  #This perform modulus of two number
exponentiation = a ** b #This perform exponentiation of two number

#Printing all the inputs.
print("Addition:", addition)             
print("Subtraction:", subtraction)       
print("Multiplication:", multiplication) 
print("Division:", division)             
print("Floor Division:", floor_division) 
print("Modulus:", modulus)               
print("Exponentiation:", exponentiation)

#Output:
# Addition: 8
# Subtraction: 2    
# Multiplication: 15
# Division: 1.6666666666666667
# Floor Division: 1
# Modulus: 2
# Exponentiation: 125

# Q.2 Write a program for assignment operators.

#Ans.2
# Initialize a variable
a = 10
print(f"Initial value of a: {a}")

# Simple assignment
a = 5
print(f"a = 5, a: {a}")

# Addition assignment
a += 3  # Equivalent to a = a + 3
print(f"After a += 3, a: {a}")

# Subtraction assignment
a -= 2  # Equivalent to a = a - 2
print(f"After a -= 2, a: {a}")

# Multiplication assignment
a *= 4  # Equivalent to a = a * 4
print(f"After a *= 4, a: {a}")

# Division assignment
a /= 2  # Equivalent to a = a / 2
print(f"After a /= 2, a: {a}")

# Floor division assignment
a //= 3  # Equivalent to a = a // 3
print(f"After a //= 3, a: {a}")

# Modulus assignment
a %= 3  # Equivalent to a = a % 3
print(f"After a %= 3, a: {a}")

# Exponentiation assignment
a **= 2  # Equivalent to a = a ** 2
print(f"After a **= 2, a: {a}")

# Bitwise AND assignment
a = 15 #In binary: 1111
a &= 7 # 7 in binary: 0111 
print(f"After a &= 7, a: {a}")

# Bitwise OR assignment
a |= 2  # Equivalent to a = a | 2
print(f"After a |= 2, a: {a}")

# Bitwise XOR assignment
a ^= 3  # Equivalent to a = a ^ 3
print(f"After a ^= 3, a: {a}")

# Bitwise right shift assignment
a >>= 1  # Equivalent to a = a >> 1
print(f"After a >>= 1, a: {a}")

# Bitwise left shift assignment
a <<= 2  # Equivalent to a = a << 2
print(f"After a <<= 2, a: {a}")

#Output:
# Addition: 8
# Subtraction: 2
# Multiplication: 15
# Division: 1.6666666666666667     
# Floor Division: 1
# Modulus: 2
# Exponentiation: 125
# Initial value of a: 10
# a = 5, a: 5
# After a += 3, a: 8
# After a -= 2, a: 6
# After a *= 4, a: 24
# After a /= 2, a: 12.0
# After a //= 3, a: 4.0
# After a %= 3, a: 1.0
# After a **= 2, a: 1.0
# After a &= 7, a: 7
# After a |= 2, a: 7
# After a ^= 3, a: 4
# After a >>= 1, a: 2
# After a <<= 2, a: 8

# Q.3Write a program for Bitwise operators.

#Ans.3
# Initialize two variables
a = 11  # Binary no is: 1011
b = 5  # Binary no is: 0101


# Bitwise AND
demo_and = a & b  # Binary: 111100 & 001101 = 001100
print(f"Bitwise AND (a & b): {demo_and}")

# Bitwise OR
demo_or = a | b  # Binary: 111100 | 001101 = 111101
print(f"Bitwise OR (a | b): {demo_or}")

# Bitwise XOR
demo_xor = a ^ b  # Binary: 111100 ^ 001101 = 110001
print(f"Bitwise XOR (a ^ b): {demo_xor}")

# Bitwise NOT
demo_not = ~a  # Binary: ~111100 = -111101 (in two's complement)
print(f"Bitwise NOT (~a): {demo_not} ")

# Bitwise left shift
shift_left = a << 2  # Binary: 111100 << 2 = 11110000
print(f"Bitwise left shift (a << 2): {shift_left}")

# Bitwise right shift
shift_right = a >> 2  # Binary: 111100 >> 2 = 001111
print(f"Bitwise right shift (a >> 2): {shift_right}")

#Output:
# Bitwise AND (a & b): 1
# Bitwise OR (a | b): 15
# Bitwise XOR (a ^ b): 14
# Bitwise NOT (~a): -12
# Bitwise left shift (a << 2): 44
# Bitwise right shift (a >> 2): 2


# Q.4 Write a program to calculate greatest of three numbers.

#Ans.4
# Function to find the greatest of three numbers
def my_function(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Input three numbers from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Find the greatest number
greatest = my_function(a,b,c)

# Output the result
print(f"The greatest of the three numbers is: {greatest}")

# Checking conditions

if a == b == c:
    print("All three numbers are equal.")
elif a == b or a == c or b == c:
    print("Two of the numbers are equal.")
else:
    print("All the numbers are different.")

#Output:
# Enter the first number: 6
# Enter the second number: 5
# Enter the third number: 4
# The greatest of the three numbers is: 6.0
# All the numbers are different.
