#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

import re

def readfile(file):
	myList = []
	with open(file,'r') as f:
		for line in f.readlines():
			line = line.rstrip('\n')
			myList.append(line)
			#print(line)
	return myList

def filter(listFilter,thesaurus):
	to_filtrer = []
	results = []
	for item in listFilter:
		for t in thesaurus:
			if re.search(item, t, re.M|re.I):
				#print(t)
				to_filtrer.append(t)
	#print(list(set(thesaurus).difference(set(to_filtrer))))
	for t in thesaurus:
		if t not in to_filtrer:
			results.append(t)
	return results
	
def main():
	thesaurus = readfile('../Resultats/extract-wiki.txt')
	# l = readfile('../Ressources/list_nationalite.txt')
	l = readfile('../Ressources/list_pays.txt')
	l.extend(readfile('../Ressources/list_nationalite.txt'))
	l.append('siècle')
	# print(l)
	# filter(l,thesaurus)
	results = filter(l,thesaurus)
	for t in results:
		print(t)

if __name__ == '__main__':
	main()
