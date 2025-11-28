#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Write a Python script to compare two numbers and print whether the first is greater.
2. Check if a given number is between 10 and 50.
3. Write a program that checks if a number is positive and even using logical and.
4. Given two strings, check if either string is empty using logical or.
5. Use not to flip a boolean variable and print its new value.
6. Evaluate and explain: 5 > 3 and 2 < 4
7. Determine the output: not (3 == 3 or 4 > 5)
8. Write a program to check if a variable is None using is.
9. Check if two variables point to the same object using is.
10. Create two identical lists and compare them using == and is.
11. What will be the result of True and not False or False and True? Break down its
precedence.
12. Write a function that returns True if a value is false.
13. Implement a condition to check if a string is not empty and contains the word "Python".
14. Create a truth table for A and B or not A with all possible combinations.
15. Compare identity and equality with numbers and strings — explain when they behave
differently.
16. Write a function that checks if a list is empty without using len().
17. Evaluate: None == False, None is False, [] == [], [] is [] and explain.
18. Make a calculator that returns result only if all inputs are truthy; else returns 'Invalid
Input'.
19. Compare how not (x and y) differs from not x or not y using DeMorgan's Laws.
20. Assign a complex logical expression to a variable and explain it step-by-step using print
statements.


# In[1]:


a=3
b=6
c= a>b
print(c)


# In[ ]:


a


# In[4]:


a = 11 
b= 50
c = a>a<b
print (c)


# In[ ]:


1. Write a Python script to compare two numbers and print whether the first is greater.
2. Check if a given number is between 10 and 50.
3. Write a program that checks if a number is positive and even using logical and.
4. Given two strings, check if either string is empty using logical or.
5. Use not to flip a boolean variable and print its new value.
6. Evaluate and explain: 5 > 3 and 2 < 4
7. Determine the output: not (3 == 3 or 4 > 5)
8. Write a program to check if a variable is None using is.
9. Check if two variables point to the same object using is.
10. Create two identical lists and compare them using == and is.
11. What will be the result of True and not False or False and True? Break down its
precedence.


# In[6]:


a=  2
if (a = "positive" and a % = 0 ):
    print("Number is positive and even")


# In[7]:


a = 2
if (a = "positive" and a % = 0):
    print("Number is positive and even")


# In[ ]:


a = 2
if a > 0 and a % 2 == 0:
    print("Number is positive and even")


# In[ ]:


1. Write a Python script to compare two numbers and print whether the first is greater.
2. Check if a given number is between 10 and 50.
3. Write a program that checks if a number is positive and even using logical and.
4. Given two strings, check if either string is empty using logical or.
5. Use not to flip a boolean variable and print its new value.


# In[2]:


a=3
b=5
if a>b:
    print("number is greater")
else:
    print("Number is smaller")


# In[10]:


a= int(input("enter any number"))
if( a >= 10 and a <= 50):
    print("in between ")
else:
    print("not in between")
    


# In[17]:


"Write a program that checks if a number is positive and even using logical and."
a= int(input("enter any number:"))
if a>0 and a % 2 ==0:
   print("number is positive and even")
else:
   print("odd number and condition fail")


# In[ ]:


# Program to check if a number is positive and even using logical and

a = int(input("Enter any number: "))

# Condition: number should be positive AND divisible by 2
if a > 0 and a % 2 == 0:
    print("Number is positive and even")
else:
    print("Odd number or condition failed")


# In[ ]:


4. Given two strings, check if either string is empty using logical or.
5. Use not to flip a boolean variable and print its new value.


# In[18]:


a="I am learning python"
b="I am learning OOPS"
print("string is empty using logical or":)



# In[19]:


a = "I am learning python"
b = "I am learning OOPS"

# Condition: check if either a or b is empty
if a == "" or b == "":
    print("One of the strings is empty")
else:
    print("Both strings are not empty")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




