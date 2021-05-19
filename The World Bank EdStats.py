#!/usr/bin/env python
# coding: utf-8

# #         The World Bank EdStats Data Analysis

# The World Bank EdStats All Indicator Query holds over 4,000 internationally comparable indicators that describe education access, progression, completion, literacy, teachers, population, and expenditures. The indicators cover the education cycle from pre-primary to vocational and tertiary education.The query also holds learning outcome data from international and regional learning assessments (e.g. PISA, TIMSS, PIRLS), equity data from household surveys, and projection/attainment data to 2050.

# With 189 member countries, staff from more than 170 countries, and offices in over 130 locations, the World Bank Group is a unique global partnership: five institutions working for sustainable solutions that reduce poverty and build shared prosperity in developing countries.

# The World Bank Group works in every major area of development. They provide a wide array of financial products and technical assistance, and they help countries share and apply innovative knowledge and solutions to the challenges they face.

# __Topics:__ Education, Gender
# 
# __Granularity:__ National
# 
# __Geographical Coverage:__ World East Asia & Pacific American Samoa Australia Brunei Darussalam Cambodia China Fiji French Polynesia Guam Hong Kong SAR, China Indonesia Japan Kiribati Korea, Dem. People's Rep. Korea, Rep. Lao PDR Macao SAR, China Malaysia Marshall Islands Mongolia Myanmar Nauru New Caledonia New Zealand Northern Mariana Islands Palau Papua New Guinea Philippines Samoa Singapore Solomon Islands Thailand Timor-Leste Tonga Tuvalu Vanuatu Vietnam Europe & Central Asia Albania Andorra Armenia Austria Azerbaijan Belarus Belgium Bosnia and Herzegovina Bulgaria Croatia Cyprus Czech Republic Denmark Estonia Faroe Islands Finland France Georgia Germany Gibraltar Greece Greenland Hungary Iceland Ireland Isle of Man Italy Kazakhstan Kyrgyz Republic Latvia Liechtenstein Lithuania Luxembourg Moldova Monaco Montenegro Netherlands North Macedonia Norway Poland Portugal Romania Russian Federation San Marino Serbia Slovak Republic Slovenia Spain Sweden Switzerland Tajikistan Turkey Turkmenistan Ukraine United Kingdom Uzbekistan Latin America & Caribbean Antigua and Barbuda Aruba Argentina Bahamas, The Barbados Belize Bolivia Brazil Cayman Islands Chile Costa Rica Colombia Cuba Curaçao Dominica Dominican Republic Ecuador El Salvador Grenada Guatemala Guyana Haiti Honduras Jamaica Mexico Nicaragua Panama Paraguay Peru Puerto Rico Sint Maarten (Dutch part) St. Kitts and Nevis St. Martin (French part) St. Lucia St. Vincent and the Grenadines Suriname Trinidad and Tobago Turks and Caicos Islands Uruguay Venezuela, RB Virgin Islands (U.S.) Middle East & North Africa Algeria Bahrain Egypt, Arab Rep. Djibouti Iraq Iran, Islamic Rep. Israel Jordan Kuwait Lebanon Libya Malta Morocco Oman Qatar Saudi Arabia Syrian Arab Republic United Arab Emirates Tunisia Yemen, Rep. Bermuda Canada United States South Asia Afghanistan Bangladesh Bhutan India Pakistan Nepal Maldives Sri Lanka Angola Benin Botswana Burkina Faso Burundi Cabo Verde Cameroon Central African Republic Chad Comoros Congo, Dem. Rep. Congo, Rep. Côte d'Ivoire Ethiopia Eritrea Equatorial Guinea Gabon Gambia, The Ghana Guinea Guinea-Bissau Kenya Lesotho Liberia Madagascar Malawi Mali Mauritania Mauritius Mozambique Namibia Niger Nigeria Rwanda São Tomé and Principe Seychelles Senegal Sierra Leone Somalia South Africa South Sudan Sudan Eswatini Tanzania Togo Uganda Zambia Zimbabwe
# 
# __Economy Coverage:__ High Income IBRD IDA Low Income
# 
# __Number of Economies:__ 214
# 
# __Periodicity:__ Annual
# 
# __Temporal Coverage:__ 1970 - 2100

# _________________________________________________________________________________________________________

# ## Importing liberaries

# In[102]:


import numpy as np  # linear algebra
import pandas as pd  # data processing
import matplotlib.pyplot as plt  # for Visualization
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns


# ## Reading Data

# In[103]:


