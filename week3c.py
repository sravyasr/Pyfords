# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:31:04 2019

@author: sri
"""

#Python programs that uses the dictionaries, tuples and other data
#structures
dict_one = {'name':'Jack', 'age': 26}

# Output: Jack
print(dict_one['name'])

# Output: 26
print(dict_one.get('age'))
dict_one['address'] = 'Downtown'  

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(dict_one)

squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

# remove a particular item
# Output: 16
print(squares.pop(4))  

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item
# Output: (1, 1)
print(squares.popitem())

# Output: {2: 4, 3: 9, 5: 25}
print(squares)

# Output: {2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

marks = {}.fromkeys(['Math','English','Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)

for item in marks.items():
    print(item)

# Output: ['English', 'Math', 'Science']
list(sorted(marks.keys()))

squares = {x: x*x for x in range(6)}

# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)

squares = {}
for x in range(6):
   squares[x] = x*x
   
   
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: True
print(1 in squares)

# Output: True
print(2 not in squares)

# membership tests for key only not value
# Output: False
print(49 in squares)

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])
    
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: 5
print(len(squares))

# Output: [1, 3, 5, 7, 9]
print(sorted(squares))

print("Tuples:")

# Empty tuple
a_tuple = ()
print(a_tuple)  # Output: ()

# Tuple having integers
a_tuple = (1, 2, 3)
print(a_tuple)  # Output: (1, 2, 3) 

# tuple with mixed datatypes
my_tuple = (1, "Welcome", 4.9)
print(my_tuple)  # Output: (1, "Hello", 3.4)  

# nested tuple
a_tuple = ("Data", [8, 4, 6], (1, 2, 3))

# Output: ("mouse", [8, 4, 6], (1, 2, 3)) 
print(a_tuple)

a_tuple = 5, 9.8, "science"
print(a_tuple)   # Output: 3, 4.6, "dog" 

# tuple unpacking is also possible
a, b, c = a_tuple

print(a)      # 3
print(b)      # 4.6 
print(c)      # dog 

a_tuple = ("hello")
print(type(a_tuple))  # <class 'str'>

# Creating a tuple having one element
a_tuple = ("hello",)  
print(type(a_tuple))  # <class 'tuple'>

a_tuple = ('T','e','c','h','n','o','l','o','g','y')

print(a_tuple[0])   # 'p' 
print(a_tuple[5])   # 't'

# IndexError: list index out of range
# print(my_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple[2.0]

# nested tuple
n_tuple = ("Data", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4

print(a_tuple[-1])

print(a_tuple[1:4])

# elements beginning to 2nd
# Output: ('p', 'r')
print(a_tuple[:-7])

# elements 8th to end
# Output: ('i', 'z')
print(a_tuple[7:])

# elements beginning to end
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(a_tuple[:])

m_tuple = ('a','n','d','r','o','i','d')

print(m_tuple.count('a'))  # Output: 2
print(m_tuple.index('d'))  # Output: 3

print("List :")

b_list = []
b_list = ['n','u','t','e','r','a','l']
# Output: p
print(b_list[0])
# Output: o
print(b_list[2])
# Output: e
print(b_list[4])
# Error! Only integer can be used for indexing
# my_list[4.0]
# Nested List
n_list = ["Amazing", [2,0,1,5]]
# Nested indexing
# Output: a
print(n_list[0][1])    
# Output: 5
print(n_list[1][3])

my_list = ['p','r','o','b','e']
# Output: p
print(my_list[0])
# Output: o
print(my_list[2])
# Output: e
print(my_list[4])
# Error! Only integer can be used for indexing
# my_list[4.0]
# Nested List
n_list = ["Happy", [2,0,1,5]]
# Nested indexing
# Output: a
print(n_list[0][1])    
# Output: 5
print(n_list[1][3])

print(b_list[2:5])

c_list = ['p','r','o','b','l','e','m']
# delete one item
del c_list[2]
# Output: ['p', 'r', 'b', 'l', 'e', 'm']     
print(c_list)
# delete multiple items
del c_list[1:5]  
# Output: ['p', 'm']
print(c_list)

k_list = [3, 8, 1, 6, 0, 8, 4]
# Output: 1
print(k_list.index(8))
# Output: 2
print(k_list.count(8))
k_list.sort()
# Output: [0, 1, 3, 4, 6, 8, 8]
print(k_list)
k_list.reverse()
# Output: [8, 8, 6, 4, 3, 1, 0]
print(k_list)

pow2 = [2 ** x for x in range(10)]
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)

for c_list in ['p','a','m']:
    print("I like",c_list)