#!/usr/bin/env python
# coding: utf-8

# # Python exercises: Dataframes

# ## Exercise 1: Loading in and inspecting a dataframe

# In session 7, you learned how to load in data of a Stroop task. Furthermore, in the lesson of this session you learned many things about how to use dataframes. Here we are going to implement some of the things you learned in the lesson.
# 
# 
# (1) read a csv file and store it in a Pandas dataframe
# (2) look at top and bottom of the Pandas dataframe using the head and tail function
# (3) Access and remove individual columns and rows
# (4) Combine multiple dataframes

# In[2]:


import pandas as pd

# Change the link below to whatever csv you want to load in
df = pd.read_csv('./data/data_exercises/subject-0_CI.csv')

df


# ## BONUS Exercise 2: Real-world problems

# There are many more publicly available datasets you can directly use. For this exercise, you can choose a dataset you find interesting. The website [Our World in Data](https://ourworldindata.org/) has datasets on the most pressing world-problems, now you are learning the tools how to work with these datasets! Pretty cool right. In your own Python IDE, choose and download a dataset you find interesting (search for the .csv file) and replicate each step from the [the tutorial](http://teaching.gureckislab.org/fall22/labincp/chapters/05/00-data.html), starting from subchapter 6.6.
# 
# A dataset we recommend exploring is the [dataset on global CO2 and greenhouse emission](https://github.com/owid/co2-data). However, you are free to choose any dataset you find interesting.

# In[ ]:


import pandas as pd

# Change the link below to whatever csv you want to load in
df = pd.read_csv('filename.csv')

