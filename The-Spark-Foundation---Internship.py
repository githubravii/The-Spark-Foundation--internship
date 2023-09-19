#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis - Retail
# ### Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’
# 
# ### As a business manager, try to find out the weak areas where you can work to make more profit.
# 
# ### What all business problems you can derive by exploring the data?
# 
# ### I used Python to perform EDA on this dataset.
# 
# ### Dataset: https://bit.ly/3i4rbWl
# 
#                                          

# In[2]:


import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')


# In[8]:


df = pd.read_csv("SampleSuperstore (1).csv")


# # Basic Data Insights

# In[9]:


df.sample(5)


# In[10]:


df.head()


# In[11]:


df.tail()


# In[12]:


df.shape


# In[13]:


df.info()


# In[14]:


df.describe()


# # Number of unique values in each column

# In[15]:


for i in df.columns:
    print(i,len(df[i].unique()))


# # Check for null values
# 

# In[16]:


df.isnull().sum()


# # Data Visualization

# In[17]:


sns.pairplot(df)


# In[18]:


fig,axes = plt.subplots(1,1,figsize=(12,7))
sns.heatmap(df.corr())
plt.show()


# In[19]:


fig,axes = plt.subplots(1,2,figsize=(14,5))
fig.suptitle("Total profit VS sales ")
sns.barplot(data=df.groupby('Sub-Category')['Sales','Profit'].agg(sum),x='Sales',y='Profit',ax=axes[1])
df.groupby('Sub-Category')['Sales','Profit'].agg(sum).plot(kind='bar',ax=axes[0])
plt.xticks(rotation=90)
plt.show()


# In[20]:


fig,axes = plt.subplots(1,2,figsize=(14,5))
fig.suptitle("Total Sales VS Quantity ")
sns.barplot(data=df.groupby('Sub-Category')['Sales','Quantity'].agg(sum),x='Sales',y='Quantity',ax=axes[1])
df.groupby('Sub-Category')['Sales','Quantity'].agg(sum).plot(kind='bar',ax=axes[0])
plt.xticks(rotation=90)
plt.show()


# In[21]:


fig,axes = plt.subplots(1,2,figsize=(14,5))
df.groupby('Sub-Category')['Discount','Profit'].agg(sum).plot(kind='bar',ax=axes[0]).set_title('Discount & Profit Relation based on Sub-Category')
df.groupby('Sub-Category')['Profit','Quantity'].agg(sum).plot(kind='bar',ax=axes[1]).set_title('Quantity & Profit Relation based on Sub-Category')
plt.xticks(rotation=90)
plt.show()


# In[22]:


fig,axes = plt.subplots(2,2,figsize=(16,8))
fig.suptitle("Distribution plots", fontsize=16)
sns.distplot(df['Sales'],ax=axes[0,0])
sns.distplot(df['Profit'],ax=axes[0,1])
sns.distplot(df['Discount'],ax=axes[1,0])
sns.distplot(df['Quantity'],ax=axes[1,1])
plt.show()


# In[30]:


fig,axes = plt.subplots(2,2,figsize=(16,8))
fig.suptitle("Sales with different shipping modes and Segments", fontsize=18)
sns.barplot(df['Ship Mode'],df['Sales'],ax=axes[0,0])
sns.lineplot(df['Ship Mode'],df['Sales'],ax=axes[0,1])
sns.barplot(df['Segment'],df['Sales'],ax=axes[1,0])
sns.lineplot(df['Segment'],df['Sales'],ax=axes[1,1])
plt.show()


# In[31]:


fig,ax= plt.subplots(1,1,figsize=(12,7))
sns.countplot(df['Quantity'],hue=df['Region'])
plt.show()


# # Some important Findings
# ### * The features Profit and Discounts are highly related.
# ### * Over Less quantity of products also the sales were high.
# ### * The maximum quantity of product in demand was in range 2-4.
# ### * The mode of shipping doesn't affect much to the sales
# ### * The Home Office provides highest sales followed by Corporate by a slight variation 
# 
# ## * Thank You :)
# 

# In[ ]:




