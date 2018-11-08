# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:34:50 2018

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
#from new_file import users_list
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
from pre_processing import pre_processing
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

df = pd.read_json('https://raw.githubusercontent.com/selva86/datasets/master/newsgroups.json')
print(df.target_names.unique())
df.head()

def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))    

def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

def make_bigrams(texts,bigram_mod):
    return [bigram_mod[doc] for doc in texts]

def make_trigrams(texts,trigram_mod):
    return [trigram_mod[bigram_mod[doc]] for doc in texts]

def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """https://spacy.io/api/annotation"""
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent)) 
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out


def getTopicForQuery (question,lda,dic):
    temp = question.lower()
    '''for i in range(len(punctuation_string)):
        temp = temp.replace(punctuation_string[i], '')

    words = re.findall(r'\w+', temp, flags = re.UNICODE | re.LOCALE)

    important_words = []
    important_words = filter(lambda x: x not in stop_words, words)'''

    ques_vec = []
    dictionary1, corpus, important_words = pre_processing(temp,dic)
    print("\n---------------------Important words are \n", len(important_words),"\n",important_words)
    #dictionary = corpora.Dictionary(important_words)
    ques_vec = dic.doc2bow(important_words)
    topic_vec = []
    print("\n----------------------------------------\nQuestion Vector is \n", len(ques_vec),"\n",ques_vec,"\n------------------------------------------\n")
    topic_vec = lda[ques_vec]
    print(topic_vec)
    for i in range(0,len(topic_vec)):
        print("\n----------------------------------------------\n",len(topic_vec[i]),"\n",topic_vec[i])
    print(len(topic_vec),len(important_words))
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
    print("\n-----\n",topic_vec[0][:][1])
    #topic = np.argmax(topic_vec[0][:][1])
    topic_vec[0].sort(key =lambda x:x[1])
    #topic_vec[0] = topic_vec[0][::-1]
    print("\nTopic is ", topic_vec[0][len(topic_vec[0])-1],"\n")
    #final = lda.print_topic(topic_vec[0][len(topic_vec[0])-1][0])
    final = lda.print_topic(topic_vec[0][len(topic_vec[0])-1][0])
    lda.print_topics(20)
    lda.show_topics(20)
    #question_topic = final.split('*') ## as format is like "probability * topic"

    return final.split('*')




data = df.content.values.tolist()
data = [re.sub('\S*@\S*\s?', '', sent) for sent in data]
data = [re.sub('\s+', ' ', sent) for sent in data]
data = [re.sub("\'", "", sent) for sent in data]
pprint(data[:1])
data_words = list(sent_to_words(data))
print(data_words[:1])

bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100)
trigram = gensim.models.Phrases(bigram[data_words], threshold=100)
bigram_mod = gensim.models.phrases.Phraser(bigram)
trigram_mod = gensim.models.phrases.Phraser(trigram)
data_words_nostops = remove_stopwords(data_words)
data_words_bigrams = make_bigrams(data_words_nostops,bigram_mod)
nlp = spacy.load('en', disable=['parser', 'ner'])
data_lemmatized = lemmatization(data_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
id2word = corpora.Dictionary(data_lemmatized)
texts = data_lemmatized
corpus = [id2word.doc2bow(text) for text in texts]

lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=10, 
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha='auto',
                                           per_word_topics=True)

doc_lda = lda_model[corpus]
print('\nPerplexity: ', lda_model.log_perplexity(corpus))
coherence_model_lda = CoherenceModel(model=lda_model, texts=data_lemmatized, dictionary=id2word, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print('\nCoherence Score: ', coherence_lda)
question = "In the 6th and 7th centuries, the first devotional hymns were created in the Tamil language.They were imitated all over India and led to both the resurgence of Hinduism and the development of all modern languages of the subcontinent.Indian royalty, big and small, and the temples they patronised drew citizens in great numbers to the capital cities, which became economic hubs as well. Temple towns of various sizes began to appear everywhere as India underwent another urbanisation"
getTopicForQuery(question,lda_model,id2word)
#getTopicForQuery(question,coherence_model_lda,id2word)


