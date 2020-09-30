#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import string
import nltk
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)
import tweepy
import csv 
import sqlite3 
conn=sqlite3.connect('storage1.db')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


c=conn.cursor()
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS maintable(un TEXT,id INTEGER, tweet TEXT)")


# In[9]:


auth = tweepy.OAuthHandler('P02ejYHS2vyZBlujssjukMNQE', 'WrZ3nE7CoNOoIhVxfTL9XA5ZfEa7lSJ8BpOcgwdghu4WT0KWVT')
auth.set_access_token('1002490053237596162-yowJ0B9wvHkBXMURgQACySx1jovSx4', 'pd5SiJ3sWNvI43jp2uTe02qMLJQ5wkya6Avi475L7k0en')
api = tweepy.API(auth)


# In[10]:




def remove_pattern(input_txt):
    r = re.findall("@[\w]*", input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
        
    return input_txt  

def strip_emoji(text):
    RE_EMOJI = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    return RE_EMOJI.sub(r'', text)

class StreamListener(tweepy.StreamListener):
    count=0
   
    create_table()
    def on_status(self, status):
        
        
       
      
        s=str(status.text)
        
         
            
        s1=remove_pattern(s)
     
        s3=s1.lower()
        
        a=status.user.screen_name
        print(a)
        b=status.id
        c.execute("INSERT INTO maintable (un,id,tweet) VALUES (?,?,?)",(a,b,s3))  
        conn.commit()
        
        print(status.text)
        self.count+=1
        if self.count==99:
            c.execute("INSERT INTO maintable (un,id,tweet) VALUES (?,?,?)",('TestBot40291878',0,'I hate myself. LIFE SUCKSSS I, wanna kill myself [test_keyword]'))
            conn.commit()
            return False
            
  
      
        
      
    def on_error(self, status_code):
        if status_code == 420:
            
            return False
            c.close()
            conn.close()
    


# In[ ]:





# In[11]:


stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["test_keyword","wanna","kill","die"])


# In[12]:


conn=sqlite3.connect('storage1.db')
c=conn.cursor()
sql1=" SELECT * FROM maintable"
with open('csvstore1.csv','w',encoding="utf-8") as csvfile:
    
    cwriter=csv.writer(csvfile)
    cwriter.writerow(('un','id','tweet'))
    
   
    c.execute(sql1)
    for row in  c.fetchall():
        cwriter.writerow(row)
   
 
    c.close()
    conn.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




