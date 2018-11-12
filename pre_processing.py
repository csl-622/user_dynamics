# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:39:11 2018
@author: Asuspc
"""

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

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

from nltk.corpus import stopwords
stop_words = stopwords.words('english')
nlp = spacy.load('en', disable=['parser', 'ner'])

def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """https://spacy.io/api/annotation"""
    texts_out = []
    #print("texts[0] is \n", texts[0])
    text = texts[0]
    doc = nlp(" ".join(texts[0]))
    #print("doc is \n", doc)
    a = [token.lemma_ for token in doc if token.pos_ in allowed_postags]
    #print("This is a \n", a)
    return a


def pre_processing(data,id2word):
    #print(data)
    data = re.sub('\S*@\S*\s?', '', data)
    #print(data)
    data = re.sub('\s+', ' ', data)
    #print(data)
    data =re.sub("\'", "", data)
    #print(data)
    data_words = list(sent_to_words(data))
    #print(data_words)
    bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100)
    trigram = gensim.models.Phrases(bigram[data_words], threshold=100)
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram_mod = gensim.models.phrases.Phraser(trigram)
    data_words_nostops = remove_stopwords(data_words)
    data_words_bigrams = make_bigrams(data_words_nostops,bigram_mod)
    data_lemmatized = lemmatization(data_words, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
    #print(data_lemmatized)
    #id2word = corpora.Dictionary(data_lemmatized)
    texts = data_lemmatized
    corpus = [id2word.doc2bow(texts)]
    return id2word, corpus, texts


def sent_to_words(sentences):
    yield(gensim.utils.simple_preprocess(str(sentences), deacc=True))

def remove_stopwords(texts):
    return [word for word in simple_preprocess(str(texts)) if word not in stop_words]

def make_bigrams(texts,bigram_mod):
    return bigram_mod[texts]

def make_trigrams(texts,trigram_mod):
    return trigram_mod[bigram_mod[doc]]





    
    
    
    