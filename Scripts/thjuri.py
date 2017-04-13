#python3

with open('jurivoc_fre-ok.txt', 'r') as f:
	lignes = f.readlines()
	for ligne in lignes[300:]:
		ligne = ligne.strip()
		print(ligne)