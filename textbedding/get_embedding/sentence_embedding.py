#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 1:34 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
import sys
import os
sys.path.append(os.path.dirname(__file__))
import jieba.posseg as pseg
import numpy as np
from tqdm import tqdm
from utils import get_stop_words
from word_embedding import word_vector

def sentence_vector(model, sentence, add_pos_weight=['n','nr','ng','ns','nt','nz'],stop_words_path=None):
    words = pseg.cut(sentence)
    vecs = []
    stop_words = get_stop_words(stop_words_path)
    for word, flag in tqdm(words):
        # 自增权重
        if flag in add_pos_weight and word not in stop_words:
            # 词向量获取
            vec = word_vector(model, word, min_n=1, max_n=3)
            vecs.append(vec)
            vecs.append(vec)  # 默认名词自增权重
        elif flag not in add_pos_weight and word not in stop_words:
            vec = word_vector(model, word, min_n=1, max_n=3)
            vecs.append(vec)
        else:
            continue

    if vecs:
        vecs = np.array(vecs)
        vecs_mean = np.mean(vecs, axis=0)
    else:
        vecs_mean = np.zeros((model.vector_size), dtype=np.float32)
    return vecs_mean

