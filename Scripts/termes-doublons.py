import copy 

dico_doublons = {} # { expression: {level: [line_number1, line_number2]} }


with open('../Resultats/thesaurus-corpus.txt', 'r') as f:
	for linum, line in enumerate(f.readlines()):
		line = line.rstrip('\n')
		#print(linum, line)
		expression = line.strip()
		niveau = line.count('\t')
		if expression not in dico_doublons:
			dico_doublons.setdefault(expression,{})
			dico_doublons[expression][niveau] = [linum]
		else:
			if niveau not in dico_doublons[expression]:
				dico_doublons[expression][niveau] = [linum]
			else:
				dico_doublons[expression][niveau].append(linum)

di = copy.deepcopy(dico_doublons)

for item in di.keys():
	#print(di[item])
	if len(di[item]) == 1:
		#print( di[item] )
		for key in di[item]:
			#print(di[item][key])
			if len( (di[item][key]) ) == 1:
				del dico_doublons[item]

print(dico_doublons)

#print(di['Palais'])
#print(dico_doublons['Palais'])

#print(di['Pédophilie'])
#print(dico_doublons['Pédophilie'])