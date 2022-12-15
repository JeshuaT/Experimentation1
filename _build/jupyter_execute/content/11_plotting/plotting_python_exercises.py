#!/usr/bin/env python
# coding: utf-8

# # Python exercises: Plotting

# During the exercises in the dataframes module you learned how to import a dataset, and how to look at the dataframe from multiple angles. In the python lessons for this module you learned that you can use matplotlib in three different ways. From "quick-and-rigid" to "slow-but-flexible", these are:
# (1) Seaborn plotting
# (2) Pyplot procedural plotting
# (3) Object-oriented plotting
# 
# ## Exercise 1: Seaborn plotting
# Load in the same dataframe as you used in dataframe_exercises:
# https://raw.githubusercontent.com/JeshuaT/Experimentation1/main/content/10_dataframes/data/subject-3.csv
# 
# Now, using seaborn, make a bar plot of the response time of each value in 'congruency'. Give the plot a title. Which value has the highest response times?

# In[ ]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/JeshuaT/Experimentation1/main/content/10_dataframes/data/data_exercises/subject-1_IC.csv')

# your code here


# 
# ## Exercise 2: Matplotlib Procedural Plotting
# Now, make the same plot using the matplotlib procedural plotting approach (don't forget to include the title as well).

# In[ ]:


# your answer here


# ## Exercise 3: Matplotlib Object-Oriented Plotting
# Yes, you guessed it: now plot the same plot using the object-oriented approach (again, title!).

# In[ ]:


# your answer here

