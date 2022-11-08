#!/usr/bin/env python
# coding: utf-8

# # Python exercises: Getting Ready

# > Below are adapted from: https://www.py4e.com/html3/01-intro
# 
# ### Exercise 1. Printing "Hello world!"
# **a.** What is wrong with the following code?
# ```
# primt 'Hello world!'
# File "<stdin>", line 1
#   primt 'Hello world!'
#                      ^
# SyntaxError: invalid syntax
# ```
# 
#  Correct the code and run it in the browser below:

# In[1]:


#enter your code here


# **b.** Now enter the code in Spyder and run it on your computer. Check the where you see the output.
# 
# **c.** Finally, let's use the same code in OpenSesame. Open OpenSesame and click File > New > Extended Template. Drag a new `inline_script` object from the Toolbar after the `instructions` object and enter the same python code. Run the experiment in a Window (use the green >> button) and check whether the message is printed to the Console. Close the experiment (Escape) and move the inline script into the `trial_sequence`. When is the print executed? How often is the print executed?
# 
# ### Exercise 2. Incrementing value of numeric variable
# 
# **a.** Run the following code in the browser, in Spyder and in OpenSesame using the same method as described in Exercise 1. What value is printed out?
# 
# ```
# myvar = 43
# myvar = myvar + 1
# print(myvar)
# ```

# In[2]:


#enter your code here


# **b.** Now, in OpenSesame, split the code into multiple `inline_scripts`. The inline after the  `instructions` object assigns the value 43 to x. The inline in the `trial_sequence` only increments x with 1 and prints x. What values are printed in the OpenSesame console when you run the experiment in windowed mode?
# 
# **c.** Finally, let's convert the python variable to an OpenSesame `experimental variable` (we will learn more this in the next session, also see https://osdoc.cogsci.nl/3.3/manual/variables/).
# 
# The advance of experimental variables in OpenSesame are:
# - They can be referred to in other objects (using the [] notation, to be discussed next session);
# - The value can be inspected during runtime using the Variable Inspector;
# - They can be logged in the textfile via the logger object.
# 
# Go back to OpenSesame and add `var.` to all mentions of variable myvar, like:
# 
# ```
# var.myvar = 43
# ```
# 
# and
# ```
# var.myvar = var.myvar + 1
# print(var.myvar)
# ```
# Note that this `var.` notation is specific to OpenSesame and does not work outside OpenSesame, e.g. in the browser or in Spyder.
# 
# Before running the experiment in windowed mode, open the `Variable Inspector` and search for `myvar`. Run the experiment and see whether the values are updated in the Variable Inspector and in the Console. Finish the experiment and check whether the values are properly saved into the logfile.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[3]:


#enter your code here

