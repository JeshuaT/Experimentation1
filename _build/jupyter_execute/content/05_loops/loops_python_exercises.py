#!/usr/bin/env python
# coding: utf-8

# # Python exercises: Loops

# >**Note** Some of the exercises below are adapted from the [Python for Everyone Course](https://www.py4e.com/html3/05-iterations) by Charles R. Severance licensed under Creative Commons Attribution 3.0
# 
# ### Exercise 1. Print total, count, and average
# 
# Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
# 
# ```
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333
# ```
# ### Exercise 2. Print maximum and minimum
# Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.
# 
# ### Exercise 3. Print moving text
# Write a program that prints Hello world repeatedly (40 times) to the screen preceded by a string called fill that adds a space to itself each time the loop is repeated. You should see the text Hello world moving to the right of the screen. Refresh the loop each ~100 ms (0.1 seconds).

# In[1]:



fill = ""
import time
for i in range(1,41):
    fill = fill + " "
    print(fill + 'Hello world',end="\r", flush=True)
    time.sleep(0.1)


# 
