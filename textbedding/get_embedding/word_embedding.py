#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 12:17 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

import numpy as np

def compute_ngrams(word, min_n, max_n):
    extended_word = word
    ngrams = []
    for ngram_length in range(min_n, min(len(extended_word), max_n) + 1):
        for i in range(0, len(extended_word) - ngram_length + 1):
            ngrams.append(extended_word[i:i + ngram_length])
    return list(set(ngrams))


def word_vector(model, word, min_n=1, max_n=3):
    # 确认词向量维度
    word_size = model.wv.syn0[0].shape[0]
    # 如果在词典之中，直接返回词向量
    if word in model.index2word:
        return model[word]
    else:
        word_vec = np.zeros(word_size, dtype=np.float32)
        # 不在词典的情况下，计算与词相近的词向量
        # 计算word的ngrams词组
        ngrams = compute_ngrams(word, min_n=min_n, max_n=max_n)

        ngrams_found = 0
        ngrams_single = [ng for ng in ngrams if len(ng) == 1]
        ngrams_more = [ng for ng in ngrams if len(ng) > 1]
        # 先只接受2个单词长度以上的词向量
        for ngram in ngrams_more:
            if ngram in model.index2word:
                word_vec += model[ngram]
                ngrams_found += 1
                # print(ngram)
        # 如果，没有匹配到，那么最后是考虑单个词向量
        if ngrams_found == 0:
            for ngram in ngrams_single:
                if ngram in model.index2word:
                    word_vec += model[ngram]
                    ngrams_found += 1
        if word_vec.any():  # 只要有一个不为0
            return word_vec / max(1, ngrams_found)
        else:
            print('all ngrams for word %s absent from model' % word)
            return word_vec  # 全为零向量


