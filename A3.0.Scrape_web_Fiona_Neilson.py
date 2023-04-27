#!/usr/bin/env python
# coding: utf-8

# # Scrape Youtube Comments with Selenium and Python - sample

# The aim of this file is to scrape comments from a YouTube video using Selenium, turn them into a dataframe and ouptut an XLSX file.

# **Video Title:** Pakistan’s Hazara women turn to Chinese martial arts for self-defence despite cultural norms

# In[1]:


# provide output filename
ref = '01.H1'
# provide the URL
url = 'https://www.youtube.com/watch?v=owHswMmexaw&t=17s'


# In[2]:


# import required libraries
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[3]:


# 
data=[]

with Chrome(executable_path=r'C:\Program Files\chromedriver.exe') as driver:
    wait = WebDriverWait(driver,15)
    driver.get(url)   
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 200);") #triggers comments load in Chrome browser
    

    for item in range(57): # specify number of 'End' button clicks
        time.sleep(5) # 5 second delay
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
                
    comments = driver.find_elements(By.CSS_SELECTOR, "#comment-content")
    
    for comment in comments:
        data.append(comment.text)  


# In[11]:


data


# In[4]:


import pandas as pd   
df = pd.DataFrame(data, columns=['comment'])
df.head()


# In[5]:


len(df)


# In[6]:


# add filename to output and download
df.to_excel(f'{ref}.xlsx', index=False)


# In[7]:


# check df
df


# In[ ]:




