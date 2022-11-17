#!/usr/bin/env python
# coding: utf-8

# # Python exercises: Plotting

# During the exercises in the dataframes module you learned how to import a dataset, and how to look at the dataframe from multiple angles. In the python lessons for this module you learned that you can use matplotlib in three different ways. From "quick-and-rigid" to "slow-but-flexible", these are:
# (1) Seaborn plotting
# (2) Pyplot procedural plotting
# (3) Object-oriented plotting
# 
# ## Exercise 1
# Pick a dataset whereby something changes over time (e.g. the [dataset on global CO2 and greenhouse emission](https://github.com/owid/co2-data)). Import that dataset, and make sure the dataset is in a [tidy format](http://teaching.gureckislab.org/fall22/labincp/chapters/05/00-data.html#data-organization-tidy-and-wide-formats).
# 

# In[ ]:


import pandas as pd

# import the csv here

# do some data wrangling here if you need to get the dataframe in tidy format

# print out the dataframe


# 
# ## Exercise 2
# Using a seaborn lineplot, plot the change over time. Add a title, an x-label, a y-label and a legend (if suitable).

# In[ ]:


import seaborn as sns

# your answer here


# ## Exercise 3
# Now, make the same plot using the pyplot procedural plotting approach. Including the title, x-label and y-label.
# 
# > **Hint**: [This youtube video](https://www.youtube.com/watch?v=_LWjaAiKaf8&ab_channel=CoreySchafer) could be of help, as well as [this tutorial](https://machinelearningmastery.com/time-series-data-visualization-with-python/).

# In[ ]:


import matplotlib.pyplot as plt

# your answer here


# ## Exercise 4
# Yes, you guessed it: now plot the same plot using the object-oriented approach. Again including the title, x-label and y-label.
# 
# > **Hint:** [This tutorial](https://www.python-graph-gallery.com/basic-time-series-with-matplotlib) is useful for this approach

# In[ ]:


import matplotlib as plt

# your answer here

