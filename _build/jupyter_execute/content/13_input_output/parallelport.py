#!/usr/bin/env python
# coding: utf-8

# # Using the parallel port in OpenSesame

# TODO tutorial plug-in provided by Iris Spruit SOLO?
# 
# based on the flanker task created in excercise 1 of the Eriksen flanker tutorial in Session 3.
# 
# https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/JeshuaT/Experimentation1/blob/main/content/solutions/flankertask_1_exercise1.osexp
# 

# # Excercises
# 
# ## Exercise 1. Add block markers
# 
# It is often convenient to have markers that indicate the start and the end of each block of trials, for example if you want to exclude EEG or other physiological data collected during the breaks when analyzing your data. Add the markers 101 and 102 to indicate the start and the end of the practice block, respectively. Add the markers 111 and 112 for test block 1, 121 and 122 for test block 2, etc.
# 
# ## Exercise 2. Recreate the incredible scanner beam emitted by KITT
# 
# > **Note:** Part of the text below is adapted from The E-Primer (Spapé, Verdonschot, & van Steenbergen, 2019). Spapé M.M.*, Verdonschot, R.G., & van Steenbergen, H.* (2019) The E-Primer: An introduction to creating psychological experiments in E-Prime. Second edition updated for E-Prime 3. Leiden: Leiden University Press. [www.e-primer.com](http://www.e-primer.com) Copyright 2019 by the authors and LUP. Adapted with permission.
# 
# For our final exercise you will recreate the incredible scanner beam emitted by KITT from the Knight Rider television series (yes folks, dating back to the 1980s!).
# 

# In[8]:


from IPython.display import IFrame


# In[9]:


IFrame(src="https://www.youtube.com/embed/oNyXYPhnUIs", width="560", height="315")


# We will use the 8 LEDs displayed on the parallel port test device kindly provided by our lab support department. In our case the scanner beam is actually a light which starts at the left and, when it reaches the right, goes back towards the left. The easiest example to implement is the one with one light only, but if you really want to test your skills you could instead start with two lights which then move two steps to the right, ending with two lights on the right before moving back. Both examples are illustrated in the figure below.
# 
# ![](images/beaming_light_KITT.png)
# 
# Make sure the whole scanner beam repeats at least five times from left to right to allow KITT enough time to scan the surrounding area for enemies.
# 
# >**Hint** To create the light pattern use a loop that presents the values 10000000, 01000000, 00100000, etc. (entered in separate rows) sequentially. Use the conversion script you created during the exercises to convert this binary notation to a decimal notation. This decimal number should be sent to the parallel port as a marker.

# In[ ]:




