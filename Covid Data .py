#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd


# In[37]:


#upload covid-19 data
#https://www.worldometers.info/coronavirus/
df_covid = pd.read_csv("Covid_Data.csv")
df_covid.Country.head()
df_covid.Total_deaths.head()


# In[38]:


#upload covid-19 data
#https://www.worldometers.info/coronavirus/
df_freedom = pd.read_csv("freedom.csv")
df_freedom.Region.head()


# In[39]:


#merge 
df_freedom = df_freedom.merge(df_covid, left_on='Countries', right_on='Country')
df_freedom.head()


# In[40]:


df_freedom.drop(columns = ['Country'])


# In[44]:


#make scatterplot csv 
#create new dataset with freedom and covid data
data = [df_freedom['Countries'],df_freedom['Region'],df_freedom['Freedom_2019'],df_freedom['Freedom_2020'],df_freedom['Freedom_2021'],df_freedom['Total_cases'], df_freedom['Total_deaths'], df_freedom['Total_Cases_Per_1M'], df_freedom['Population']]
headers = ['Countries','Region','Freedom_2019','Freedom_2020','Freedom_2021','Total_cases','Total_deaths','Total_cases_per_1M','Population']
df_covid_freedom = pd.concat(data,axis=1,keys=headers)
df_covid_freedom.head()


# In[45]:


df_covid_freedom.to_csv("covid_freedom.csv")


# In[63]:


#for each region, what is the mean freedom score?
df_freedom.head()
Free_2019 = df_freedom.groupby(by='Region',as_index=False)['Freedom_2019'].mean()


# In[64]:


Free_2020 = df_freedom.groupby(by='Region',as_index=False)['Freedom_2020'].mean()


# In[73]:


Free_2021 = df_freedom.groupby(by='Region',as_index=False)['Freedom_2021'].mean()
Free_2021.head()


# In[74]:


#make line graph csv 
data = [Free_2019['Region'],Free_2019['Freedom_2019'], Free_2020['Freedom_2020'], Free_2021['Freedom_2021']]
headers = ['Region','Freedom_2019','Freedom_2020','Freedom_2021']
df_free_means_by_region = pd.concat(data,axis=1,keys=headers)
df_free_means_by_region.head()


# In[75]:


df_free_means_by_region.to_csv("df_free_means_by_region.csv")


# In[ ]:




