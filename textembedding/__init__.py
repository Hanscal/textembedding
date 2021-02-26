#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 12:07 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

import textembedding.get_embedding
import textembedding.load_model


name = "textbedding"

# 加载wv model
def load_word2vect(filepath):
    model = textembedding.load_model.load_word2vect(filepath)
    return model

# 获取字向量
def get_word_embedding(model,word,min=1,max=3):
    word_vector = textembedding.get_embedding.get_word_embedding(model, word, min, max)
    return word_vector

# 获取句子向量
def get_sentence_embedding(model, sentence, add_pos_weight=['n','nr','ng','ns','nt','nz'],stop_words_path=None):
    sentence_vector = textembedding.get_embedding.get_sentence_embedding(model, sentence, add_pos_weight, stop_words_path)
    return sentence_vector
