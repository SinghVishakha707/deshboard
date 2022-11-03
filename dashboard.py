#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pywedge')


# In[2]:


import pywedge as pw
import pandas as pd


# In[5]:


df=pd.read_excel("C:\\Users\\User7\\Downloads\\US_violent_crime.xlsx")
df.head()


# In[6]:


mc=pw.Pywedge_Charts(df, c=None, y= 'Murder')


# In[7]:


charts=mc.make_charts()


# In[ ]:




