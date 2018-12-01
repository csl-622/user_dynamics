import gensim
import numpy as np
import nltk
nltk.download('words')
model=gensim.models.KeyedVectors.load_word2vec_format("lexvec.commoncrawl.300d.W+C.pos.vectors",binary=False)

words = set(nltk.corpus.words.words())

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

def filter(list_of_topics):
    for user_topics in list_of_topics:
        for topic in user_topics:
            if topic.lower() not in words or not topic.isalpha():
                user_topics.remove(topic)
    return list_of_topics

def remove_stopwords(list_of_topics):
    for user_topics in list_of_topics:
        for topic in user_topics:
            if topic in stop_words:
                user_topics.remove(topic)
    return list_of_topics


def drive(mat):
	mat = filter(mat)
	mat = remove_stopwords(mat)
	n=len(mat)
	print("No. of contributors for this page:-"+str(n))
	print("Topics generated for all these users are: ")
	for i in range(n):
		print(mat[i])
	tot_user_similarity=0.0
	for i in range(n-1):
		for j in range(i+1,n):
			tot=0
			a=len(mat[i])
			b=len(mat[j])
			mm=min(a,b)
			#print(mm)
			for k in range(mm):
				#print(mat[i][k])
				#print(mat[j][k])
				similarity=np.dot(model[mat[i][k]],model[mat[j][k]])
				if similarity>=70:
					tot+=1
					#print(tot)
			unique=a+b-tot
			st="similarity between topics of user "+str(i)+" and user "+str(j)
			#print(st)
			#print(tot)
			#print(unique)
			tmp=tot/unique
			#print(tmp)
			tot_user_similarity+=tmp
	print("Total similarity between all users contributing to same page or The User Similarity coefficient is ")
	print(tot_user_similarity/n)
