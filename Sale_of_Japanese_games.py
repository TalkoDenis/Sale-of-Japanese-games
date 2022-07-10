#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


games = pd.read_csv('games.csv')


# In[3]:


games.head()


# In[4]:


games.isna().sum()


# In[5]:


games = games.dropna()


# In[32]:


games['Year'] = games['Year'].astype('int')


# In[33]:


games.describe()


# In[34]:


# Показывает моду
stats.mode(games.Year)


# In[46]:


sns.countplot(games.Year)
sns.set(rc={'figure.figsize':(20,20)})
plt.title("Sale of games by years", fontsize=20)
plt.xlabel('Year', fontsize=20)
plt.ylabel('Count', fontsize=20)
plt.tick_params(axis='x', which='major', labelsize=17, rotation=45)
plt.tick_params(axis='y', labelsize=17)


# In[9]:


games.query('Year > 2007').shape


# In[10]:


games.groupby('Platform').agg('count')


# In[11]:


games.Platform.value_counts(normalize=True)*100


# In[12]:


games.head()


# In[13]:


games.groupby('Publisher').agg('count')


# In[14]:


games.Publisher.value_counts(normalize=True)


# In[16]:


stats.mode(games.Publisher)


# In[17]:


games.Publisher.value_counts()


# In[18]:


games.query('Publisher == "Nintendo"').describe()


# In[49]:


sns.boxplot(x='Genre', y='JP_Sales', data=games)
sns.set(rc={'figure.figsize':(20,20)})
plt.tick_params(axis='x', which='major', labelsize=17, rotation=45)
plt.tick_params(axis='y', labelsize=17)
plt.title("Japan games genre", fontsize=20)
plt.xlabel('Genre', fontsize=20)
plt.ylabel('Sales', fontsize=20)


# In[55]:


nintendo_games = games.query('Publisher == "Nintendo"')


# In[57]:


sns.boxplot(x='Genre', y='JP_Sales', data=nintendo_games)
sns.set(rc={'figure.figsize':(20,20)})
plt.title("Nintendo games", fontsize=20)
plt.xlabel('Genre', fontsize=20)
plt.ylabel('Sales', fontsize=20)


# In[23]:


genre_game = games.query("Genre in ('Fighting', 'Simulation', 'Platform', 'Racing', 'Sports')").groupby('Global_Sales').agg('sum')


# In[24]:


sns.lineplot(data=genre_game, x="Year", y="Rank")


# In[25]:


genre_game.head()


# In[26]:


genre_game_2 = games.query("Genre in ('Fighting', 'Simulation', 'Platform', 'Racing', 'Sports')").groupby(['Genre', 'Year']).agg('sum')


# In[27]:


genre_game_2.head()


# In[28]:


sns.lineplot(data=genre_game_2, x="Year", y="Global_Sales")


# In[ ]:





# In[ ]:




