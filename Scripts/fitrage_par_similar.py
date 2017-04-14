#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
from itertools import combinations
import logging,scipy,gensim.models
import calcul_similar,re

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

niveau4 = tmp.split('\n')
niveau4 = list(filter(None, niveau4))
# print(niveau4)

model = gensim.models.Word2Vec.load('../Resultats/wv.model')

for t in niveau4:
	sac_thesaurus = t.split(',')
	sac_thesaurus = list(filter(None, sac_thesaurus))
	if len(sac_thesaurus) > 1:
		print('----------------------------------------------')
		# print(sac_thesaurus)
		combine = list(combinations(sac_thesaurus,2))
		for t1,t2 in combine:
			s = calcul_similar.calcul_similarity(calcul_similar.avg_feature_vector(t1.split(),model, num_features=300),calcul_similar.avg_feature_vector(t2.split(),model, num_features=300))
			print(t1,"-",t2," : ",s)





"""
model = gensim.models.Word2Vec.load('../Resultats/wv.model')
# l = ("Délit pénal,Peine de mort,Loi d'amnistie").split(',')
l = ("Référendum,Peine de mort,Loi d'amnistie").split(',')
l_combine = list(combinations(l,2))
for t1,t2 in l_combine:
	s = calcul_similar.calcul_similarity(calcul_similar.avg_feature_vector(t1.split(),model, num_features=300),calcul_similar.avg_feature_vector(t2.split(),model, num_features=300))
	print(t1,"-",t2," : ",s)


"""



