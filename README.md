# thesaurus_juridique

Les étudiants rendront leur travail sous la forme d'un rapport et feront une présentation orale (10mn par groupe + 5 min de questions). Ils auront déjà commencé leur stage (en accord avec les étudiants, nous avons repoussé la date pour remettre leur travail au 14 avril) et nous allons donc prévoir un horaire compatible.
Seriez-vous disponible à 18h  sur l'une de ces dates en avril : 18, 19, 24, 25 ou 26 ?

## Équipe

Xianfan Zhang & Nidia Hernández

## Tâche

Normalisation du thesaurus Wolters Kluwer

## Ressources 

Wikipedia/DBpedia

## Méthode 

1) Extraction des termes et de la hierarchie de la branche du droit francais dede Wikipedia (https://fr.wikipedia.org/wiki/Portail:Droit_fran%C3%A7ais/Arborescence#Liste_des_toutes_les_cat.C3.A9gories_li.C3.A9es) 
1.1) programme de crawling avec Scrappy (nomdu spider.py) pour récupérer l'arborescence des termes juridiques << problème : requêtes xpath trop longues 
1.2) idem avec Beautiful Soup (html2xml.py) << problème : balises filles avec même nom que les balises mères
1.3) DBpedia SPARQL Endpoint (requête) >> approche choisie
2) Complémentation de cette arborescence avec d'autres ressources (Jurivoc) 
3) Mise en relation de notre thesaurus avec les termes clés des sommaires et des titres (avec l'accès des données des entreprises).

## Évaluation

- pertinence de la problématique
- rapport de 5 pages
- code réalisé
- résultats obtenus (qualitativement)
