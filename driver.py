import gensim
import numpy as np
model=gensim.models.KeyedVectors.load_word2vec_format("lexvec.commoncrawl.300d.W+C.pos.vectors",binary=False)


def drive(mat):
	n=len(mat)
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
				if similarity>=100:
					tot+=1
					#print(tot)
			unique=a+b-tot
			st="similarity between topics of user "+str(i)+" and user "+str(j)
			#print(st)
			#print(tot)
			print(unique)
			tot_user_similarity+=(tot/unique)
	print("Total similarity between all users contributing to same page is ")
	print(tot_user_similarity/n)
