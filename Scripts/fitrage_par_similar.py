#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
from itertools import combinations
import logging,scipy,gensim.models
import calcul_similar,re
"""
tmp = ""
char = re.compile("\w")
with open('../Resultats/thesaurus-corpus.txt','r') as f:
	lignes = [ligne for ligne in [l.strip("\n") for l in f.readlines()] if ligne]
	indexMax = len(lignes) - 1
	i = 0
	for terme in lignes:
		indentation = re.search(char,terme).start()
		if indentation == 5: 
			terme = terme.strip()
			tmp += terme+','
			# print(terme,indentation)
		else:
			tmp += '\n'
			# print('\n')
print(tmp)

niveau4 = tmp.split('\n')
niveau4 = list(filter(None, niveau4))
print(niveau4)

			termePrecedant = lignes[i-1]
			if re.search(char,termePrecedant).start == 3 :
				print('---------------')
				print(termePrecedant)
			elif re.search(char,termePrecedant).start == 4 :
				print(terme)

		i += 1

print(dico)




"""
model = gensim.models.Word2Vec.load('../Resultats/wv2.model')
# l = ("Délit pénal,Peine de mort,Loi d'amnistie").split(',')
l = ("Référendum,Peine de mort,Loi d'amnistie").split(',')
l_combine = list(combinations(l,2))
for t1,t2 in l_combine:
	s = calcul_similar.calcul_similarity(calcul_similar.avg_feature_vector(t1.split(),model, num_features=300),calcul_similar.avg_feature_vector(t2.split(),model, num_features=300))
	print(t1,"-",t2," : ",s)






