#!/usr/bin/env python
# coding: utf-8

# # Python exercises: Plotting

# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

iris


# In[2]:


sepal_length = iris['sepal_length']
sepal_width = iris['sepal_width']
species = iris['species']

plt.plot(sepal_length, sepal_width, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.title('Company profit per month')
plt.show()

