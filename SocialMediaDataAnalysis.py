#!/usr/bin/env python
# coding: utf-8

# # Clean & Analyze Social Media

# ## Introduction
# 
# Social media has become a ubiquitous part of modern life, with platforms such as Instagram, Twitter, and Facebook serving as essential communication channels. Social media data sets are vast and complex, making analysis a challenging task for businesses and researchers alike. In this project, we explore a simulated social media, for example Tweets, data set to understand trends in likes across different categories.
# 
# ## Prerequisites
# 
# To follow along with this project, you should have a basic understanding of Python programming and data analysis concepts. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - Matplotlib
# - ...
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`
# 
# ## Project Scope
# 
# The objective of this project is to analyze tweets (or other social media data) and gain insights into user engagement. We will explore the data set using visualization techniques to understand the distribution of likes across different categories. Finally, we will analyze the data to draw conclusions about the most popular categories and the overall engagement on the platform.
# 
# ## Step 1: Importing Required Libraries
# 
# As the name suggests, the first step is to import all the necessary libraries that will be used in the project. In this case, we need pandas, numpy, matplotlib, seaborn, and random libraries.
# 
# Pandas is a library used for data manipulation and analysis. Numpy is a library used for numerical computations. Matplotlib is a library used for data visualization. Seaborn is a library used for statistical data visualization. Random is a library used to generate random numbers.

# In[16]:


import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns


# In[18]:


# Defining a list of categories
categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']
print (categories)


# In[19]:


# Entries count
n = 300

data = {
    'Date': pd.date_range('2021-01-01', periods=n),
    'Category': [random.choice(categories) for _ in range(n)],
    'Likes': np.random.randint(0, 10000, size=n)
}

# Create a Data Frame
df = pd.DataFrame(data)

# Let's take the first 15 rows of data
print(df.head(15))

# Data Frame information
print("\nDataFrame Information:")
print(df.info())

# DataFrame Description
print("\nDataFrame Description:")
print(df.describe())

# Count of each Category element
categories_count = df['Category'].value_counts() 
print("\nCategory - Count")
print(categories_count)


# In[28]:


# Dropping all data that has a value of Null
new_df = df.dropna()
print(new_df)

# Dropping duplicates
new_df = new_df.drop_duplicates()
print("----")

# Changing Date category to actual date-time
new_df['Date'] = pd.to_datetime(new_df['Date'])
print(new_df)

# Convert 'Likes' field to integer
new_df['Likes'] = new_df['Likes'].astype(int)


# Creating a histogram
sns.histplot(new_df['Likes'])
plt.show()

# Creating a boxplot
sns.boxplot(new_df, x=new_df['Category'], y=new_df['Likes'])
plt.show()

# Mean Likes
likes_mean = new_df['Likes'].mean()
print("Mean of 'Likes' category:", likes_mean)

# Category Likes
category_like = new_df.groupby('Category')['Likes'].mean()
print(category_like)

