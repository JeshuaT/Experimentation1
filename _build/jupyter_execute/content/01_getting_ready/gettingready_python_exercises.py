#!/usr/bin/env python
# coding: utf-8

# # Python exercises: Getting Ready

# ### Exercise 1. First script
# Let's make a first script! Open a new file in spyder, and paste in the following code:
# 
# ```
# age = input("What is your age? Type your age here: ")
# 
# if int(age) < 24:
#     print("Wow you are young!")
# elif int(age) >= 25:
#     print("Nice, a real 90s kid")
# ```
# 
# Save the script as "age_judgement.py". Then, run the script either by pressing F5 or clicking on the green arrow with "run script". Type in your age. Do you agree with my judgements? If not, change the age and the response to the age!

# > **Note:** Some of the exercises below are adapted from the [Python for Everyone Course](https://www.py4e.com/html3/01-intro) by Charles R. Severance licensed under Creative Commons Attribution 3.0
# 
# ### Exercise 2. Printing "Hello world!"
# 
# > **Note**: For this part of the tutorial you will need to launch the script using Google Colab
# 
# What is wrong with the following code?
# ```
# primt 'Hello world!'
# ```
# 
#  Correct the code and run it in the browser below:

# In[4]:


#enter your code here


# Now enter the code in Spyder and run it on your computer. Check the where you see the output.
# 
# Finally, let's use the same code in OpenSesame. Open OpenSesame and click File > New > Extended Template. Drag a new `inline_script` object from the Toolbar after the `instructions` object and enter the same python code. Run the experiment in a Window (use the green >> button) and check whether the message is printed to the Console. Close the experiment (Escape) and move the inline script into the `trial_sequence`. When is the print executed? How often is the print executed?
# 
# ### Exercise 3. Incrementing value of numeric variable
# 
# Run the following code in the browser, in Spyder and in OpenSesame (as in the previous exercise). What value is printed out? Does it correspond between the programs?
# 
# ```
# myvar = 43
# myvar = myvar + 1
# print(myvar)
# ```

# In[5]:


#enter your code here


# ### Exercise 4. Inline scripts in OpenSesame
# Now, in OpenSesame create a new experiment using the Extended template. Now split the code shown above into multiple `inline_scripts`. The inline after the  `instructions` object assigns the value 43 to myvar. The inline in the `trial_sequence` only increments myvar with 1 and prints myvar. What values are printed in the OpenSesame console when you run the experiment in windowed mode? Why?
# 
# ### Exercise 5. Inline scripts in OpenSesame using experimental variables
# Finally, let's convert the python variable to an OpenSesame `experimental variable` (we will learn more this in the next Chapter, also see https://osdoc.cogsci.nl/3.3/manual/variables/).
# 
# The advance of experimental variables in OpenSesame are:
# - They can be referred to in other objects (using the [] notation, to be discussed next chapter);
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
