# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 02:46:47 2019

@author: sri
"""

# =============================================================================
# # =============================================================================
# Arithmetic Operators :
# a) +    Addition: adds two operands    x + y
# b) -    Subtraction: subtracts two operands    x - y
# c) *    Multiplication: multiplies two operands    x * y
# d) /    Division (float): divides the first operand by the second    x / y
# e) //    Division (floor): divides the first operand by the second    x // y
# f) %    Modulus: returns the remainder when first operand is divided by the second    x % y
# # =============================================================================
# =============================================================================
print("Arithmetic Operators : \n  ")
a = 10
b = 5
c = a+b
print("Addition of a+b is:" ,c)

d = a-b
print("Subtraction of a-b is:" ,d)

e = a*b
print("Multiplication of a+b is:" ,e)

f = a/b
print("Division of a+b is:" ,f)

g = a//b
print("Division (Floor) of a+b is:" ,g)

h = a%b
print("Modulus of a+b is:" ,h)



# =============================================================================
# # =============================================================================
# Relational Operators:
# a)>    Greater than: True if left operand is greater than the right    x > y
# b)<    Less than: True if left operand is less than the right    x < y
# c)==    Equal to: True if both operands are equal    x == y
# d)  !=    Not equal to - True if operands are not equal    x != y
# e) >=    Greater than or equal to: True if left operand is greater than or equal to the right    x >= y
# f) <=    Less than or equal to: True if left operand is less than or equal to the right    x <= y
# # =============================================================================
# =============================================================================

print("Relational Operators : \n ")
if a>b:
    print ("a is Greater than b:",a)
else:
    print(False)


if a<b:
    print (a,b)
else:
    print("b is less than a:",b)


i = 1
j = 1
if i==j:
    print(True)
else:
    print(False)

k = 2
if i!=k:
    print(True)
else:
    print(False)

l = 13
m = 12
if l>=m:
    print(True)
else:
    print(False)

if m<=l:
    print(True)
else:
    print(False)


# =============================================================================
# =============================================================================
# Logical Operators:
# a)and    Logical AND: True if both the operands are true    x and y
# b) or    Logical OR: True if either of the operands is true    x or y
# c) not    Logical NOT: True if operand is false    not x
# =============================================================================
# =============================================================================
print("Logical Operators : \n  ")

a = True
b = True
print (a and b)

a = True
b = False
print(a or b)

a = True
b = False
print( not b)


# =============================================================================
# =============================================================================
# Bitwise Operators:
# a) &    Bitwise AND    x & y
# b)|    Bitwise OR    x | y
# c)~    Bitwise NOT    ~x
# d) ^    Bitwise XOR    x ^ y
# e) >>    Bitwise right shift    x>>
# f) <<    Bitwise left shift    x<<
# =============================================================================
# =============================================================================
print("Bitwise Operators : \n  ")

x = 5     # 000 101
y = 7     # 000 111
print("Bitwise AND of x and y is  :",x & y)   #100

print("Bitwise OR of x and y is  :",x | y)  # 111

print("Bitwise NOT of x is  :", ~ x ) #111 010

print( "Bitwise XOR of x and y is  :",x ^ y ) #000 010

print( "Bitwise right shift of x is  :",x >> 0)

print( "Bitwise left shift of x is  :",x << 1)



# # =============================================================================
# =============================================================================
# Assignment Operators:
# a) =    Assign value of right side of expression to left side operand    x = y + z
# b) +=    Add AND: Add right side operand with left side operand and then assign to left operand    a+=b     a=a + b
# c)-=    Subtract AND: Subtract right operand from left operand and then assign to left operand    a-=b       a=a-b
# d) *=    Multiply AND: Multiply right operand with left operand and then assign to left operand    a*=b       a=a*b
# e) /=    Divide AND: Divide left operand with right operand and then assign to left operand    a/=b         a=a/b
# f) %=    Modulus AND: Takes modulus using left and right operands and assign result to left operand    a%=b   a= a % b
# g) //=    Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand    
# h)  a//=b             a=a//b
# i) **=    Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand    a**=b     
# j)      a=a**b
# k) &=    Performs Bitwise AND on operands and assign value to left operand    a&=b     a=a&b
# l) |=    Performs Bitwise OR on operands and assign value to left operand    a|=b         a=a|b
# m) ^=    Performs Bitwise xOR on operands and assign value to left operand    a^=b       a=a^b
# n) >>=    Performs Bitwise right shift on operands and assign value to left operand    a>>=b     a=a>>b
# o) <<=    Performs Bitwise left shift on operands and assign value to left operand    a <<= b   a= a << b
# =============================================================================
# # =============================================================================

print(" Assignment Operators :  \n")
a=5
b=4
a += c
print("The value of Add AND (+=) is :",a)

a =5
b= 2
a -= b
print("The value of Subtract AND (-+) is :",a)

a =5
b= 2
a *= b
print("The value of Multiply AND (*=) is :",a)

a =5
b= 2
a /= b
print("The value of Divide AND (/=) is :" ,a)

a =5
b= 2
a %= b
print("The value of Modulus AND (%=) is :",a)

a =5
b= 2
a //= b
print("The value of Divide (Floor) (//=) is",a)

a =5
b= 2
a **= b
print("The value of Exponent AND (**=) is",a)

a =5
b= 2
a &= b
print("The value of Bitwise AND  (&=) is" ,a)

a =5
b= 2
a |= b
print("The value of Bitwise OR (|=) is", a)

a =5
b= 2
a^=b
print("The value of Bitwise XOR (^=) is", a)

a =5
b= 2
a<<=b
print("The value of Bitwise Right Shift (<<=) is", a)

a =5
b= 2
a>>=b
print("The value of Bitwise Left Shift (>>=) is" ,a)
# =============================================================================
# =============================================================================
# Special Operators: identity and Membership
# i)Identity operators :
# is and is not are the identity operators both are used to check if 2 values are located on the same part of  the memory. Two variables that are equal does not imply that they are identical
#  is          True if the operands are identical 
#    is not      True if the operands are not identical 
# =============================================================================
# =============================================================================
print("Identity Operators : \n")
a1 = 3
b1 = 3
a2 = 'DataScience'
b2 = 'DataScience'
a3 = [1,2,3] 
b3 = [1,2,3] 
print(a1 is not b1) 
print(a2 is b2) 
 # Output is False, since lists are mutable. 
print(a3 is b3) 

# =============================================================================
# Membership Operator:
# - in and not in are the membership operators; used to test whether a value or variable is in a sequence.
#     in            True if value is found in the sequence
#     not in        True if value is not found in the sequence
# =============================================================================
print("Membership Operator : \n ")

x = 'Data Science'
y = {3:'a',4:'b'} 
  
print('D' in x) 
  
print('data' not in x) 
  
print('Data' not in x) 
  
print(3 in y) 
  
print('b' in y)

# =============================================================================
# Control Flow Statements :
#     Conditions : if,elif,elif ladder and else
#     Iterations : while,for,break and continue
# =============================================================================
print("Control Flow Statements : \n" )
a= 4
b =5
if a>b:
    print('A is bigger',a)
else:
    print('B is bigger',b ,"\n")
print("if elif else example : \n")    
a=5
b=7
c=9
if a>b and a>c:
    print('A is Bigger',a)
elif b>c:
    print('B is Bigger',b)
else:
    print('C is Bigger',c,"\n")

print("elif ladder : \n")
x = -15

if x == 0:
    print(x, "is zero")
elif x > 0:
    print(x, "is positive")
elif x < 0:
    print(x, "is negative")
else:
    print(x, "is unlike anything I've ever seen... \n")
print("While Loop : \n")    
n=1
while True:
  print (n)
  n+=1
  if n==5:
    break
print("After Break \n")


print("For Loop Example: \n")
for str in "Python":
    if str == "t":
        break
    print(str)
print("Exit from loop \n")

print("Continue keyword example using for while : \n")
n=0
while n < 5:
  n+=1
  if n==3:
    continue
print (n, "\n")

print("Continue keyword example using for loop: \n")
n=0
for n in range(5):
  n+=1
  if n==3:
    continue
  print(n)
print("Loop Over \n")

# For loop example
print("For Loop : \n")
word = "Android"
for letter in word:
    print(letter)
# While loop
print("\n While Loop : \n" )
a = 0
while a < 10:
   a = a + 1
   print(a)