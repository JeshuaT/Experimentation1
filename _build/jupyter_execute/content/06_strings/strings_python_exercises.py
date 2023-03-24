#!/usr/bin/env python
# coding: utf-8

# # Python exercises: Strings

# >**Note** Some of the exercises below are adapted from the [Python for Everyone Course](https://www.py4e.com/html3/06-strings) by Charles R. Severance licensed under Creative Commons Attribution 3.0
# 
# ### Exercise 1. Extract substring
# Take the following Python code that stores a string:
# 
# ```
# text1 = 'X-DSPAM-Confidence:0.8475'
# ```
# 
# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
# 

# In[2]:


text1 = 'X-DSPAM-Confidence:0.8475'
# your code here


# ### Exercise 2. Understanding string methods
# 
# Read the documentation of the string methods [here](https://docs.python.org/library/stdtypes.html#string-methods). You might want to experiment with some of them to make sure you understand how they work. Strip and replace are particularly useful.
# 
# The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.
# 
# Then use these commands to remove leading, trailing and double spaces (iteratively) in the string indicated below and replace the word "setece" with "sentence".

# In[3]:


text2 = "  This is a  setece      with  a typo and   too many  spaces "
# your code here


# ### Exercise 3. Create a looping text
# 
# Adapt the program you wrote in the previous chapter to present a moving text of 40 characters long that runs like a circle from left to right: when characters reach the end they starts to appear at the beginning again.
# 
# Work step by step!
# - If you do not know where to start, assume you want to print the string "1234" and write out what should be the values (use a piece of paper!), like this sketch:
# 
# ![](images/loopingtext.png)
# 
# - If the script works for "1234", you can change the code to make it work for a string of any length e.g. "Look at this moving text!!!!!!!!!!!!!!!!" (40 characters long).
# 
# - If this works, repeat the loop for 3 cycles (add an outer loop that runs 3 times)

# In[4]:


# your code here

