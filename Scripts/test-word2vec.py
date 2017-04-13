# -*- coding: utf-8 -*-

from gensim.models import word2vec
import logging

# main program
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus("../../Corpus/types/ABUS_DE_CONFIANCE.txt")  # load corpus
model = word2vec.Word2Vec(sentences, size=200)

# calculate the similarity of two words
y1 = model.similarity("somme", "tribunal")
print(u"similarity：", y1)
print("--------\n")

# 20 most similar words with "tribunal"
y2 = model.most_similar("l'action", topn=5)
print(u"similarity words with tribunal\n")
for w in y2:
    print(w[0],w[1])
print("--------\n")


# find the corresponding relationship
y3 = model.most_similar(["dossier"])