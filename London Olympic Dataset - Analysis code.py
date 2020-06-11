#!/usr/bin/env python
# coding: utf-8

# <img src="http://cfs22.simplicdn.net/ice9/new_logo.svgz "/>
# 
# # Assignment 02: Evaluate the Summer Olympics, London 2012 dataset
# 
# *The comments/sections provided are your cues to perform the assignment. You don't need to limit yourself to the number of rows/cells provided. You can add additional rows in each section to add more lines of code.*
# 
# *If at any point in time you need help on solving this assignment, view our demo video to understand the different steps of the code.*
# 
# **Happy coding!**
# 
# * * *

# #### 1: View and add the dataset

# In[7]:


#Import the necessary library
import numpy as np


# In[8]:


#Manually add the Summer Olympics, London 2012 dataset as arrays
countries    = np.array(["Great Britain","China","Russia","United States","Korea","Japan","Germany"])
country_code = np.array(["GBR","CHN","RUS","US","KOR","JPN","GER"])
year         = 2012
gold         = np.array([29,38,24,46,13,7,11])
silver       = np.array([17,28,25,28,8,14,11])
bronze       = np.array([19,22,32,29,7,17,14])


# #### Find the country with maximum gold medals

# In[9]:


#Use the argmax() method to find the highest number of gold medals
#country_max_gold = gold.argmax()
country_max_gold = countries[gold.argmax()]


# In[10]:


#Print the name of the country
print(country_max_gold)


# #### Find the countries with more than 20 gold medals

# In[11]:


#Use Boolean indexing technique to find the required output
more_than_20 = gold>20
print(countries[more_than_20])


# #### Evaluate the dataset and print the name of each country with its gold medals and total number of medals

# In[48]:


#Use a for loop to create the required output
for i in range(len(countries)):
    total_medals= gold[i]+silver[i]+bronze[i]
    print('{} has got {} gold medals and total medals is {}'.format(countries[i],gold[i],total_medals))

