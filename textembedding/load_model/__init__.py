#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 12:10 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
import textembedding.load_model.load_worc2vect

def load_word2vect(filepath):
    model = textembedding.load_model.load_worc2vect.load_file(filepath)
    return model
