
# coding: utf-8

# In[7]:

import numpy as np


# In[8]:

import pandas as pd


# In[9]:

birddata=pd.read_csv("bird_tracking.csv")#lifewatch INBO project


# In[4]:

birddata.info()


# In[5]:

birddata.head()


# In[10]:

import matplotlib.pyplot as plt


# %matplotlib inline 

# In[11]:

bird_names=pd.unique(birddata.bird_name)


# In[12]:

bird_names


# In[13]:

import cartopy.crs as ccrs


# In[14]:

import cartopy.feature as cfeature


# In[15]:

proj = ccrs.Mercator()


# In[31]:

plt.figure(figsize=(10,10))
ax = plt.axes(projection = proj)
ax.set_extent((-25.0, 20.0,52.0,10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS,linestyle=':')

for name in bird_names:
    ix = birddata['bird_name'] == name
    x,y = birddata.longitude[ix],birddata.latitude[ix]
    ax.plot (x,y,".",transform=ccrs.Geodetic(),label=name)
plt.legend(loc="upper left")
plt.savefig("map.pdf")


# In[16]:

birddata.columns


# In[18]:

birddata.speed_2d.plot(kind='hist',range=[0,30])
plt.xlabel("2d speed")


# In[ ]:



