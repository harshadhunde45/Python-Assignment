#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Python Strings Assignment (Basic to Advanced)

Date: May 9, 2025 (Friday)
Topic: String Manipulation in Python
    
Instructions
This assignment progresses from basic string operations to more advanced string manipulation
techniques. Complete all sections, showing your work for each problem. Comment your code to
explain your approach.

Section 1: Creating & Accessing Strings (Basic)
1. Create three different strings using different quotation methods (single quotes, double
quotes, and triple quotes).
2. Create a string variable containing your full name and write code to:
o Print the first character
o Print the last character
o Print the length of the string
3. Given the string s = "Python Programming":
o Access and print the letter 'P' in "Programming" using positive indexing
o Access and print the letter 'P' in "Programming" using negative indexing

Section 2: Slicing & Extended Slicing (Basic to Intermediate)
1. Using the string s = "Python Programming":
o Extract and print "Python"
o Extract and print "Programming"
o Extract and print "gram"
2. Given s = "0123456789":
o Extract every even-indexed character
o Extract every odd-indexed character
o Reverse the string using slicing
3. Create a function that takes a string and returns a "rotated" version where the first
character is moved to the end. For example, "Python" becomes "ythonP".

Section 3: Immutability & Interning (Intermediate)
1. Demonstrate string immutability with an example. Try to change a character in a string
and explain what happens.
2. Write code to check if two strings with the same content point to the same memory
location. Test this with:
o Two string literals with the same content
o Two string variables assigned the same string literal
o Two string variables created using string operations that result in the same content
3. Create a function that efficiently concatenates a large number of strings. Compare your
approach with using the + operator in a loop.

Section 4: String Methods (Intermediate)
1. Given the string s = " Python is Amazing! ":
o Remove leading and trailing whitespace
o Convert to all uppercase
o Convert to all lowercase
o Replace "Amazing" with "Awesome"
2. Write a function that counts the occurrences of each character in a string and returns a
dictionary with the results.
3. Create a function that checks if a string is a palindrome (reads the same backward as
forward), ignoring case, spaces, and punctuation
4. Given s = "python,java,c++,javascript,ruby":
o Split the string into a list of programming languages
o Join the list with a different separator (e.g., " | ")

Section 5: Escape Sequences & Raw Strings (Intermediate)
1. Create a string that includes tab characters, newlines, and quotes using escape sequences.
2. Explain when you would use raw strings in Python and provide an example with file
paths.
3. Create a function that formats a multi-line address with proper newlines and indentation
using escape sequences.
4. Write a program that takes a Windows file path (with backslashes) as input and correctly
processes it using raw strings.

Section 6: Unicode & Multiline Strings (Intermediate to
Advanced)
1. Create strings containing characters from at least three different writing systems (e.g.,
Latin, Cyrillic, Arabic, CJK).
2. Write a function that counts the number of characters in a Unicode string, taking into
account combining characters and surrogate pairs.
3. Create a multi-line string containing a short poem or quote with proper formatting.
4. Create a function that takes a multi-line string and returns the line with the most
characters.

Section 7: String Formatting (Advanced)
1. Format the same data using all three main formatting methods (f-strings, .format(), and
% formatting):
o Format a floating-point number to two decimal places
o Format an integer with leading zeros
o Format a string with fixed width and alignment
2. Given a dictionary with student information (name, ID, grades), create formatted output
using all three formatting methods.
3. Create a function that generates a table of data with proper alignment using f-strings.
4. Write a program that formats dates and times in different regional formats using string
formatting


# In[ ]:


Section 1: Creating & Accessing Strings (Basic)
1. Create three different strings using different quotation methods (single quotes, double
quotes, and triple quotes).
2. Create a string variable containing your full name and write code to:
o Print the first character
o Print the last character
o Print the length of the string
3. Given the string s = "Python Programming":
o Access and print the letter 'P' in "Programming" using positive indexing
o Access and print the letter 'P' in "Programming" using negative indexing


# In[4]:


1. Create three different strings using different quotation methods (single quotes, double
quotes, and triple quotes).

