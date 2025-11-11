#!/usr/bin/env python
# coding: utf-8

# In[1]:


.Part 1: Variables and Memory Allocation
    
Exercise 1.1: Memory Exploration
Write a program that demonstrates how variables and memory allocation work in Python. Your
program should:
1. Create variables of different types (int, float, string, list, tuple).
2. Print the ID (memory address) of each variable using the id() function.
3. Create a second variable that references the same object as one of your first variables.
4. Modify the original variable and observe what happens to the second one (for both
mutable and immutable types).
5. Include comments explaining the behavior you observe.

Exercise 1.2: Variable Scope Investigation
Create a function that demonstrates variable scope in Python:
1. Define global variables outside the function.
2. Define local variables inside the function with the same names.
3. Try to modify a global variable both with and without the global keyword.
4. Print the IDs of all variables before and after modifications
5. Explain what happens and why in your comments.

Part 2: Data Types and Type Conversion
Exercise 2.1: Type Exploration
Create a program that:
1. Creates at least one variable of each of these types: int, float, complex, bool, str, and
None.
2. Uses the type() function to verify the type of each variable.
3. Uses isinstance() to check if variables are of specific types.
4. Demonstrates at least three examples where Python automatically converts types in
expressions.
5. Includes comments documenting your observations about type behavior.

Exercise 2.2: Type Conversion Challenge
Write a function that:
1. Takes a string input containing a mixture of numbers and text (e.g., "I am 25 years old
and my height is 5.9 feet").
2. Extracts all numbers from the string and converts them to their appropriate numeric types
(int or float).
3. Returns a tuple containing two lists: one with all integers found and one with all floats
found.
4. Handles potential conversion errors gracefully.
Part 3: Number Systems and Representation
                                                                  
Exercise 3.1: Base Converter
Create a set of functions that:
1. Converts decimal integers to binary, octal, and hexadecimal striings without using built-in
functions like bin(), oct(), or hex().
2. Converts binary, octal, and hexadecimal strings to decimal integers without using int(x,
base).
3. Demonstrates your functions with at least five different numbers.
4. Verifies your results by comparing with Python's built-in conversion functions.
Part 4: Floating-Point Precision
                                                                  
Exercise 4.1: Precision Problems
Write a program that demonstrates floating-point precision issues:
1. Create at least five examples where floating-point arithmetic gives unexpected results.
2. For each example, explain why the result occurs.
3. Implement a solution to each problem using at least two different approaches (rounding,
epsilon comparison, Decimal, Fraction, etc.).
4. Compare the accuracy and performance of each solution.
Part 5: Deep Dive Modules
                                                                  
Exercise 5.1: Math Module Explorer
Write a program that explores the capabilities of the math module:
1. Use at least 10 different functions from the math module.
2. Create practical examples for each function.
3. Create a function that calculates the roots of a quadratic equation using math functions.
4. Create a function that converts between different angle units (degrees, radians) using 
math functions.
5. Include comments explaining each function and its application.                                                                 


# In[1]:


"""## Exercise 1.1: Memory Exploration ,Print the ID (memory address) of each variable using the id() function.
Write a program that demonstrates how variables and memory allocation work in Python. Your
program should"""

a= 2
b= 3
c= 7
print("meomory allocation","a",id(a))
print("meomory allocation","b",id(b))
print("meomory allocation","c",id(c))


# In[2]:


# Create a second variable that references the same object as one of your first variables.
a= 3
b= 5
a=b
print(a)


# In[4]:


'''4. Modify the original variable and observe what happens to the second one (for both
mutable and immutable types) ''' 
 
a= [5,6,7,8] 
a[0] =99
b=(3,7,9,1)
b[0] =99
print(a)
print(b)



# In[ ]:


Exercise 1.2: Variable Scope Investigation
Create a function that demonstrates variable scope in Python:
1. Define global variables outside the function.
2. Define local variables inside the function with the same names.
3. Try to modify a global variable both with and without the global keyword.
4. Print the IDs of all variables before and after modifications
5. Explain what happens and why in your comments.


# In[ ]:


"1. Define global variables outside the function."
"
# Global variable
x = 10  

def show():
    print("Inside function:", x)   # Can access global variable

show()
print("Outside function:", x)


# In[ ]:


x=10
def show():
    print("inside function:",x)
show()
print("outside function :",x)


# # will do later variable global

# In[ ]:


Exercise 2.2: Type Conversion Challenge
Write a function that:
1. Takes a string input containing a mixture of numbers and text (e.g., "I am 25 years old
and my height is 5.9 feet").
2. Extracts all numbers from the string and converts them to their appropriate numeric types
(int or float).
3. Returns a tuple containing two lists: one with all integers found and one with all floats
found.
4. Handles potential conversion errors gracefully.
Part 3: Number Systems and Representation


# In[13]:


""""1. Creates at least one variable of each of these types: int, float, complex, bool, str, and
None."""
a= "mangka"
print(a)
b=1+3j
print(b)
c= True
print(c)
d= None
print(d)


# In[14]:


".2 . Uses the type() function to verify the type of each variable."
a= "mangka"
print(type(a))
b=1+3j
print(type(b))
c= True
print(type(c))
d= None
print(type())


# In[8]:


""""3. Demonstrates at least three examples where Python automatically converts types in
expressions."""
a=3
b=4.3
c=a+b
print("\nAutomatic type conversions:")
print(c,type(c))

4. Includes comments documenting your observations about type behavior.
Both a and b are integers, so adding them (a + b) does not trigger any type conversion.

To demonstrate automatic type conversion, you need expressions where Python mixes 
 different types, e.g., int + float, float + bool, or int + complex.
    
✅ Key points:

Python automatically converts smaller types to larger types to avoid data loss.

bool is treated as a subclass of int (True=1, False=0).

Mixing int with float gives a float.
# 
#  Exercise 2.2: Type Conversion Challenge
# Write a function that:
# 1. Takes a string input containing a mixture of numbers and text (e.g., "I am 25 years old
# and my height is 5.9 feet").
# 2. Extracts all numbers from the string and converts them to their appropriate numeric types
# (int or float).
# 3. Returns a tuple containing two lists: one with all integers found and one with all floats
# found.
# 4. Handles potential conversion errors gracefully.
# Part 3: Number Systems and Representation

# # """Exercise 2.2: Type Conversion Challenge
# Write a function that:
# 1. Takes a string input containing a mixture of numbers and text (e.g., "I am 25 years old
# and my height is 5.9 feet")."""
# 
# a="I am 25 years old and my height is 5.9 feet"
# 

# In[ ]:





# # ."2. Extracts all numbers from the string and converts them to their appropriate numeric types(int or float)."
# 

# # 3. Returns a tuple containing two lists: one with all integers found and one with all floats
# found.
# 4. Handles potential conversion errors gracefully.
# Part 3: Number Systems and Representation

# In[ ]:


Exercise 3.1: Base Converter
Create a set of functions that:
1. Converts decimal integers to binary, octal, and hexadecimal striings without using built-in
functions like bin(), oct(), or hex().
2. Converts binary, octal, and hexadecimal strings to decimal integers without using int(x,
base).
3. Demonstrates your functions with at least five different numbers.
4. Verifies your results by comparing with Python's built-in conversion functions.
Part 4: Floating-Point Precision


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


Exercise 4.1: Precision Problems
Write a program that demonstrates floating-point precision issues:
1. Create at least five examples where floating-point arithmetic gives unexpected results.
2. For each example, explain why the result occurs.
3. Implement a solution to each problem using at least two different approaches (rounding,
epsilon comparison, Decimal, Fraction, etc.).
4. Compare the accuracy and performance of each solution.
Part 5: Deep Dive Modules
                                                                  


# In[ ]:





# In[ ]:





# In[ ]:


Exercise 5.1: Math Module Explorer
Write a program that explores the capabilities of the math module:
1. Use at least 10 different functions from the math module.
2. Create practical examples for each function.
3. Create a function that calculates the roots of a quadratic equation using math functions.
4. Create a function that converts between different angle units (degrees, radians) using 
math functions.
5. Include comments explaining each function and its application.                                                                 


# In[3]:


"1. Use at least 10 different functions from the math module."
import math

print(math.sqrt(16))       # 4.0
print(math.factorial(5))   # 120
print(math.pow(2, 3))      # 8.0
print(math.sin(math.pi/2)) # 1.0
print(math.cos(0))         # 1.0
print(math.tan(math.pi/4)) # 1.0
print(math.log(100,10))    # 2.0
print(math.exp(2))         # e^2
print(math.ceil(2.3))      # 3
print(math.floor(2.7))     # 2

 


# In[4]:


print(math.sqrt(16))  


# In[5]:


print(math.factorial(4))


# In[6]:


print(math.ceil(2.3))      # 3


# In[7]:


print(math.floor(2.7))


# In[ ]:


Exercise 5.1: Math Module Explorer
Write a program that explores the capabilities of the math module:
1. Use at least 10 di


# In[ ]:


math import 
a.squrt


# In[ ]:


📘 Part 1: Variables and Memory Allocation
Exercise 1.1: Memory Exploration

Instruction meaning word by word:

"Write a program" → You have to code in Python.

"demonstrates how variables and memory allocation work in Python" → Show how Python stores variables in memory and how references behave.

Step-by-step tasks:

"Create variables of different types (int, float, string, list, tuple)."
→ Make one variable each, e.g. x=5 (int), y=3.2 (float), z="hello" (string), a=[1,2,3] (list), b=(1,2,3) (tuple).

"Print the ID (memory address) of each variable using the id() function."
→ Use print(id(x)) etc. This shows where Python stores the object in memory.

"Create a second variable that references the same object as one of your first variables."
→ Example: c = x. Now c points to the same place in memory as x.

"Modify the original variable and observe what happens to the second one (for both mutable and immutable types)."
→ Immutable = numbers, strings, tuples → they create a new object in memory when changed.
→ Mutable = lists, dictionaries → they change in place, so second variable also reflects changes.

"Include comments explaining the behavior you observe."
→ Use # in code to explain what you see happening.

Exercise 1.2: Variable Scope Investigation

Instruction meaning word by word:

"Create a function" → Define a function with def.

"demonstrates variable scope" → Show difference between local (inside function) and global (outside function) variables.

Step-by-step tasks:

"Define global variables outside the function."
→ Example: x = 10.

"Define local variables inside the function with the same names."
→ Example: inside function: x = 20.

"Try to modify a global variable both with and without the global keyword."
→ Without global: Python treats it as local and won’t change the global one.
→ With global x: Python changes the global variable.

"Print the IDs of all variables before and after modifications."
→ Use id(x) before and after to see if memory reference changes.

"Explain what happens and why in your comments."
→ Add # comments like # local x shadowed global x.

📘 Part 2: Data Types and Type Conversion
Exercise 2.1: Type Exploration

"Creates at least one variable of each of these types: int, float, complex, bool, str, and None."
→ Example: a=5, b=2.5, c=3+4j, d=True, e="hello", f=None.

"Uses the type() function to verify the type of each variable."
→ print(type(a)) → <class 'int'>.

"Uses isinstance() to check if variables are of specific types."
→ isinstance(a,int) → True.

"Demonstrates at least three examples where Python automatically converts types in expressions."
→ Example: 5 + 2.5 → converts int to float → 7.5.

"Includes comments documenting your observations about type behavior."
→ Example: # int+float → float (widening conversion).

Exercise 2.2: Type Conversion Challenge

"Takes a string input containing a mixture of numbers and text"
→ Example input: "I am 25 years old and my height is 5.9 feet".

"Extracts all numbers from the string and converts them to their appropriate numeric types (int or float)."
→ 25 → int, 5.9 → float.

"Returns a tuple containing two lists: one with all integers found and one with all floats found."
→ Output → ([25], [5.9]).

"Handles potential conversion errors gracefully."
→ Use try/except in case string has weird values.

📘 Part 3: Number Systems and Representation
Exercise 3.1: Base Converter

"Converts decimal integers to binary, octal, and hexadecimal strings without using built-in functions like bin(), oct(), or hex()."
→ You must write custom logic using division and remainders.

"Converts binary, octal, and hexadecimal strings to decimal integers without using int(x, base)."
→ Parse the string manually, multiply each digit with its base power.

"Demonstrates your functions with at least five different numbers."
→ Example: convert 10, 25, 100, 255, 512.

"Verifies your results by comparing with Python's built-in conversion functions."
→ Compare your_binary_function(25) with bin(25).

📘 Part 4: Floating-Point Precision
Exercise 4.1: Precision Problems

"Create at least five examples where floating-point arithmetic gives unexpected results."
→ Example: 0.1+0.2 != 0.3.

"For each example, explain why the result occurs."
→ Because floats are stored in binary approximation.

"Implement a solution to each problem using at least two different approaches (rounding, epsilon comparison, Decimal, Fraction, etc.)."
→ round(0.1+0.2,1), math.isclose(), Decimal("0.1")+Decimal("0.2").

"Compare the accuracy and performance of each solution."
→ Decimal = accurate but slower, rounding = faster but less precise.

📘 Part 5: Deep Dive Modules
Exercise 5.1: Math Module Explorer

"Use at least 10 different functions from the math module."
→ Examples: sqrt, ceil, floor, factorial, gcd, log, pow, sin, cos, radians.

"Create practical examples for each function."
→ e.g., math.sqrt(16) → 4.0.

"Create a function that calculates the roots of a quadratic equation using math functions."
→ Formula: (-b ± sqrt(b²-4ac)) / 2a.

"Create a function that converts between different angle units (degrees, radians) using math functions."
→ math.radians(180) → π, math.degrees(π/2) → 90.

"Include comments explaining each function and its application."
→ Add # like # sqrt() gives square root.


# In[ ]:





# In[ ]:




