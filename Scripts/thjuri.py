#python3

with open('../Ressources/jurivoc_fre.txt', 'r') as f:
	lignes = f.readlines()
	for ligne in lignes[300:]:
		ligne = ligne.strip()
		print(ligne)