a= "Harsha dhunde"

c=""" Nikhil harsha dhunde"""


# In[7]:


print(a)

print(c)


# In[ ]:


2. Create a string variable containing your full name and write code to:
o Print the first character
o Print the last character
o Print the length of the string
3. Given the string s = "Python Programming":
o Access and print the letter 'P' in "Programming" using positive indexing
o Access and print the letter 'P' in "Programming" using negative indexing


# In[8]:


a="nikhil harsha dhopre"


# In[9]:


a[0]


# In[10]:


a[-1]


# In[11]:


len(a)


# In[13]:


s = "Python Programming"


# In[14]:


"""o Access and print the letter 'P' in "Programming" using positive indexing"""
s[7]


# In[17]:


"""Access and print the letter 'P' in "Programming" using negative indexing"""
s[-11]



# Section 2: Slicing & Extended Slicing (Basic to Intermediate)
# 1. Using the string s = "Python Programming":
# o Extract and print "Python"
# o Extract and print "Programming"
# o Extract and print "gram"
# 2. Given s = "0123456789":
# o Extract every even-indexed character
# o Extract every odd-indexed character
# o Reverse the string using slicing
# 3. Create a function that takes a string and returns a "rotated" version where the first
# character is moved to the end. For example, "Python" becomes "ythonP"

# In[19]:


s = "Python Programming"
s[0:6:1]


# In[21]:


s[7:18:1]


# In[22]:


s[10:14:1]


# In[24]:


s = "0123456789"
s[2:10:2]


# In[25]:


s[1:10:2]


# In[26]:


s[::-1]


# In[ ]:


"""3. Create a function that takes a string and returns a "rotated" version where the first
character is moved to the end. For example, "Python" becomes "ythonP"""


# In[28]:


a="rotated"


# In[29]:


a[::-1]


# In[30]:


a[1:]


# In[31]:


a[0]


# In[32]:


a[1:]+a[0]


# In[ ]:


Section 3: Immutability & Interning (Intermediate)
1. Demonstrate string immutability with an example. Try to change a character in a string
and explain what happens.
2. Write code to check if two strings with the same content point to the same memory
location. Test this with:
o Two string literals with the same content
o Two string variables assigned the same string literal
o Two string variables created using string operations that result in the same content
3. Create a function that efficiently concatenates a large number of strings. Compare your
approach with using the + operator in a loop.


# In[ ]:


a= "Nikhil"


# In[33]:


id(a)


# In[34]:


a = "python"
b = "python"
print("A equality:", a == b)            # True
print("A same object (is):", a is b)   # Often True due to interning
print("A ids:", id(a), id(b))


# In[ ]:


Section 4: String Methods (Intermediate)
1. Given the string s = " Python is Amazing! ":
o Remove leading and trailing whitespace
o Convert to all uppercase
o Convert to all lowercase
o Replace "Amazing" with "Awesome"
2. Write a function that counts the occurrences of each character in a string and returns a
dictionary with the results.
3. Create a function that checks if a string is a palindrome (reads the same backward as
forward), ignoring case, spaces, and punctuation
4. Given s = "python,java,c++,javascript,ruby":
o Split the string into a list of programming languages
o Join the list with a different separator (e.g., " | ")

Section 5: Escape Sequences & Raw Strings (Intermediate)
1. Create a string that includes tab characters, newlines, and quotes using escape sequences.
2. Explain when you would use raw strings in Python and provide an example with file
paths.
3. Create a function that formats a multi-line address with proper newlines and indentation
using escape sequences.
4. Write a program that takes a Windows file path (with backslashes) as input and correctly
processes it using raw strings.


# In[35]:


s = " Python is Amazing! "


# In[37]:


s.upper()


# In[38]:


s.lower()


# In[40]:


"""Replace "Amazing" with "Awesome"""
s[11::]


# In[43]:


s= s.replace("Amazing" , "Awesome")
print(s)


# In[ ]:


Palindrome = mirror string → same if you flip it around.


# In[ ]:


import string

def is_palindrome(s):
    # keep only letters/numbers and make lowercase
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]   # compare forward vs reverse

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("hello"))


# In[1]:


s = "python,java,c++,javascript,ruby"

# Split into list
languages = s.split(",")
print(languages)

# Join with " | "
joined = " | ".join(languages)
print(joined)


# In[2]:


languages = s.split(",")
print(languages)
joined ="|".join(languages)
print(joined)


# In[3]:


a = s.split(",")
print(a)
b= "|".join(a)
print(b)


# In[ ]:


1. Create a string that includes tab characters, newlines, and quotes using escape sequences.
2. Explain when you would use raw strings in Python and provide an example with file
paths.
3. Create a function that formats a multi-line address with proper newlines and indentation
using escape sequences.
4. Write a program that takes a Windows file path (with backslashes) as input and correctly
processes it using raw strings.


# In[2]:


a = "\n  nikhil \t dhopre"
print(a)


# In[ ]:


a ="""i am learning python"""


# In[3]:


# Multi-line address using \n for new line and \t for indentation
name = "Harsha Dhunde"
street = "123 MG Road"
city = "Pune"
pincode = "411057"

print("F*My name is {name}, our street {street},city name {city},my pincode is{pincode}")



# In[ ]:


print("My name is {}, our street {}, city name {}, my pincode is {}".format(name, street, city, pincode))


# In[5]:


print(f"My name is {name},our street {street}, my pincode is {pincode}")


# In[7]:


print("My name is {}, our street {},city name {}, my pincode is {}". format(name,street,city,pincode))


# In[ ]:


a = 10
b = 5
print(f"Sum = {a + b}, Product = {a * b}")


# In[8]:


a= 4
b=6
print(f"sum ={a+b}, product ={a*b}, minus ={a-b}" )


# In[13]:


a = 8
b = 5

sum = a + b
product = a * b
minus = a - b

print("sum {}, product {}, minus {}".format(sum, product, minus))


# In[15]:


a=2
b=6
sum = a+b
product = a*b 
minus = a-b
print("sum {},product {},minus {}" .format(sum, product , minus))


# In[16]:


# Without raw string
print("C:\newfolder\test.txt")


# In[17]:


# With raw string
print(r"C:\newfolder\test.txt")


# In[18]:


name = "Harsha"
print(rf"C:\Users\{name}\Documents")


# In[22]:


print(rf"C:\newfolder\test.txt")


# In[ ]:





# In[ ]:





# In[ ]:


Section 6: Unicode & Multiline Strings (Intermediate to
Advanced)
1. Create strings containing characters from at least three different writing systems (e.g.,
Latin, Cyrillic, Arabic, CJK).
2. Write a function that counts the number of characters in a Unicode string, taking into
account combining characters and surrogate pairs.
3. Create a multi-line string containing a short poem or quote with proper formatting.
4. Create a function that takes a multi-line string and returns the line with the most
characters.

Section 7: String Formatting (Advanced)
1. Format the same data using all three main formatting methods (f-strings, .format(), and
% formatting):
o Format a floating-point number to two decimal places
o Format an integer with leading zeros
o Format a string with fixed width and alignment
2. Given a dictionary with student information (name, ID, grades), create formatted output
using all three formatting methods.
3. Create a function that generates a table of data with proper alignment using f-strings.
4. Write a program that formats dates and times in different regional formats using string
formatting


# In[ ]:


# ---------------------------------------------------------
# SECTION 6: Unicode & Multiline Strings
# ---------------------------------------------------------

# 1. Unicode Strings from different writing systems
latin = "Hello"
cyrillic = "Привет"     # Russian
arabic = "مرحبا"        # Arabic
cjk = "こんにちは"        # Japanese

print(latin, cyrillic, arabic, cjk, sep=" | ")

# 2. Function to count Unicode characters considering combining marks
import unicodedata

def unicode_length(text):
    count = 0
    for ch in text:
        if not unicodedata.combining(ch):
            count += 1
    return count

sample = "áéíóú"
print("\nNormal length:", len(sample))
print("Unicode-aware length:", unicode_length(sample))

# 3. Multi-line formatted string
poem = """
🌿 The Quiet Path 🌿

When silence speaks louder than words,
When calm becomes the loudest voice,
Choose peace — for in peace,
Your soul learns to rest.
"""

print("\n" + poem)

# 4. Function to get longest line from a multi-line string
def longest_line(text):
    lines = text.strip().split("\n")
    return max(lines, key=len)

print("Longest line:", longest_line(poem))


# ---------------------------------------------------------
# SECTION 7: String Formatting (Advanced)
# ---------------------------------------------------------

num_float = 45.6789
num_int = 42
name = "Python"

print("\n--- Formatting with F-String ---")
print(f"Float: {num_float:.2f}")
print(f"Integer: {num_int:05d}")
print(f"String: |{name:^10}|")

print("\n--- Formatting with .format() ---")
print("Float: {:.2f}".format(num_float))
print("Integer: {:05d}".format(num_int))
print("String: |{:^10}|".format(name))

print("\n--- Formatting with %% operator ---")
print("Float: %.2f" % num_float)
print("Integer: %05d" % num_int)
print("String: |%-10s|" % name)


# 2. Format dictionary data with all methods
student = {"name": "Harsha", "id": 2025, "grade": 92.5}

print("\n--- Student Info Formatting ---")
print(f"F-String      => Student: {student['name']} | ID: {student['id']} | Grade: {student['grade']:.1f}")
print("Format()      => Student: {} | ID: {} | Grade: {:.1f}".format(student["name"], student["id"], student["grade"]))
print("Percent (%)   => Student: %s | ID: %d | Grade: %.1f" % (student["name"], student["id"], student["grade"]))


# 3. Function to build formatted table using f-strings
def build_table(data):
    print("\nName         Age   City")
    print("-" * 25)
    for row in data:
        print(f"{row['name']:<12} {row['age']:<5} {row['city']}")

records = [
    {"name": "Harsha", "age": 23, "city": "Pune"},
    {"name": "Nikhil", "age": 31, "city": "Nagpur"},
    {"name": "Asha", "age": 55, "city": "Mumbai"}
]

build_table(records)


# 4. Date formatting in different regions
from datetime import datetime

now = datetime.now()

print("\n--- Regional Date Formats ---")
print("US Format:     ", now.strftime("%m/%d/%Y, %I:%M %p"))
print("India Format:  ", now.strftime("%d-%m-%Y, %H:%M"))
print("ISO Format:    ", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Japan Format:  ", now.strftime("%Y年%m月%d日 %H:%M"))


# In[24]:


latin = "Hello"        # Latin alphabet
cyrillic = "Привет"    # Cyrillic alphabet (Russian)
arabic = "مرحبا"        # Arabic script
cjk = "你好"             # Chinese characters

mixed = latin + " " + cyrillic + " " + arabic + " " + cjk
print(mixed)


# In[25]:


poem = """Roses are red,
Violets are blue,
Python is fun,
And so are you."""

print(poem)


# In[26]:


def longest_line(multiline_str):
    lines = multiline_str.split("\n")  # split into lines
    max_line = max(lines, key=len)      # find the line with max length
    return max_line

# Example usage
text = """Roses are red,
Violets are blue,
Python is fun,
And so are you."""

print("Longest line:", longest_line(text))


# In[27]:


# Data
num_float = 12.3456
num_int = 42
text = "Hello"

# f-string formatting
print(f"Float: {num_float:.2f}, Int: {num_int:05d}, Text: {text:<10}")

# .format() formatting
print("Float: {:.2f}, Int: {:05d}, Text: {:<10}".format(num_float, num_int, text))

# % formatting
print("Float: %.2f, Int: %05d, Text: %-10s" % (num_float, num_int, text))


# In[5]:


a= 3
b=4
print(f"sum of two numbers {a},{b}, addition  is {a+b}")


# In[ ]:





# In[ ]:





# In[ ]:




