#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv("planets.csv")


# In[5]:


print(df.describe())


# In[8]:


df.dtypes()


# In[9]:


print(df['st_rad'].value_counts())


# In[13]:


df.drop(['pl_orbsmax','pl_bmassprov'])


# In[15]:


df.columns


# In[20]:


df2=df.drop(['pl_orbsmax', 'pl_orbsmaxerr1', 'pl_orbsmaxerr2', 'pl_orbsmaxlim',
       'pl_orbeccen', 'pl_orbeccenerr1', 'pl_orbeccenerr2', 'pl_orbeccenlim',
       'pl_orbincl', 'pl_orbinclerr1', 'pl_orbinclerr2', 'pl_orbincllim',
       'pl_bmassj', 'pl_bmassjerr1', 'pl_bmassjerr2', 'pl_bmassjlim',
       'pl_bmassprov', 'pl_radj', 'pl_radjerr1', 'pl_radjerr2', 'pl_radjlim',
       'pl_dens', 'pl_denserr1', 'pl_denserr2', 'pl_denslim', 'pl_ttvflag',
       'pl_kepflag', 'pl_k2flag', 'pl_nnotes'],axis=1)


# In[18]:


df.columns


# In[21]:


print(df2)


# In[23]:


df2=df2.drop(['pl_orbperlim','st_optmaglim','st_optmagblend','st_tefflim','st_teffblend','st_masslim','st_massblend','st_radlim','st_radblend'],axis=1)


# In[24]:


print(df2)


# In[25]:


df2.columns


# In[27]:


df2=df2.drop(['st_optmagerr'],axis=1)


# In[28]:


df2.describe()


# In[29]:


df3=df2.dropna()


# In[31]:


print(df3)


# In[32]:


df3.to_csv("cleanData1.csv")


# In[33]:


df2.interpolate()


# In[36]:


df4=df2.interpolate()


# In[37]:


df4.isnull()


# In[38]:


df4.to_csv("cleanData2.csv")


# In[39]:


df4=df4.drop(['st_distlim'],axis=1)


# In[41]:


df4.to_csv("cleanData2.csv")


# In[42]:


df3=df3.drop(['st_distlim'],axis=1)


# In[43]:


df3.to_csv("cleanData1.csv")


# In[47]:


df4=df4.fillna(method='pad')


# In[48]:


df4.to_csv("cleanData2.csv")


# In[52]:


df4=df4.drop(['rowid','rowupdate'],axis=1)


# In[53]:


df4.columns


# In[55]:


df4.to_csv('cleanData2.csv')


# In[66]:


x = df4[['pl_orbper']].values.astype(float)


# In[58]:


min_max_scaler = preprocessing.MinMaxScaler()


# In[59]:


from sklearn import preprocessing


# In[67]:


x = df4[['pl_orbper']].values.astype(float)


# In[68]:


min_max_scaler = preprocessing.MinMaxScaler()


# In[69]:


x_scaled = min_max_scaler.fit_transform(x)


# In[70]:


df5= pd.DataFrame(x_scaled)


# In[71]:


df5.plot(kind='bar')


# In[72]:


print(df5)


# In[73]:


df4['pl_name'] = df['pl_hostname'].str.cat(df['pl_letter'],sep=" ")


# In[74]:


print(df4)


# In[75]:


df4.drop(['pl_hostname','pl_letter'],axis=1)


# In[76]:


df4.columns


# In[77]:


df4=df4[['pl_name','pl_hostname', 'pl_letter', 'pl_discmethod', 'pl_pnum', 'pl_orbper',
       'pl_orbpererr1', 'pl_orbpererr2', 'ra_str', 'ra', 'dec_str', 'dec',
       'st_dist', 'st_disterr1', 'st_disterr2', 'st_optmag', 'st_optband',
       'st_teff', 'st_tefferr1', 'st_tefferr2', 'st_mass', 'st_masserr1',
       'st_masserr2', 'st_rad', 'st_raderr1', 'st_raderr2']]


# In[78]:


print(df4)


# In[79]:


df4=df4.drop(['pl_hostname', 'pl_letter'],axis=1)


# In[80]:


df4.to_csv('cleanData2.csv')


# In[ ]:




