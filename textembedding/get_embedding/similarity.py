#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/3 2:12 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
import numpy as np

def get_similarity(query_vec, vec_list,metric_type='cos'):
    similarity = None
    if metric_type == 'cos':
        vec_arr = np.asarray(vec_list)
        query_arr = np.asarray(query_vec)
        similarity_arr = np.dot(vec_arr, query_arr.reshape(1, -1).T)
        similarity_arr_arg = np.argsort(similarity_arr, axis=0)[::-1]  # 从大到小排序
        similarity = [(similarity_arr[i][0][0],i[0]) for i in similarity_arr_arg]
    else:
        print('not support metric type in similarity get!')
    return similarity