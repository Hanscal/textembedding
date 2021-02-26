#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 1:35 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
import os

file_root = os.path.dirname(__file__)

def get_stop_words(filepath=None):
    if filepath is None:
        filepath = os.path.join(file_root, 'stop_words.txt')
    elif isinstance(filepath,str) and not os.path.exists(filepath):
        filepath = os.path.join(file_root,'stop_words.txt')
    with open(filepath, 'r') as f:
        stop_words_text = f.read()
        stop_words = set(stop_words_text.split('\n'))
    return stop_words

