#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re, string, unicodedata
import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import inflect
import contractions


# In[2]:


data1 = pd.read_csv('US.csv')


# In[3]:


data1.head()


# In[4]:


len(data1)


# In[5]:


job_location1 = ""
for p_location1 in data1['job_location']:
    if p_location1 != 'NONE':
        job_location1 += p_location1 + ' '


# In[6]:


job_title1 = pd.DataFrame(data1['job_title'])
JT1 = job_title1.applymap((lambda x: "_".join(x.split()) if type(x) is str else x)) 
Job_Title1 = ""
a = ' '
for p_title1 in JT1['job_title']:
    if p_title1 != 'NONE':
        Job_Title1 += p_title1 + a


# In[7]:


jt = Job_Title1.lower()
jt = re.sub("-", "", jt) # delete the content in parentheses
jt = re.sub(u"\\(.*?\\)", "", jt) # delete the content in parentheses
jt = re.sub('/', '_', jt)
jt = re.sub('&', '', jt )
jt = re.sub('\+', '', jt)
jt = re.sub('\$', '', jt)
jt = re.sub('\#', '', jt)
jt = re.sub('/*', '', jt)
jt = re.sub('®', '', jt)
jt = re.sub('/*', '', jt)
jt = re.sub('•', '', jt)
jt = re.sub('%', '', jt)
jt = re.sub('@', '', jt)
jt = re.sub(',', '', jt)


# In[8]:


job_information1 = ""
for p_information1 in data1['job_information']:
    if p_information1 != 'NONE':
        job_information1 += p_information1 + ' '


# In[9]:


def replace_contractions(text):
    """Replace contractions in string of text"""
    return contractions.fix(text)

job_information = replace_contractions(job_information1)


# In[10]:


jd = job_information.lower()
jd = re.sub("-", "", jd) # delete the content in parentheses
jd = re.sub(u"\\(.*?\\)", " ", jd) # delete the content in parentheses
jd = re.sub('\n', ' ', jd)  # delete \n
jd = re.sub(r'[a-zA-z]+://[^\s]*', '', jd) # delete website address 
jd = re.sub('[0-9]', '', jd)
jd = re.sub('\+', '', jd)
jd = re.sub('&', '', jd)
jd = re.sub('/', '', jd)
jd = re.sub('\$', '', jd)
jd = re.sub('\#', '', jd)
jd = re.sub('/*', '', jd)
jd = re.sub('®', '', jd)
jd = re.sub('/*', '', jd)
jd = re.sub('•', '', jd)
jd = re.sub('%', '', jd)
jd = re.sub('@', '', jd)
jd = re.sub('!', '', jd)
jd = re.sub('\?', '', jd)
jd = re.sub(':', '', jd)
jd = re.sub('·', '', jd)
jd = re.sub(';', '', jd)


# In[11]:


total1 = jt + ' '+ jd + ' ' + job_location1


# In[12]:


# Preparing the dataset
all_sentences = nltk.sent_tokenize(total1)
all_words = [nltk.word_tokenize(sent) for sent in all_sentences]


# In[13]:


for i in range(len(all_words)):
    all_words[i] = [w for w in all_words[i] if w not in stopwords.words('english')]


# In[38]:


word2vec = Word2Vec(all_words, window=700,min_count=2)
vocabulary = word2vec.wv.vocab
print(len(vocabulary))


# In[39]:


from gensim.models import Word2Vec, KeyedVectors   
word2vec.wv.save_word2vec_format('word2vec_us_700.bin', binary=True)


# In[19]:


# word2vec.wv.most_similar(['python'])


# In[ ]:



        

        

