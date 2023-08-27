#!/usr/bin/env python
# coding: utf-8

# # Cardio-Good-Fitness Dataset

# # Business study - Descriptive Statistics 
# 
# #### (understanding the problem statement)
# 
# The market research team at Adright is assignes the task to identify the profile of the typical customer for each treadmill product offered by CardioGood Fitness. The market research team decides to investigate whether there are differences across the product lines with respect to customer characteristics. The team decides to collect data on individuals who purchased a treadmill at a CrdioGoodFitness retail store during the prior three months. The data are stored in the CardioGoodFitness.csv file.
# 
# The team identifies the following customer variables to study:
# - product purchased TM195, TM498 OR TM798.
# - Gender
# - Age ; in years
# - Education ; in years
# - Relationaship status ; single or married
# - Annual household income
# - Average number of time customer plans to use the treadmill each week.
# - Average number of miles the customer expects to walk/run each week.
# - and self-rated fitness on 1-5 scale, where 1 is poor shape and 5 is excellent shape.
# 

# In[4]:


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


mydata=pd.read_csv("CardioGoodFitness-1.csv")


# In[6]:


mydata.head()


# In[7]:


mydata.tail()


# In[29]:


#random observation comes
mydata.sample(16)


# In[28]:


mydata.shape #THERE ARE 180 ROWS AND 9 COLUMNS


# In[32]:


#data types of every type comes according to all the columns
mydata.dtypes


# In[33]:


mydata.info()


# In[34]:


#to know every information of our data or statistics
mydata.describe()


# In[35]:


#works for both numerical and categorical data.
#data is not distributed properly.
mydata.describe(include="all")


# In[36]:


mydata.isnull().sum()


# In[26]:


sns.boxplot(x='Age',data=mydata)


# In[39]:


sns.boxplot(x='Education',data=mydata)


# In[43]:


sns.boxplot(x='Usage',data=mydata)


# In[44]:


sns.boxplot(x='Fitness',data=mydata)


# In[45]:


sns.boxplot(x='Income',data=mydata)


# In[46]:


sns.boxplot(x='Miles',data=mydata)


# In[38]:


import warnings
warnings.filterwarnings("ignore")


# In[48]:


sns.distplot(mydata["Age"])


# In[49]:


sns.distplot(mydata["Education"])


# In[50]:


sns.distplot(mydata["Usage"])


# In[51]:


sns.distplot(mydata["Fitness"])


# In[55]:


sns.distplot(mydata["Income"])
plt.show()


# In[54]:


sns.distplot(mydata["Miles"])
plt.show()


# In[56]:


mydata.hist(figsize=(10,20))
plt.show


# In[58]:


mydata.describe(include="all").T


# In[60]:


sns.countplot(x="MaritalStatus",data=mydata)


# In[61]:


#hue is written to add another attribute
sns.countplot(x="Product",hue="Gender",data=mydata)


# In[62]:


sns.countplot(x="Product",hue="MaritalStatus",data=mydata)


# In[63]:


sns.boxplot(x="Product",y="Age",data=mydata) #one should be numerical


# In[64]:


pd.crosstab(mydata['Product'],mydata['Gender'])


# In[65]:


sns.pairplot(mydata,diag_kind='kde')


# In[8]:


corr = mydata.corr()
corr


# In[9]:


sns.heatmap(corr,annot=True)


# # END
