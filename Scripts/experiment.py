#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
from itertools import combinations
from collections import defaultdict
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

niveau4 = tmp.split('\n')
niveau4 = list(filter(None, niveau4))
# print(niveau4)

model = gensim.models.Word2Vec.load('../Resultats/wv.model')
similar_neg = []
cpt = 0

for t in niveau4:
	sac_thesaurus = t.split(',')
	sac_thesaurus = list(filter(None, sac_thesaurus))
	similar = defaultdict(list)	
	if len(sac_thesaurus) > 1:
		# print('----------------------------------------------')
		# print(sac_thesaurus)
		combine = list(combinations(sac_thesaurus,2))
		for t1,t2 in combine:
			cpt += 1
			s = calcul_similar.calcul_similarity(calcul_similar.avg_feature_vector(t1.split(),model, num_features=300),calcul_similar.avg_feature_vector(t2.split(),model, num_features=300))
			"""
			if s < 0:
				print(t1,"-",t2," : ",s)
				similar_neg.append(t1+"-"+t2+" : "+str(s))
			"""
			if s != 'nan':
				similar[t1].append(s)
				similar[t2].append(s)
	for terme in similar:
		if len(similar) > 2:
			# print([vec for vec in simiar[terme] if vec < 0])
			if len(similar[terme]) == len([vec for vec in similar[terme] if vec < 0]):
				print('----------------------------------------------')
				print(terme)
				print(similar)


# print(cpt)
# print(len(similar_neg))





"""
model = gensim.models.Word2Vec.load('../Resultats/wv.model')
# l = ("Délit pénal,Peine de mort,Loi d'amnistie").split(',')
l = ("Référendum,Peine de mort,Loi d'amnistie").split(',')
l_combine = list(combinations(l,2))
for t1,t2 in l_combine:
	s = calcul_similar.calcul_similarity(calcul_similar.avg_feature_vector(t1.split(),model, num_features=300),calcul_similar.avg_feature_vector(t2.split(),model, num_features=300))
	print(t1,"-",t2," : ",s)


"""



