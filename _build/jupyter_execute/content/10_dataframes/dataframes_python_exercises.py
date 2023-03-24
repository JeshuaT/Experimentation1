#!/usr/bin/env python
# coding: utf-8

# # Python exercises: Dataframes

# ## Exercise 1. Loading and inspecting a dataframe

# In Chapter 7, you learned how to load in data of a Stroop task. Furthermore, in the lesson of this chapter you learned many things about how to use dataframes. Here we are going to implement some of the things you learned in the lesson.
# 
# The following URL contains the datafile that we will work with:
# ```https://raw.githubusercontent.com/JeshuaT/Experimentation1/main/content/10_dataframes/data/data_exercises/subject-1_IC.csv```
# 
# For the first exercise:
# (1) read the csv file and store it in a Pandas dataframe
# (2) look at top 5 and bottom 5 rows of the Pandas dataframe using the head and tail function
# (3) print out only the 'response_time' column
# (3) find out whether the response time at the 67th row is lower or higher than 1000ms (watch out: python starts counting at 0!)

# In[ ]:


import pandas as pd

# your code here


# ## Exercise 2. Removing rows and columns

# OpenSesame dataframes are usually enormous, because it stores everything you want but also many things you don't need. In this exercise we are going to clean up the dataframe a bit from this clutter.
# 
# (1) print out the shape of the dataframe
# (2) make a new dataframe where you only keep the following columns: 'subject_nr', 'correct', 'response_time', 'congruency'
# (3) make another new dataframe, based on the dataframe of (2), where you only keep correct trials (correct is defined with a "1" in the "correct" column
# (4) print out the shape of the new dataframe, what has changed?

# In[ ]:


# your code here


# ## Exercise 3. Sorting
# 
# Sorting can help to give you an idea of the highest and lowest values in a dataframe, or can be just neat for cleanliness of the dataframe.
# (1) You already have a dataframe with only correct trials. Now, make a dataframe with incorrect trials as well
# (2) Sort both dataframes based on response_time, from highest response time to lowest response time
# (3) Print out the first 10 rows of both dataframes. Which congruency seems to be the hardest for participants (con, inc or neutral)?

# In[ ]:


# your code here


# ## BONUS Exercise 4. Real-world problems

# There are many more publicly available datasets you can directly use. For this BONUS exercise, you can choose a dataset you find interesting. The website [Our World in Data](https://ourworldindata.org/) has datasets on the most pressing world-problems, now you are learning the tools how to work with these datasets! Pretty cool right. In your own Python IDE, choose and download a dataset you find interesting (search for the .csv file) and replicate each step from the [the tutorial](http://teaching.gureckislab.org/fall22/labincp/chapters/05/00-data.html), starting from subchapter 6.6.
# 
# A dataset we recommend exploring is the [dataset on global CO2 and greenhouse emission](https://github.com/owid/co2-data). However, you are free to choose any dataset you find interesting.

# In[ ]:


# your code here

