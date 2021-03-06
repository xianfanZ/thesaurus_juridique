#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

import logging,scipy,gensim.models
import numpy as np

def avg_feature_vector(words, model, num_features):
        featureVec = np.zeros((num_features,), dtype="float32")
        nwords = 0
        for word in words:
            nwords = nwords+1
            try:
                c = model[word.lower()]
            except KeyError:
                # print(word,"not in vocabulary")
                c = 0
            # featureVec = np.add(featureVec, model[word])
            featureVec = np.add(featureVec, c)
        if(nwords>0):
            featureVec = np.divide(featureVec, nwords)
        return featureVec

# calculer la similarité entre deux expressions
def calcul_similarity(v1,v2):
    return 1 - scipy.spatial.distance.cosine(v1,v2)

# main program
# def main():
    # logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # sentences = word2vec.Text8Corpus("../Corpus/types/ABUS_DE_CONFIANCE.txt")  # load corpus
    # model = word2vec.Word2Vec(sentences, size=200)

    # model = gensim.models.Word2Vec.load('../Resultats/wv.model')

    # calculer le vecteur moyen d'une liste de mots
    # v1 = avg_feature_vector("Droit de vote".split(),model, num_features=300)
    # print(v1)
#     v2 = avg_feature_vector('Fraude électorale'.split(),model, num_features=300)

#     s = calcul_similarity(v1,v2)
#     print(s)

# if __name__ == '__main__':
#     main()

