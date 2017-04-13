 
  Contenu du directory DISK$MIC:[THESAURUS]:
  ------------------------------------------

  1) Fichiers *.DMP
 
  Ces fichiers contiennent les diff�rents th�sauri et dictionnaires en Format
  Basis-Plus (TM Free format) permettant un rechargement dans une autre
  Base de donn�es Th�saurus Basis-Plus.
 
  Ces fichiers ne contiennent pas les relations r�ciproques, car lors d'un
  rechargement dans Basis-Plus ces r�ciproques sont automatiquement g�n�r�es.
  Par contre les termes "feuilles", c'est � dire n'ayant pas de relation
  principale, peuvent appara�tre isol� (par ex.: LT  SC�NARIO). Ceci est
  particuli�rement visible dans les dictionnaires o� tous les termes de la
  langue secondaire apparaissent isol�ments (par ex.: LT  � VIE). 
 
  D�tails du contenu des fichiers:
    - JURIVOC_GER.DMP          Th�saurus en langue allemande
    - JURIVOC_FRE.DMP          Th�saurus en langue fran�aise
    - JURIVOC_ITA.DMP          Th�saurus en langue italienne
    - JURIVOC_GER_FRE.DMP      Dictionnaire allemand - fran�ais
    - JURIVOC_GER_ITA.DMP      Dictionnaire allemand - italien
    - JURIVOC_FRE_ITA.DMP      Dictionnaire fran�ais - italien
  (NB: Les fichiers JURIVOC_xxx_TAG.DMP contiennent des termes Tags et ne
  sont en principe pas utile). 
 
 
  2) Fichiers *.DOC
 
  Ces fichiers contiennent les diff�rents th�sauri et dictionnaires en Format
  textuel agr�able � lire. Elle peuvent �tre relu dans n'importe quel
  traitement de texte (Word, ...), utiliser de pr�f�rence une police de
  caract�res � chasse fixe pour obtenir un alignement correct des termes.
 
    - JURIVOC_GER.DOC          Th�saurus en langue allemande
    - JURIVOC_FRE.DOC          Th�saurus en langue fran�aise
    - JURIVOC_ITA.DOC          Th�saurus en langue italienne
    - JURIVOC_GER_FRE.DOC      Dictionnaire allemand-fran�ais
    - JURIVOC_FRE_GER.DOC      Dictionnaire fran�ais-allemand
    - JURIVOC_GER_ITA.DOC      Dictionnaire allemand-italien
    - JURIVOC_ITA_GER.DOC      Dictionnaire italien-allemand
    - JURIVOC_FRE_ITA.DOC      Dictionnaire fran�ais-italien
    - JURIVOC_ITA_FRE.DOC      Dictionnaire italien-fran�ais


  3) Les relations et leurs r�ciproque:

     Dans les dictionnaires:

	- GER    Relation de traduction vers l'allemand
  - FRE    Relation de traduction vers le fran�ais
	- ITA    Relation de traduction vers l'italien

     Dans les th�sauri:

	Relations	R�ciproque	Signification

	- LT		n-a*		Lead Term
					(Terme principal pour les relations
					suivantes)
	- NT            BT              Narrow Term / Broad Term
					(Hierarchie des termes).
	- COM           n-a         	Commentaire interne du groupe th�saurus.
 	- SA01 � SA40	n-a	        See Also (Siehe Auch)
             				(relations non standard en remplacement
					de RT = Related Term).
	- SN		n-a		Scope Note.
					(note explicative, d�finition,
			  		indication d'utilisation).
	- UF 		USE		Used for / Use
					synonyme ou quasi-synonyme.
	- USA		UFA             use ... and ... / used for ... and ...
					renvoi � une combinaison de 
					descripteurs.

	* n-a = non-applicable (not available)


     (Cr�ation: voir BRATHES$COM:DUMP_JURIVOC.COM et PRINT_JURIVOC.COM)

	TFL-DyO / 8.09.1999

