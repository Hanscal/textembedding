#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 12:10 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

import textembedding.get_embedding.word_embedding
import textembedding.get_embedding.sentence_embedding

def get_word_embedding(model,word,min=1,max=3):
    word_vector = textembedding.get_embedding.word_embedding.word_vector(model, word, min, max)
    return word_vector

def get_sentence_embedding(model,sentence, add_pos_weight=['n','nr','ng','ns','nt','nz'],stop_words_path=None):
    sentence_vector = textembedding.get_embedding.sentence_embedding.sentence_vector(model, sentence, add_pos_weight, stop_words_path)
    return sentence_vector
