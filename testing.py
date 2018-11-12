# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:34:50 2018
@author: Asuspc
"""
import re
import nltk
nltk.download('stopwords')
import re
import numpy as np
import pandas as pd
from pprint import pprint
import spacy
# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
#from new_file import users_list
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
from pre_processing import pre_processing
from nltk.corpus import stopwords
nlp = spacy.load('en', disable=['parser', 'ner'])
stop_words = stopwords.words('english')




def getTopicForQuery (question,lda,dic):
    temp = question.lower()
    '''for i in range(len(punctuation_string)):
        temp = temp.replace(punctuation_string[i], '')
    words = re.findall(r'\w+', temp, flags = re.UNICODE | re.LOCALE)
    important_words = []
    important_words = filter(lambda x: x not in stop_words, words)'''

    ques_vec = []
    dictionary1, corpus, important_words = pre_processing(temp,dic)
    
    #print("\n---------------------Important words are \n", len(important_words),"\n",important_words)
    
    #dictionary = corpora.Dictionary(important_words)
    ques_vec = dic.doc2bow(important_words)
    topic_vec = []
    
    #print("\n----------------------------------------\nQuestion Vector is \n", len(ques_vec),"\n",ques_vec,"\n------------------------------------------\n")
    
    topic_vec = lda[ques_vec]
    
    #print(topic_vec)
    
    #for i in range(0,len(topic_vec)):
    #    print("\n----------------------------------------------\n",len(topic_vec[i]),"\n",topic_vec[i])
    
    #print(len(topic_vec),len(important_words))
    
    '''word_count_array = np.empty((len(topic_vec), 2), dtype = np.object)
    for i in range(len(topic_vec)):
        word_count_array[i, 0] = topic_vec[i][0]
        word_count_array[i, 1] = topic_vec[i][1]
    print("Word count array is \n", word_count_array)
    idx = np.argsort(list(word_count_array.values()))
    idx = idx[::-1]
    word_count_array = word_count_array[idx]'''

    final = []
    #final = lda.print_topic(word_count_array[0, 0], 1)
    
    #print("\n-----\n",topic_vec[0][:][1])
    
    #topic = np.argmax(topic_vec[0][:][1])
    topic_vec[0].sort(key =lambda x:x[1])
    #topic_vec[0] = topic_vec[0][::-1]
    #print("\nTopic is ", topic_vec[0][len(topic_vec[0])-1],"\n")
    #final = lda.print_topic(topic_vec[0][len(topic_vec[0])-1][0])
    final = lda.print_topic(topic_vec[0][len(topic_vec[0])-1][0])
    lda.print_topics(20)
    lda.show_topics(20)
    #question_topic = final.split('*') ## as format is like "probability * topic"
    #print(final)
    a=re.findall(r"[a-zA-Z']+",final)
    #a=final.split('*')
    #print(a)
    return a





#getTopicForQuery(question,coherence_model_lda,id2word)

    