Data = pd.read_csv('EdStatsData.csv')
Data.head()


# It's clear that we have a lot of missing values so cheking for more information.

#    ### MISSING values

# In[101]:


Data.info()


# __To sort the number of null value that we have for each year (decreasing)__

# In[122]:


Data.isnull().sum().sort_values(ascending=False).head(66)


# It seems like an incomplete data set. 2010, the most complete year with 644488 missing values, but there are 3665 indicators and we need to check completeness for those relevant to our problem.

# In[105]:


Data.groupby('Indicator Code').count()


# ### Checking duplicated data

# In[38]:


Data.duplicated().sum()


# ### The number of raws & columns of our Data

# In[4]:


Data.shape


# __Features of our Data__

# In[4]:


Data.columns


# In[ ]:





# In[ ]:





# ## Reading Country Data

# In[77]:


Country = pd.read_csv('C:/Users/azade/Desktop/OC/Projet 2/EdStatsCountry.csv')
Country.head()


# ### Number of missing values

# In[125]:


Country.isnull().sum().sort_values(ascending=False).head(20)


# ### Checking duplicated data

# In[85]:


Country.duplicated().sum()


# ### The number of raws & columns 

# In[86]:


Country.shape


# __Features of Country Data__

# In[21]:


Country.columns


# __Create a DF with contry_code, name, region and income_group__

# In[112]:



countries_income = pd.DataFrame({"Country_Code" : Country["Country Code"].unique(), "Name" : Country["Short Name"],
                                 "Region" : Country["Region"], "Income_group" : Country["Income Group"]})

countries_income


# we have 242 countries in our data countries

# __check how many countries we have in our Data__

# In[115]:


Data["Country Name"].describe()


# __Check how many indicators in data and for doubles__

# In[116]:


Data["Indicator Name"].describe()


# Create a file with list of countries in data

# In[117]:


countries = Data["Country Name"].unique()
countries = pd.DataFrame({"Country Name" : Data["Country Name"].unique()})
countries.to_csv("countries.csv")
print(countries)


# __Merging__ our Data with the countries_income that we have created.

# In[129]:


data_plus_country = pd.merge(Data,countries_income, left_on='Country Code', right_on='Country_Code')
data_plus_country.head()


# In[130]:


data_plus_country.info()


# In[134]:


data_plus_country.isnull().sum().sort_values(ascending= False).head(20)


# In[ ]:





# In[ ]:





# In[131]:


s1= data_plus_country.dtypes
s1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Reading Country_Series

# In[82]:


Country_Series = pd.read_csv('C:/Users/azade/Desktop/OC/Projet 2/EdStatsCountry-Series.csv')
Country_Series.head()


# ### Number of missing values in Country_Series

# In[83]:


Country_Series.isnull().sum().sort_values(ascending=False)


# ### Duplicated Country_Series Data

# In[84]:


Country_Series.duplicated().sum()


# ### The number of raws & columns 

# In[71]:


Country_Series.shape


# In[ ]:





# ## Reading FootNote Data

# In[87]:


FootNote = pd.read_csv('C:/Users/azade/Desktop/OC/Projet 2/EdStatsFootNote.csv')
FootNote.head()


# ### Number of missing values in FootNote

# In[90]:


FootNote.isnull().sum().sort_values(ascending= False)


# ### Duplicated data

# In[91]:


FootNote.duplicated().sum()


# ### The number of raws & columns 

# In[70]:


FootNote.shape


# In[ ]:





# In[ ]:





# ## Reading Series

# In[96]:


Series = pd.read_csv('C:/Users/azade/Desktop/OC/Projet 2/EdStatsSeries.csv')
Series.head()


# ### Number of missing values in Series Data

# In[97]:


Series.isnull().sum().sort_values(ascending=False)


# ### Duplicated data

# In[98]:


Series.duplicated().sum()


# ### The number of raws & columns 

# In[99]:


Series.shape


# In[ ]:





# In[23]:


Series.columns


# In[28]:


Series.shape


# In[41]:


Series.head(50)


# In[50]:


Series['Indicator Name'].value_counts()


# In[26]:


Series.drop(['Unnamed: 20','Related indicators','Other web links','Unit of measure','License Type',
             'Notes from original source','Development relevance','General comments','Limitations and exceptions',
               'Statistical concept and methodology','Aggregation method','Periodicity',
                     'Related source links','Base Period','Other notes','Short definition'],axis=1, inplace=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Q1:Which countries have a strong potential of customers for our services?

# In[ ]:




