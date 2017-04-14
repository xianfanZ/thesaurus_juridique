# thesaurus_juridique

## TODO
- mettre resultats obtenus avec word2vec
- finir le rapport
    - expliquer scripts
    - evaluation qualitative des resultats
    - perspectives

## Équipe

Xianfan Zhang & Nidia Hernández

## Tâche

Normalisation du thesaurus Wolters Kluwer

## Ressources 

- Wikipedia/DBpedia
- Jurivoc (http://www.bger.ch/fr/index/juridiction/jurisdiction-inherit-template/jurisdiction-jurivoc-home.htm)

## Méthode 

1) Extraction des termes et de la hierarchie de la branche du droit francais de Wikipedia (https://fr.wikipedia.org/wiki/Portail:Droit_fran%C3%A7ais/Arborescence#Liste_des_toutes_les_cat.C3.A9gories_li.C3.A9es) 
1.1) programme de crawling avec Scrappy (juridique/spiders/test.py) pour récupérer l'arborescence des termes juridiques << problème: requêtes xpath trop longues 
1.2) idem avec Beautiful Soup (html2xml.py) << problème : balises filles avec même nom que les balises mères
1.3) DBpedia SPARQL Endpoint (requête) >> approche choisie
2) Complémentation de cette arborescence avec d'autres ressources (Jurivoc) 
3) Mise en relation de notre thesaurus avec les termes clés des sommaires et des titres (avec l'accès des données des entreprises).

## Évaluation

TODO

## Perspectives 

TODO

