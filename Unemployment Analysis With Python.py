#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


# In[2]:


data = pd.read_csv("Desktop/Unemployment.csv")
data


# In[3]:


data = data.dropna()
data.info()


# In[4]:


data[' Date'] = pd.to_datetime(data[' Date'])
data.describe()


# In[5]:


min = data[' Date'].min()
max = data[' Date'].max()
print(min,max)


# In[6]:


plt.figure(figsize=(15,5))
plt.plot(data[' Date'], data[' Estimated Unemployment Rate (%)'])
plt.xlabel('Date')
plt.ylabel('Unemployment Rate')
plt.title('Unemployment Rate in India')
plt.show()


# In[7]:


plt.figure(figsize=(15,5))
sns.lineplot(x=' Date',y = ' Estimated Unemployment Rate (%)',data=data)


# In[8]:


mean_unemployment = data[' Estimated Unemployment Rate (%)'].mean()
median_unemployment = data[' Estimated Unemployment Rate (%)'].median()
print(f'Mean Unemployment Rate: {mean_unemployment}')
print(f'Median Unemployment Rate: {median_unemployment}')


# In[10]:


rate = pd.read_csv("Desktop/Unemployment01.csv")
rate.info()


# In[11]:


plt.figure(figsize=(15,5))
plt.plot(rate[' Date'],rate[' Estimated Unemployment Rate (%)'])
plt.xlabel("Date")
plt.ylabel("Unemployment Rate")
plt.title("Unemployment rate Upto 11-2020")
plt.show()


# In[12]:


plt.figure(figsize=(15,5))
sns.lineplot(x=' Date',y = ' Estimated Unemployment Rate (%)',data=rate)


# In[13]:


mean_unemployment = rate[' Estimated Unemployment Rate (%)'].mean()
median_unemployment = rate[' Estimated Unemployment Rate (%)'].median()
print(f'Mean Unemployment Rate during Covid-19: {mean_unemployment}')
print(f'Median Unemployment Rate during Covid-19: {median_unemployment}')


# In[ ]:




