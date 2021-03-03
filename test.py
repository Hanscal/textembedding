#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 12:03 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

import textembedding

if __name__ == '__main__':
    filepath = '/Volumes/work/project/article_search/data/Tencent_AILab_ChineseEmbedding/Tencent_AILab_ChineseEmbedding.bin'
    model = textembedding.load_word2vect(filepath)
    word_vect = textembedding.get_word_embedding(model, '中国')
    sent_vect = textembedding.get_sentence_embedding(model, '我是中国人，我爱我的祖国。', stop_words_path='')
    vect_sim = textembedding.get_vector_similarity(word_vect,[sent_vect, word_vect])
    print(model.vector_size)
    print(vect_sim)