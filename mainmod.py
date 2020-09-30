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
c=conn.cursor()
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS maintable(un TEXT,id INTEGER, tweet TEXT)")
auth = tweepy.OAuthHandler('P02ejYHS2vyZBlujssjukMNQE', 'WrZ3nE7CoNOoIhVxfTL9XA5ZfEa7lSJ8BpOcgwdghu4WT0KWVT')
auth.set_access_token('1002490053237596162-yowJ0B9wvHkBXMURgQACySx1jovSx4', 'pd5SiJ3sWNvI43jp2uTe02qMLJQ5wkya6Avi475L7k0en')
api = tweepy.API(auth)
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
    
 

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["test_keyword","wanna","kill","die"])

conn=sqlite3.connect('storage1.db')
c=conn.cursor()
sql1=" SELECT * FROM maintable"
with open('csvstore1.csv','w',encoding="utf-8") as csvfile:
    
    cwriter=csv.writer(csvfile)
    cwriter.writerow(('un','id','tweet'))
    
   
    c.execute(sql1)
    for row in  c.fetchall():
        cwriter.writerow


# In[ ]:


import re
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import string
import nltk
import json
import csv
import tweepy
from nltk.corpus import stopwords
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)
from wordcloud import WordCloud
from textblob import TextBlob
sterms=['suicide', 'suicidal','hate']
sphrase=["killing myself","like dying","wish i was dead","wish to die"," wishing for death","kill myself"]
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


auth = tweepy.OAuthHandler('P02ejYHS2vyZBlujssjukMNQE', 'WrZ3nE7CoNOoIhVxfTL9XA5ZfEa7lSJ8BpOcgwdghu4WT0KWVT')
auth.set_access_token('1002490053237596162-yowJ0B9wvHkBXMURgQACySx1jovSx4', 'pd5SiJ3sWNvI43jp2uTe02qMLJQ5wkya6Avi475L7k0en')
api = tweepy.API(auth)


# In[ ]:


colnames = ['un', 'id', 'tweet']
data = pd.read_csv('csvstore1.csv', names=colnames)
tweet_list=data.tweet.tolist()
'''print(tweet_list)'''


# In[ ]:


def stermcheck(tb):
    for word in tb.words:
        for w in sterms:
            if (word==w):
                return True 
def sphrasecheck(to):
    val=-1
    for phrase in sphrase:
        val=to.find(phrase)
        if(val>-1):
            return True
            break


# In[ ]:


count=1
for tweetobj in tweet_list:
    print(tweetobj)
    count+=1
    analysis = TextBlob(tweetobj)

    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
        print ('Positive')
    else:
        print ('Negative')
        if stermcheck(analysis)or(sphrasecheck(tweetobj)):
            print('found')
            col_list = ["un"]
            df = pd.read_csv("csvstore1.csv")
            print (df.loc[count-3,'un'])
            """user_check(df.loc[count,'un'])"""
    print("")


    


# In[ ]:



def user_check(username='TestBot40291878'):
    tweets = api.user_timeline(screen_name=username)
    i=1
    wocl_coll=''

    for tweet in tweets:
        
        i+=1
        analysis = TextBlob(tweet.text)
        print(tweet.text.lower())
        wocl_coll+=tweet.text.lower()
        
        print(analysis.sentiment)
        if analysis.sentiment[0]>0:
            print ('Positive')
        else:
            print ('Negative')
            stermcheck(analysis)
            print("")
        if(i==5):
            wordcl(wocl_coll)
            break;

user_check() 


# In[ ]:


def wordcl(wcc):

    final_wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='black', 
                stopwords = set(stopwords.words('english')), 
                min_font_size = 10).generate( wcc)

    plt.figure(figsize = (10, 10), facecolor = None) 

    plt.imshow(final_wordcloud) 

    plt.axis("off") 

    plt.tight_layout(pad = 0) 
    plt.show()


# In[ ]:




