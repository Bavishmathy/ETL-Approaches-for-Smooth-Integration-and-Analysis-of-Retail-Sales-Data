#!/usr/bin/env python
# coding: utf-8

# In[7]:


pip install mysql-connector-python


# In[8]:


import mysql.connector as sql
import pandas as pd


# In[9]:


mydb = sql.connect(
    host= "localhost",
    user = "root",
    password= "root@123",
    database= "stores"
)


# In[10]:


mycursor=mydb.cursor()


# In[11]:


query="select * FROM retail_sales"


# In[12]:


query


# In[13]:


df=pd.read_sql(query,mydb)
df


# #  Transform the data 

# In[14]:


df.fillna(0, inplace=True)
df


# In[17]:


filter_data=df[df['Total_amount']<=600]
filter_data


# In[23]:


df['transformed_column'] = df['quantity'] + 1
df


# # Load data

# In[24]:


filter_data.to_csv('target_data.csv')


# In[26]:


doc=pd.read_csv(r'target_data.csv')
doc


# In[27]:


filter_data = doc[doc['Price_per_unit']<=200]


# In[28]:


filter_data


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




