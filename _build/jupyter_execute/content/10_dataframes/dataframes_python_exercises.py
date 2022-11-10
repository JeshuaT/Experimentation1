#!/usr/bin/env python
# coding: utf-8

# # Python exercises: Dataframes

# ## Exercise 1

# In the tutorial you followed along an explanation using a open dataset with information on salary. There are many more publicly available datasets you can directly use. Even better: with one line of code you can import any dataset file from github! Now, in your own Python IDE, choose a dataset you find interesting from [this github](https://github.com/mwaskom/seaborn-data) and replicate each step from the [the tutorial](http://teaching.gureckislab.org/fall22/labincp/chapters/05/00-data.html), starting from subchapter 6.6. Below is the code to get you on your way. To get the csv link, click on one of the files in the github, and then click on the **Raw** button. This takes you to the raw code for the dataframe: copy the url from that page.

# In[1]:


import pandas as pd

# Change the link below to whatever csv you want to load in
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

