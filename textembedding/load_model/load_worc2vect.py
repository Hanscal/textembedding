#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 12:11 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

import gensim


def load_file(filepath):
    print("文件载入开始")
    wv_from_text = gensim.models.KeyedVectors.load(filepath,mmap='r')
    print("文件载入完毕")
    # vector_size = wv_from_text.vector_size
    return wv_from_text

if __name__ == '__main__':
    filepath = '/Volumes/work/project/article_search/data/Tencent_AILab_ChineseEmbedding/Tencent_AILab_ChineseEmbedding.bin'
    load_file(filepath)
