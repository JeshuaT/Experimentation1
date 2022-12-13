#!/usr/bin/env python
# coding: utf-8

# # Python exercises: Strings

# >**Note** Some of the exercises below are adapted from the [Python for Everyone Course](https://www.py4e.com/html3/06-strings) by Charles R. Severance licensed under Creative Commons Attribution 3.0
# 
# ### Exercise 1. Extract substring
# Take the following Python code that stores a string:
# 
# ```
# str = 'X-DSPAM-Confidence:0.8475'
# ```
# 
# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
# 

# In[7]:


str = 'X-DSPAM-Confidence:0.8475'
# your code here


# ### Exercise 2. Understanding string methods
# 
# Read the documentation of the string methods [here](https://docs.python.org/library/stdtypes.html#string-methods). You might want to experiment with some of them to make sure you understand how they work. Strip and replace are particularly useful.
# 
# The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.
# 
# Then use these commands to remove leading, trailing and double spaces (iteratively) in the string indicated below and replace the word "setece" with "sentence".

# In[8]:


str = "  This is a  setece      with  a typo and   too many  spaces "
# your code here


# ### Exercise 3. Create a looping text
# 
# Adapt the program you wrote in the previous session to present a moving text of 40 characters long that runs like a circle from left to right: when characters reach the end they starts to appear at the beginning again. Let the loop run from 1 to 80 so you can present a full circle.

# In[9]:


# your code here

