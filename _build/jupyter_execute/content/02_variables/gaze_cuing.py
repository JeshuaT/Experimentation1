#!/usr/bin/env python
# coding: utf-8

# # Gaze cuing task in OpenSesame

# In[10]:


from IPython.display import IFrame


# The tutorial can be found [here](https://osdoc.cogsci.nl/3.3/tutorials/beginner/)

# In[11]:




IFrame(src="https://osdoc.cogsci.nl/3.3/tutorials/beginner/", width="800", height="600")


# 
# ## Exercises
# 
# ### Exercise 1. Express the location of the cues in relative terms
# Let's now adapt the gaze cuing experiment you created in the tutorial. Change the 300 and -300 values into percentages (e.g. 10% and -10%) and calculate the x-coordinates of both the target and the distractor based on the resolution (width) of the screen.
# 
# Test whether the location is updated when you change the resolution of the screen.
# 
# ### Exercise 2. Calculate average performance
# 
# Change the TimeOut value of the Keyboard_response object to 500 (ms) so that missing values are recorded. How does OpenSesame store missing responses? Check this in the log file.
# 
# Now count the number of times the response was correct, incorrect and missing. Also, count the total number of trials presented in the block. Present the percentage of correct, incorrect, and missing responses in the feedback item. Compare whether the values you calculated correspond with the values automatically created by OpenSesame.

# In[9]:




