#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


#read in 2021 WHR data
df_2021 = pd.read_csv("WHR-2021.csv")
df_2021.head()


# In[4]:


#read in 2020 WHR data
df_2020 = pd.read_csv("WHR-2020.csv")
df_2020.head()


# In[5]:


#read in 2019 WHR data
df_2019 = pd.read_csv("WHR-2019.csv")
df_2019.head()


# In[6]:


#merging all three years: 2019, 2020, 2021
#add 2019 and label vars with year
df = pd.read_csv("WHR-2019.csv")
df = df.add_suffix("_2019")
df.head()


# In[7]:


#add 2020 and label vars with year
df = df.merge(df_2020.add_suffix("_2020"), left_on='Country or region_2019', right_on='Country name_2020')
df.head()


# In[8]:


#add 2021 and label vars with year
df = df.merge(df_2021.add_suffix("_2021"), left_on='Country or region_2019', right_on='Country name_2021')
df.head()


# In[16]:


#consolidate country column
#rename Freedom columns to be more concise
df = df.rename(columns = {"Country or region_2019":"Country"})
df = df.drop(columns = ["Country name_2020", "Country name_2021"])
df = df.rename(columns = {
    "Freedom to make life choices_2019":"Freedom_2019",
    "Freedom to make life choices_2020":"Freedom_2020",
    "Freedom to make life choices_2021":"Freedom_2021"})
df.head()


# In[18]:


#compare generosity means from 2019, 2020, 2021
g1 = df.Freedom_2019.mean()
g2 = df.Freedom_2020.mean()
g3 = df.Freedom_2021.mean()

print(g1,g2,g3) #HOW COME THEY ARE GOING UP???


# In[19]:


#create bar graph of mean generosity each year
df_freedom_means = pd.DataFrame({'year':['2019','2020','2021'], 'Mean freedom':[g1, g2, g3]})
ax = df_freedom_means.plot.bar(x='year', y='Mean freedom', rot=0)


# In[20]:


#create two new columns to capture the change in generosity scores between the years
df['Change_In_Freedom_2019_2020'] = abs(df['Freedom_2019']-df['Freedom_2020'])
df['Change_In_Freedom_2020_2021'] = abs(df['Freedom_2020']-df['Freedom_2021'])
df.head()


# In[21]:


#countries with the top generosity scores 2019
df.sort_values(by="Freedom_2019",ascending=False).Country.head()


# In[22]:


#countries with the top genersoity scores 2020
df.sort_values(by="Freedom_2020",ascending=False).Country.head()


# In[23]:


#countries with the top genersoity scores 2021
df.sort_values(by="Freedom_2021",ascending=False).Country.head()


# In[ ]:





# In[24]:


#countries with the bottom generosity scores 2019
df.sort_values(by="Freedom_2019").Country.head()


# In[25]:


#countries with the bottom generosity scores 2020
df.sort_values(by="Freedom_2020").Country.head()


# In[26]:


#countries with the bottom generosity scores 2021
df.sort_values(by="Freedom_2021").Country.head()


# In[115]:


#create line graph of top country's generosity scores each year: 
# Indonesia, Myanmar, Gambia, Haiti, Uzbekistan
#FIX
df_gen_top_countries = pd.DataFrame({
    'Indonesia': [ df[df.Country == "Indonesia"].Generosity_2019, df[df.Country == "Indonesia"].Generosity_2020, df[df.Country == "Indonesia"].Generosity_2021 ],
    'Myanmar': [ df[df.Country == "Myanmar"].Generosity_2019, df[df.Country == "Myanmar"].Generosity_2020, df[df.Country == "Myanmar"].Generosity_2021 ],
    'Gambia': [ df[df.Country == "Gambia"].Generosity_2019, df[df.Country == "Gambia"].Generosity_2020, df[df.Country == "Gambia"].Generosity_2021],      
    'Haiti': [ df[df.Country == "Haiti"].Generosity_2019, df[df.Country == "Haiti"].Generosity_2020, df[df.Country == "Haiti"].Generosity_2021],
    'Uzbekistan': [ df[df.Country == "Uzbekistan"].Generosity_2019, df[df.Country == "Uzbekistan"].Generosity_2020, df[df.Country == "Uzbekistan"].Generosity_2021]
    }, index = [2019,2020,2021])
lines = df_gen_top_countries.plot.line()


# In[27]:


#countries with most change in freedom between 2019 and 2020
df.sort_values(by="Change_In_Freedom_2019_2020",ascending=False).Country.head()


# In[28]:


#countries with most change in freedom between 2019 and 2020
df.sort_values(by="Change_In_Freedom_2020_2021",ascending=False).Country.head()


# In[61]:


df['Regional indicator_2020'].head()


# In[64]:


#create new dataset with just freedom 2020 data
data = [df['Countries'],df['Regional indicator_2020'],df['Freedom_2019'],df['Freedom_2020'],df['Freedom_2021']]
headers = ['Countries','Region','Freedom_2019','Freedom_2020','Freedom_2021']
df_freedom = pd.concat(data,axis=1,keys=headers)
df_freedom.head()


# In[82]:


df_freedom.to_csv("freedom.csv")


# In[ ]:





# In[ ]:




