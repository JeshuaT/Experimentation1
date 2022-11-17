#!/usr/bin/env python
# coding: utf-8

# # Digital Span Task in OpenSesame

# ## Step 1: Download OpenSesame file and adapt it
# 
# Download the Digit Span task created by Grant M. Berry here.
# 
# Open the file in OpenSesame and try to understand how it works.
# 
# Let's first make the layout of the loop nicer and reorder the columns in the `Trials` loop. This is not easy to do in OpenSesame, so use Excel (or other spreadsheet software) instead.
# 
# 1.  Copy the entire content of the loop to a sheet in Excel. 2. Copy again and paste the transposed table (Paste Special) in a new sheet. 3. Sort the entire table on the first column (no header). 4. Copy again and paste again in a new sheet as transposed table. 5. Copy this table and paste it in the OpenSesame loop after you deleted all columns and rows first.
# 
# Please note that Nback indicates the span of the sequence presented in the corresponding trial.
# 
# Interestingly, if you run the program it always starts with span 3. Why is this the case? Fix the conditional running.
# 
# Actually, let's remove the 10 first rows all together.
# 
# Set Weight to 1 (easier for debugging)
# 
# ## Step 2: Change number stimuli into characters
# 
# Let's add some python code to provide real-time feedback to the participant whether the answer used was correct
# 
# We first change the stimuli we present. Instead of presenting numbers 1..9 that can be used multiple times (random.choice picks a value WITH replacement)

# In[1]:


import random
nums=[1,2,3,4,5,6,8,9]
random.shuffle(nums)
num0=random.choice(nums)
num1=random.choice(nums)
num2=random.choice(nums)
num3=random.choice(nums)
num4=random.choice(nums)
num5=random.choice(nums)
...
...
...
...
...


# In[2]:


import random
nums=["A","B","C","D","E","F","G","H","I","J"]
random.shuffle(nums)
num0=nums[0]
num1=nums[1]
num2=nums[2]
num3=nums[3]
num4=nums[4]
num5=nums[5]
num6=nums[6]
num7=nums[7]
num8=nums[8]
num9=nums[9]


# 
# Now let's print the content of the nine variables in a string

# In[3]:


import random
seq_presented = num0 + num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9
print(seq_presented)


# 
# change sequence depending on Nback

# In[4]:


Nback = 2
seq_presented = seq_presented[0:Nback]
print(seq_presented)


# 
# raise an exception if current_span \> length

# In[5]:


Nback = 4
if Nback > len(seq_presented):
    raise Exception('Invalid value for Nback (%s)' % Nback)

seq_presented = seq_presented[0:Nback]
print(seq_presented)


# 
# If your code works well, go back to OpenSesame and add it in the proper locations: the code for the presented stimuli should be inserted into `GenerateNums` and replace the part that refers to numbers.
# 
# In addition, add a python inline script before the logger and call it `process_trial`
# 
# Add the code that calculates the `seq_presented` in this inline.
# 
# Make sure you all variables with `var.` that refer to the OpenSesame environment.
# 
# Check: is your data correctly logged. TODO: why is it not in the CSV??
# 

# 
# ### Step 3: Provide feedback
# 
# Let's go back to the code in this tutorial.
# 

# In[ ]:


response = "fcd"
if (response == seq_presented):
    print("Correct")
else:
    print("Error")


# remove spaces and make all capitals

# In[ ]:


response = "fe"
response = response.upper()
response = response.strip()
if (response == seq_presented):
    fbtext = "Correct"
else:
    fbtext = "Error"
print(fbtext)


# 
# get number of correctly retrieved items
# 

# In[ ]:


num_correct = 0
num_total = len(response)
for char in response:
    if (seq_presented.find(char)) > -1:
        num_correct = num_correct + 1
print(num_correct)


# 
# # Exercises
# 
# TODO
# 1. stop presenting when more than four trials in a row were incorrect
# 
# 2.  recollect in reverse orde
