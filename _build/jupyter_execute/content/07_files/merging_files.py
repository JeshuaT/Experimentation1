#!/usr/bin/env python
# coding: utf-8

# # Merging logfiles OpenSesame
# 
# > **Warning** During this tutorial we are going to work with files. You learn to create, copy, move, and delete files! Make sure you run your scripts in a location where you are allowed to edit files and that this location does not contain other files. Be careful and make sure you do not accidentially delete or move other files (copying is safer then moving or deleting!). Make backups of important files on your computer before continuing. The sandbox of Google Colab is a safe (more protected) environment to work with files.
# 
# ## Introduction
# OpenSesame creates a logfile separately for each participant you run. In this tutorial we show a way to merge these logfiles by assuming they all have exactly the same format (i.e., they have identical headers). This is not necessarily the case if you run slightly different versions of the experiment for different participants! Note that during the datawrangling tutorial in a later session, you will learn about a different way to merge logfiles that is more flexible.
# 
# ## Step 1. Get OpenSesame data from osf
# Let's use some python code to download existing OpenSesame data of a Stroop task from [osf](https://osf.io/7ma4t/). Note that the code below creates a folder called `tutorial_data` in your current working directory. Run the code below.

# In[23]:


import requests
import shutil
import os

# recursively remove folder main and its content, do this if you want to start again with
#shutil.rmtree('tutorial_data')

# create the main directory
if not os.path.exists('tutorial_data'):
    os.makedirs('tutorial_data')

# download the zip file
url = 'https://osf.io/download/3d9er/'
r = requests.get(url, allow_redirects=True)
open('./tutorial_data/data_pilot.zip', 'wb').write(r.content)

# extract the zip file
import zipfile
with zipfile.ZipFile('./tutorial_data/data_pilot.zip', 'r') as zip_ref:
    zip_ref.extractall('./tutorial_data/'

#os.remove removes files! Always be careful!
os.remove('./tutorial_data/CI_RSI2000_test.csv') # remove one file that is atypical


# Check whether the data is properly stored and extracted. Open a csv file to see it's content.
# 
# ## Step 2. Create a loop that finds all files in a particular directory
# Let's now create a loop that prints all the filesnames found by the os.listdir function and counts the number of files found.

# In[ ]:


# Change this to the folder that contains the .csv files
SRC_FOLDER = './tutorial_data/data/'

filecount = 0
for basename in os.listdir(SRC_FOLDER):
    path = os.path.join(SRC_FOLDER, basename)
    print('Reading ',path)
    filecount = filecount + 1
print('Number of files considered for merge:',filecount)


# ## Step 3. Merge all files into one csv file
# As a next step, we are going to read in each file line by line and write them to a new merged file.
# 
# To create the new merged file and close the handle at the end use the following commands:

# In[24]:


fout = open('./tutorial_data/merged.csv', 'w')
#... do stuff
fout.close()


# To read in a file line by line and save each line to the merged file use this loop:

# In[25]:


fhand = open(path)
for line in fhand:
    fout.write(line)
fhand.close()


#  Insert these code snippets in the code we just created at the right locations:
# 

# In[ ]:


# Change this to the folder that contains the .csv files
SRC_FOLDER = './tutorial_data/data/'
# ... your code here

filecount = 0
for basename in os.listdir(SRC_FOLDER):
    path = os.path.join(SRC_FOLDER, basename)
    print('Reading ',path)
    # ... your code here
    filecount = filecount + 1
print('Number of files considered for merge:',filecount)
# ... your code here


# Run the code and check whether a merged file is created.
# 
# Solution:

# In[ ]:


# Change this to the folder that contains the .csv files
SRC_FOLDER = './tutorial_data/data/'
fout = open('./tutorial_data/merged.csv', 'w')

filecount = 0
for basename in os.listdir(SRC_FOLDER):
    path = os.path.join(SRC_FOLDER, basename)
    print('Reading ',path)
    fhand = open(path)
    for line in fhand:
        fout.write(line)
    fhand.close()
    filecount = filecount + 1
print('Number of files considered for merge:',filecount)
fout.close()


# ## Step 4. Compare headers
# 
# 
# 
# 
# 

# In[ ]:


# Change this to the folder that contains the .csv files
SRC_FOLDER = './tutorial_data/data/'

fout = open('./tutorial_data/merged.csv', 'w')

filecount = 0
filecountmerged = 0
for basename in os.listdir(SRC_FOLDER):
    path = os.path.join(SRC_FOLDER, basename)
    if path !=  "./tutorial_data/data/CI_RSI2000_test.csv":
        print('Reading {}'.format(path))
        fhand = open(path)
        linecount = 0
        for line in fhand:

            #print('number of commas: ',line.count(','))
            if linecount == 0:
                if filecount == 0:
                    #header first file
                    refheader =  line
                    fout.write(line)
                    write_this_file = True
                else:
                    #check whether current header matches refheader
                    if line == refheader:
                        write_this_file = True
                        filecountmerged = filecountmerged + 1
                    else:
                        write_this_file = False
            else:
                if write_this_file:
                    fout.write(line)
            linecount = linecount + 1
        print('Line Count:', linecount)
        fhand.close()
        filecount = filecount + 1
fout.close()
print('Number of files considered for merge:',filecount,". Merged: ",filecountmerged)


# 
# # Exercises
# 
# ### Exercise 1. Count number of files merged
# Add a counter to the script created in the tutorial that keeps the number of files that are merged. Add this number in the print message at the end of the script.

# In[ ]:


# your code here


# ### Exercise 2. Manually change content of merged file
# 
# Create a script that opens the merged file created with the code in the tutorial above. Replace all words "neutral" with "neu" and save the edited file under a new name.

# In[ ]:


# your code here


# 
# ### Exercise 3. Copy renamed files to another location
# 
# Run the following code to create a folder structure with 10 dummy textfiles nested into 10 folders. Assume that the text files reflect data belonging to ten participants.

# In[ ]:


import os
import shutil

# recursively remove folder tutorial_data2 and its content
#shutil.rmtree("tutorial_data2")

# create the tutorial_data directory
if not os.path.exists('tutorial_data2'):
    os.makedirs('tutorial_data2')

# create the subdirectories
for i in range(1, 11):
    directory_name = os.path.join('tutorial_data2', str(i))
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

# create the text files
for i in range(1, 11):
    directory_name = os.path.join('tutorial_data2', str(i))
    file_name = os.path.join(directory_name, 'file.txt')
    with open(file_name, 'w') as f:
        for j in range(1,100):
            f.write('Hello world. \t This is another column with line number ' + str(j) + '\n')


# Now create a new script that creates a copy of all text files just created and put this copy into the main folder (tutorial_data2). Change the name of the copies file so that the participant number (1..10) is stored into the file name in this format file_pp1.txt, file_pp2.txt, etc.
# 

# In[ ]:


# your code here


# ### Exercise 4. Add information as a new column to the textfile
# 
# Create a script that opens the textfiles you created in exercise 2 and that addz the name of its file as a first column (assume data is tab-delimited), so that each file consists of three columns.

# In[ ]:


# your code here


# ### Exercise 5. Merge the new textfiles to a single textfile
# 
# Create a script that merges all files created in Exercise 3 into a single text file. Start the text file with a header indicating file name, column 2, and column 3 separated by tabs.
# 
# Open the tab-delimited text file in a spreadsheet program and check whether it opens properly in 3-column format.

# In[ ]:


# your code here

