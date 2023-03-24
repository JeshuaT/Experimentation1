#!/usr/bin/env python
# coding: utf-8

# # OpenSesame, Anaconda and using this website

# This course makes use of several software programs and tools. In this chapter we will guide you through how to use the tools, and how to install the right programs. You will need all these programs in this course, so download them right away.
# 
# > **Tip:** There are numerous links to other websites in this jupyter book. To navigate to one of those links without leaving this jupyter notebook, you can do *ctrl+click*. Try it out with [this link](https://www.computerhope.com/jargon/c/ctrl-click.htm)

# ## OpenSesame
# We will be making use of the experiment builder [OpenSesame](https://osdoc.cogsci.nl/3.3/). The advantage of this experiment builder is that it allows you to build experiment using both a [graphical user interface (GUI)](https://en.wikipedia.org/wiki/Graphical_user_interface) and the programming language [Python](https://en.wikipedia.org/wiki/Python_(programming_language)). To download OpenSesame, navigate to the [download page](https://osdoc.cogsci.nl/3.3/download/) and choose the right installation for your operating system. For Windows, the standard download suffices. For Mac devices, you'll perhaps get a security error. To circumvent that error, follow [these](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) instructions.

# 
# > **Note**: There are other open-source python-based experiment builders with their own advantages/disadvantages. For example, [Expyriment](https://www.expyriment.org/) is more lightweight than other experiment builders, but you should be comfortable with only coding. [PsychoPy](https://www.psychopy.org/) is a good alternative for OpenSesame, but also requires a bit more coding proficiency.

# ## Anaconda
# Installing [Anaconda](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution)) is a very convenient way to get started with programming in Python if you are a psychologist/neuroscientist. If you don't have any prior programming experience, we suggest you download the latest version of Anaconda via [this link](https://www.anaconda.com/). You can view Anaconda as a kind of starter pack for doing data-science in Python: it installs not only Python for you, but also all kinds of packages (add-ons) and software that you will most certainly use as a scientist.
# 
# > **Note**: A disadvantage of Anaconda is that it also installs a lot of packages/software that you will perhaps never use. Therefore, if you already have experience with programming, a good alternative is [miniconda](https://docs.conda.io/en/latest/miniconda.html), which gives you all the functionality of Anaconda without the extra packages/software.

# ## Spyder: your Python IDE
# Just as you type words to make essays in either Word, Pages or Notepad, you can also have different software programs in which you can type Python code to make Python scripts. We call those software programs *integrated development environments (IDEs)*. Conveniently, your Anaconda installation comes with one such IDE: [Spyder](https://www.spyder-ide.org/). Just as Word and Pages have all kind of tools to help you write essays, Spyder comes with all kinds of tools to help you write Python code. However, just as you had to practice with Word to make the best use of the tool, so it is that you'll need practice to make the best use of Spyder. The best way to open Spyder is to search for the Anaconda Prompt program on your computer, and then to type in "spyder". See the screenshot below for how it should look like.
# 
# ![image info](spyder_prompt.JPG)
# 
# If you are new with Spyder/Python IDES, follow the material below to get on your way:
# If you like learning from video's, follow [these tutorials](https://docs.spyder-ide.org/current/videos/first-steps-with-spyder.html)
# If you like learning by reading along, follow [this tutorial](https://medium.com/coderbyte/spyder-python-ide-for-absolute-beginners-89e4ea1832af)

# ## Jupyter Notebooks
# 
# We will often work with jupyter notebooks in this class. To be able to open and use Jupyter Notebooks (which you can recognize with the **.ipynb** extension), we will need another program than Spyder. Luckily, your Anaconda distribution also comes with Jupyter Notebook: a way to view and edit jupyter notebooks. To open the software, run the following command in your Anaconda Prompt:
# 
# ```
# jupyter notebook
# ```
# 
# See below how it should look like:
# ![image info](jupyter_notebook_prompt.JPG)
# 
# This will open a browser page, in which you can navigate to your .ipynb file and make changes. It should look something like this:
# 
# ![image info](jupyter_notebook_browser.JPG)

# ## Using this website (Jupyter Notebooks and Google Colabs)
# Lastly, some notes on how to use this website. This website is powered by Jupyter Notebook, a web-based IDE that allows script and text to be integrated in one file. This website is built using [Jupyter Book](https://jupyterbook.org/en/stable/intro.html), which collects (amongst other things) Jupyter Notebooks in a nice book-like format. Thanks to this format, we can merge text ...

# In[1]:


print("... and Python code, all in one file!")


# This will be very useful later on, when we will guide you through Python exercises on this website. Just as Spyder, in Jupyter Notebook format you also have a place where you write code, and a place where the output is (console). Now, run the following code:

# In[2]:


age = input("What is your age? Type your age here: ")

if int(age) < 24:
    print("Wow you are young!")
elif int(age) >= 25:
    print("Nice, a real 90s kid")


# Hmmm...perhaps you are puzzled now since you are not able to run this. To be able to interact with the code blocks, you will need to start your own *interactive server*. For that, click on the rocket on the top right of your screen and choose "Colab".
# 
# ![image info](./launcher_icons.PNG)
# 
# A server will start, and you are able to interact with all the code blocks. Go do it now if you are still reading from the non-interactive website!
# 
# Now, try to run the code above, simply click on the arrow >. Importantly, the changes you make in this interactive environment **will not be automatically saved**. The easiest way to save your changes is by saving a copy on your Google Drive. If for any reason you don't want to store anything on Google Drive, you can also download your file as an .ipynb and store in on your computer. Whenever you are in a Google Colab environment, you can load in that file again. Alternatively, you can open the .ipynb file with the Jupyter Notebook software described above.

# Whenever you need to start a Google Colab server, we will make it clear with a note like the following:
# 
# > **Note**: For this part of the tutorial you will need to launch the script using Google Colab

# There are interactive elements (like multiple choice questions) for which you don't have to switch, so keep an eye out for this note before you go to Google Colab.
# 
# If you've gone through all the steps successfully you have everything ready to follow this course. Let's start!

# 
