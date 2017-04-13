# -*- coding: utf-8 -*-

from gensim.models import word2vec
import logging,scipy
import numpy as np

def avg_feature_vector(words, model, num_features):
        #function to average all words vectors in a given paragraph
        featureVec = np.zeros((num_features,), dtype="float32")
        nwords = 0

        #list containing names of words in the vocabulary
        #index2word_set = set(model.index2word) this is moved as input param for performance reasons
        for word in words:
            nwords = nwords+1
            featureVec = np.add(featureVec, model[word])

        if(nwords>0):
            featureVec = np.divide(featureVec, nwords)
        return featureVec


# main program
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus("../Corpus/types/ABUS_DE_CONFIANCE.txt")  # load corpus
model = word2vec.Word2Vec(sentences, size=200)

# calculer le vecteur moyen d'une liste de mots
v1 = avg_feature_vector(['tribunal','pénal'],model, num_features=200)
#print(v1)
v2 = avg_feature_vector(['constitution','articles'],model, num_features=200)

# calculer la similarité
similarity = 1 - scipy.spatial.distance.cosine(v1,v2)
print(similarity)

