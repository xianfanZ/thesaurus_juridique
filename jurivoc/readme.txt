 
  Contenu du directory DISK$MIC:[THESAURUS]:
  ------------------------------------------

  1) Fichiers *.DMP
 
  Ces fichiers contiennent les différents thésauri et dictionnaires en Format
  Basis-Plus (TM Free format) permettant un rechargement dans une autre
  Base de données Thésaurus Basis-Plus.
 
  Ces fichiers ne contiennent pas les relations réciproques, car lors d'un
  rechargement dans Basis-Plus ces réciproques sont automatiquement générées.
  Par contre les termes "feuilles", c'est à dire n'ayant pas de relation
  principale, peuvent apparaître isolé (par ex.: LT  SCÉNARIO). Ceci est
  particulièrement visible dans les dictionnaires où tous les termes de la
  langue secondaire apparaissent isoléments (par ex.: LT  À VIE). 
 
  Détails du contenu des fichiers:
    - JURIVOC_GER.DMP          Thésaurus en langue allemande
    - JURIVOC_FRE.DMP          Thésaurus en langue française
    - JURIVOC_ITA.DMP          Thésaurus en langue italienne
    - JURIVOC_GER_FRE.DMP      Dictionnaire allemand - français
    - JURIVOC_GER_ITA.DMP      Dictionnaire allemand - italien
    - JURIVOC_FRE_ITA.DMP      Dictionnaire français - italien
  (NB: Les fichiers JURIVOC_xxx_TAG.DMP contiennent des termes Tags et ne
  sont en principe pas utile). 
 
 
  2) Fichiers *.DOC
 
  Ces fichiers contiennent les différents thésauri et dictionnaires en Format
  textuel agréable à lire. Elle peuvent être relu dans n'importe quel
  traitement de texte (Word, ...), utiliser de préférence une police de
  caractères à chasse fixe pour obtenir un alignement correct des termes.
 
    - JURIVOC_GER.DOC          Thésaurus en langue allemande
    - JURIVOC_FRE.DOC          Thésaurus en langue française
    - JURIVOC_ITA.DOC          Thésaurus en langue italienne
    - JURIVOC_GER_FRE.DOC      Dictionnaire allemand-français
    - JURIVOC_FRE_GER.DOC      Dictionnaire français-allemand
    - JURIVOC_GER_ITA.DOC      Dictionnaire allemand-italien
    - JURIVOC_ITA_GER.DOC      Dictionnaire italien-allemand
    - JURIVOC_FRE_ITA.DOC      Dictionnaire français-italien
    - JURIVOC_ITA_FRE.DOC      Dictionnaire italien-français


  3) Les relations et leurs réciproque:

     Dans les dictionnaires:

	- GER    Relation de traduction vers l'allemand
  - FRE    Relation de traduction vers le français
	- ITA    Relation de traduction vers l'italien

     Dans les thésauri:

	Relations	Réciproque	Signification

	- LT		n-a*		Lead Term
					(Terme principal pour les relations
					suivantes)
	- NT            BT              Narrow Term / Broad Term
					(Hierarchie des termes).
	- COM           n-a         	Commentaire interne du groupe thésaurus.
 	- SA01 à SA40	n-a	        See Also (Siehe Auch)
             				(relations non standard en remplacement
					de RT = Related Term).
	- SN		n-a		Scope Note.
					(note explicative, définition,
			  		indication d'utilisation).
	- UF 		USE		Used for / Use
					synonyme ou quasi-synonyme.
	- USA		UFA             use ... and ... / used for ... and ...
					renvoi à une combinaison de 
					descripteurs.

	* n-a = non-applicable (not available)


     (Création: voir BRATHES$COM:DUMP_JURIVOC.COM et PRINT_JURIVOC.COM)

	TFL-DyO / 8.09.1999

