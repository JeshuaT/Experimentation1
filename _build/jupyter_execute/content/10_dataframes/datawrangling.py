#!/usr/bin/env python
# coding: utf-8

# # Session 10
# 

# In[1]:



dm = io.readtxt('merged-data.csv')
df = pd.read_csv('merged-data.csv')

plt.plot(dm.subject_nr, dm.acc, ',')


# In[2]:


#check counts
pd.pivot_table(
    dm,
    values="acc",
    index=["subject_nr"],
    columns=["congruency"],
    aggfunc=len,
)


# In[3]:


#datamatrix syntax
plt.figure(figsize=(8,6))
plt.hist((dm.congruency == 'con').response_time, bins=100, alpha=0.5, label="data1")
plt.hist((dm.congruency == 'inc').response_time, bins=100, alpha=0.5, label="data2")


# In[4]:


#dataframe syntax
plt.figure(figsize=(8,6));
plt.hist(df.query("congruency == 'con'").response_time, bins=100, alpha=0.5, label="data1");
plt.hist(df.query("congruency == 'inc'").response_time, bins=100, alpha=0.5, label="data2");


# In[5]:



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


# In[6]:


plt.figure(figsize=(8,6));
plt.hist(df.query("congruency == 'inc' & rt_zscore <= 3").response_time, bins=100, alpha=0.5, label="data1");
plt.hist(df.query("congruency == 'inc' & rt_zscore > 3").response_time, bins=100, alpha=0.5, label="data2");


# In[7]:


import seaborn as sns

df['is_outlier'] = df['rt_zscore'] > 3

sns.set_theme(style="darkgrid")
sns.displot(
    df.query("subject_nr != 0"), x="response_time", col="congruency", row="subject_nr",
    binwidth=10, height=3, facet_kws=dict(margin_titles=True), hue = "is_outlier",
)


# In[8]:


df


# In[9]:


df_sum = df.query("rt_zscore <= 3").groupby(['subject_nr','congruency'])['response_time'].mean()


# In[10]:


df_sum


# In[ ]:




