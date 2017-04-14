import re

termes = []
with open('../Resultats/thesaurus-nettoye.txt','r') as f:
	for line in f.readlines():
		termes.append(line)
# termes = list(set(termes))


jurivoc = []
with open('../Ressources/jurivoc_fre.txt','r') as f:
	for line in f.readlines():
		line = line.strip()
		#pattern = re.compile('BT')
		if re.match('BT|NT',line):
			#print(line)
			line = re.sub('BT\s+|NT\s+','',line)
			# print(line)
			jurivoc.append(' '+line.lower()+' ')
jurivoc = list(set(jurivoc))


with open('../Resultats/corpus_concat.txt','r') as f:
	text = f.read()
	# print(text)
text1 = """
LA COUR, Par jugement contradictoire en date du 13 mars 2003, le tribunal correctionnel de GAP statuant : - sur l'action publique : a déclaré Pascal X... coupable d'avoir à GAP (05), entre le 5 août et le 22 décembre 2000, détourné, au préjudice de la CARPA, des fonds, des valeurs ou un bien, en l'espèce une somme de 628.049,36 francs (six cent vingt huit mille quarante neuf francs trente six centimes), par encaissement sur son compte personnel à la S.M.C., qui lui avait été remise à charge de la rendre ou représenter ou d'en faire un usage détermine ; faits prévus et réprimés par l'article 314-1 du Code pénal ; en répression l'a condamné à la peine d'un an d'emprisonnement assortie d'un sursis simple et à une peine d'amende de 7 500 euros ; - sur l'action civile : a déclaré irrecevable le Barreau des Hautes Alpes en sa constitution de partie civile ; a reçu la CARPA des Hautes Alpes en sa constitution de partie civile ; a déclaré Pascal X... entièrement responsable du préjudice moral de la CARPA l'a condamné à payer à celle-ci la somme de 1 500 euros à ce titre, a rejeté la demande afférente au préjudice matériel et condamné M. X... aux dépens. 
""".lower()


termes_freq = {}
sortie = ''
for t in termes:
	terme = ' '+t.strip().lower()+''
	if terme in text:
		print(terme)
		sortie += t
	# l = re.findall(terme,text,re.I)
	# if len(l) > 0:
	# 	sortie += t
	# 	termes_freq.setdefault(terme,len(l))

with open('../Resultats/thesaurus-corpus.txt','w') as f:
	f.write(sortie)



