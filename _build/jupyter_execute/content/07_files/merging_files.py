#!/usr/bin/env python
# coding: utf-8

# # Merging logfiles OpenSesame

# TODO

# In[1]:


from matplotlib import pyplot as plt
import os

import numpy as np

from datamatrix import DataMatrix, io, operations as ops

import pandas as pd


# Now a text here

# In[2]:


df = pd.read_csv('data/subject-0_CI.csv')
print(df)


# In[3]:


df


# In[4]:


from datamatrix import io

dm = io.readtxt('data/subject-0_CI.csv')
print(dm)


# In[5]:


#r"C:\Users\steenbergenhvan1\surfdrive\Virtual_P\My Documents\Teaching\2022-2023\Experimentation I nw style\Exp1Docs_Shared\07_Files\data"

dm = io.readtxt(r"C:\Users\steenbergenhvan1\surfdrive\Virtual_P\My Documents\Teaching\2022-2023\Experimentation I nw style\Exp1Docs_Shared\07_Files\data\subject-0_CI - copy.csv")
print(dm)


# In[ ]:





# In[6]:


# Change this to the folder that contains the .csv files
SRC_FOLDER = 'data'
# Change this to a list of column names that you want to keep
COLUMNS_TO_KEEP = [
    'subject_nr',
    'congruency',
    'response_time',
    'acc'
]


dm = DataMatrix()
for basename in os.listdir(SRC_FOLDER):
    path = os.path.join(SRC_FOLDER, basename)
    print('Reading {}'.format(path))
    dm <<= ops.keep_only(io.readtxt(path), *COLUMNS_TO_KEEP)
io.writetxt(dm, 'merged-data.csv')


# In[7]:



dm = io.readtxt('merged-data.csv')
df = pd.read_csv('merged-data.csv')

plt.plot(dm.subject_nr, dm.acc, ',')


# In[8]:


#check counts
pd.pivot_table(
    dm,
    values="acc",
    index=["subject_nr"],
    columns=["congruency"],
    aggfunc=len,
)


# In[9]:


#datamatrix syntax
plt.figure(figsize=(8,6))
plt.hist((dm.congruency == 'con').response_time, bins=100, alpha=0.5, label="data1")
plt.hist((dm.congruency == 'inc').response_time, bins=100, alpha=0.5, label="data2")


# In[10]:


#dataframe syntax
plt.figure(figsize=(8,6));
plt.hist(df.query("congruency == 'con'").response_time, bins=100, alpha=0.5, label="data1");
plt.hist(df.query("congruency == 'inc'").response_time, bins=100, alpha=0.5, label="data2");


# In[11]:



#df.head()

#df['acc']
#df.acc

#df.iloc[1]

#print(df['congruency'])

#df.shape

#dfg = df.groupby('subject_nr')
#dfg.mean()

#df.groupby('subject_nr').agg([np.sum, np.mean, np.std])


df['rt_zscore'] = df.groupby(['subject_nr','congruency'])['response_time'].transform(lambda x: (x-x.mean())/x.std())

print(df)


# In[12]:


plt.figure(figsize=(8,6));
plt.hist(df.query("congruency == 'inc' & rt_zscore <= 3").response_time, bins=100, alpha=0.5, label="data1");
plt.hist(df.query("congruency == 'inc' & rt_zscore > 3").response_time, bins=100, alpha=0.5, label="data2");


# In[13]:


import seaborn as sns

df['is_outlier'] = df['rt_zscore'] > 3

sns.set_theme(style="darkgrid")
sns.displot(
    df.query("subject_nr != 0"), x="response_time", col="congruency", row="subject_nr",
    binwidth=10, height=3, facet_kws=dict(margin_titles=True), hue = "is_outlier",
)


# In[14]:


df


# In[15]:


df_sum = df.query("rt_zscore <= 3").groupby(['subject_nr','congruency'])['response_time'].mean()


# In[16]:


df_sum


# In[ ]:




