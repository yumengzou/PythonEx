
# coding: utf-8

# In[8]:

import glob, os, re, math
import matplotlib.pyplot as plt
import numpy as np
get_ipython().magic(u'matplotlib inline')


# In[2]:

def tokenize(text):
    ans=text.split()
    punctuations=",.?!\"\':;-"
    ans=[s.strip(punctuations).lower() for s in ans]
    return ans


# In[4]:

def chunk(lst, n, overlap=False):
    if overlap==False:
        overlap=n
    index=range(0,len(lst),overlap)
    ans=[lst[i:i+n] for i in index]
    return ans


# In[1]:

def text_freq(path):
    
    ## create a corpus
    filenames=glob.glob(path)
    corpus=[tokenize(open(f,'r').read()) for f in filenames]
    
    ## build a dictionary of tokens
    tf={}
    for text in corpus:
        for token in text:
            if token in tf:
                tf[token]+=1
            else:
                tf[token]=1
    return tf


# In[6]:

def doc_freq(path):
    
    ## build corpus: list of list of strings
    filenames=glob.glob(path)
    corpus=[tokenize(open(f,'r').read()) for f in filenames]
    
    ## create dictionary with document frequency
    doc_freq={}
    for text in corpus:
        text=set(text) 
        for wd in text:
            if wd in doc_freq.keys():
                doc_freq[wd]+=1
            else:
                doc_freq[wd]=1
                    
    return doc_freq


# In[7]:

def vectorize(features, text):
    ans=[]
    for flst in features:
        regex="|".join(flst)
        count=len([wd for wd in text if re.match(regex,wd)])
        ans.append(count/(float)(len(text)))
    return ans


# In[10]:

def tf_idf (flpath, crpath):
    
    tf_dict=text_freq(flpath)
    df_dict=doc_freq(crpath)
    
    score={}
    for wd in tf_dict.keys():
        score[wd]=tf_dict[wd]*math.log(36.0/df_dict[wd])
    
    return score


# In[11]:

def distance(c1,c2):
    ans=0
    for i, v in enumerate(c1):
        ans+=(v-c2[i])**2
    ans=ans**.5
    return ans 


# In[12]:

def type_token(text):
    ans=len(set(text))/(float)(len(text))
    return ans


# In[ ]:



