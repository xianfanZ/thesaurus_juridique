#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus("../Resultats/corpus_concat.txt")  # load corpus
model = word2vec.Word2Vec(sentences, size=300, min_count=1)
model.save('../Resultats/wv2.model')