#!/usr/bin/env python
# coding: utf-8

# # Python exercises: Variables
# 
# > **Note:** Some of the exercises below are adapted from the [Python for Everyone Course](https://www.py4e.com/html3/02-variables) by Charles R. Severance licensed under Creative Commons Attribution 3.0
# 
# > **Note**: For these exercises you will need to launch the page using Google Colab.
# 
# ### Exercise 1. Print welcome text
# 
# Write a program that uses input to prompt a user for their name and then welcomes them.
# 
# ```
# Enter your name: Chuck
# Hello Chuck
# ```

# In[1]:


#your code here


# ### Exercise 2. Compute gross pay
# 
# Write a program to prompt the user for hours and rate per hour to compute gross pay.
# 
# ```
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
# ```
# 
# We won’t worry about making sure our pay has exactly two digits after the decimal place for now. If you want, you can play with the built-in Python round function to properly round the resulting pay to two decimal places.
# 

# In[2]:


#your code here


# ### Exercise 3. Numeric calculations
# 
# Assume that we execute the following assignment statements:
# 
# ```
# width = 17
# height = 12.0
# ```
# 
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).
# 
# width//2
# 
# width/2.0
# 
# height/3
# 
# 1 + 2 * 5
# 
# Use the Python interpreter to check your answers.
# 

# In[3]:


#your code here


# 
# ### Exercise 4. Convert temperature
#  Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
#  
#  ```
# Enter temperature in Celsius: 25
# Temperature in Fahrenheit: 77.0
#  ```
# 

# In[4]:


#your code here


# ### Exercise 5. Convert reaction time
#  Write a program which prompts the user for a certain reaction time value in milliseconds (between 1 and 2000 ms). Assume we want to apply a transformation of this value to correct for the skewed distribution of reaction time (in later chapters you will learn how to transform multiple values at once). Calculate the following two measures:
# 
# - Inverse RT: RTinv = -1000 / RT
# - Logarithm of RT: RTlog = log(RT)
# 
# Make sure your round both values to two decimals. Example of expected behavior:
# ```
# Enter reaction time value in ms (between 1 and 2000 ms): 987
# Inverse RT is: -1.01; Log RT is: 6.89.
# ```
# 
# For the log transformation, you will need the in-built mathematics package called "math". We import math in the code below for you. To log-transform a numeric variable, you can call the **math.log(variable)** function.

# In[5]:


#your code here
import math


# ### Exercise 6. Combine reaction time and accuracy information
#  Write a program which prompts the user for a certain average reaction time value in milliseconds (between 1 and 2000 ms) and an average accuracy score (as proportion correct scores, ranging from 0 to 1). Combine these measure to a single score called the inverse accuracy score.
# 
# Bruyer and Brysbaert (2011, p.6) explain how to calculate the inverse efficiency score (note that PE means proportion of errors):
# > To deal with the issue of how to combine speed and error, Townsend and Ashby (1978) proposed the “inverse efficiency score” (IES; see also Townsend & Ashby, 1983). IES can be thought of as an observable measure that gauges the average energy consumed by the system over time (or the power of the system; Townsend & Ashby, 1983, p. 204). It consists of RT divided by 1 - PE (or by PC, the proportion of correct responses). So, for a given participant the mean (or median) RT of the correct responses in a particular condition is calculated and divided by (1-PE) or by PC. Since RTs are expressed in ms and divided by proportions, IES is expressed in ms as well. For instance, if a participant in a particular condition responds with an average RT of 652 ms and makes 5% errors, then IES = 652/(1-.05) = 652/.95 = 686 ms.
# 
# Print all the relevant measures to the screen in one line of text, as in the example below:
# ```
# Enter average reaction time value in ms (between 1 and 2000 ms): 652
# Enter average accuracy score as proportion (between 0 and 1): .9449
# When combining an RT of 652 ms and an ACC of 0.9449 (= 5.51% errors), the IES score is 690 ms.
# ```

# In[6]:


#your code here


# ### Exercise 7. Saving and loading the jupyter notebook
# 
# Now, save your work and store the .ipynb file in a designated folder. Close this window, and re-open the Google colab. Reload your work. Is everything still there?

# # References
# 
# Bruyer, R., & Brysbaert, M. (2011). Combining speed and accuracy in cognitive psychology: Is the inverse efficiency score (IES) a better dependent variable than the mean reaction time (RT) and the percentage of errors (PE)?. *Psychologica Belgica*, *51*(1), 5-13.
