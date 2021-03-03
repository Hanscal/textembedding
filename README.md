# 什么是 textembedding

[GitHub 欢迎提 pr，如果有 bug 或新需求 请反馈 issue](https://github.com/Hanscal/textembedding/issues)

textembeding 是我在计算文本相似度时经常需要用到的算法包，你可以使用它来加载预训练的Word2vec模型、得到词的向量和句子的向量，有助于您使用深度学习前的文本处理。

### 依赖与安装

```bash
jieba
numpy
gensim
```

```py
pip3 install textembedding
```

## 使用 textembedding

### 加载word2vector模型

```py
import textembedding as tb
model = tb.load_word2vect(modelpath)
vect_dim = model.vector_size
```

### 获得词向量

**model：load_word2vect加载的词向量模型**

**word：传入参数为需要求向量的词**

```py
word_vect = tb.get_word_embedding(model,word='中国')
```

### 获得句子向量

**model：load_word2vect加载的词向量模型**

**sentence：传入参数为需要求向量的句子**

**stop_words_path：用户自定义的stop words文件路径，文件和jieba的stop words格式一致**。

```py
sent_vect = tb.get_sentence_embedding(model,sentence='我们缺少的不是机会，而是在机会面前将自己重新归零的勇气。',stop_words_path='')
```

### 获得向量相似度

**query_vec：需要查询的向量**

**vec_list：向量库，在该库中查询向量**

**metirc_type：相似度的度量方式，目前只支持余弦相似度查询**。

**返回的是从大到小排列的相似度，[(item01,item02),...,(itemn1,itemn2)],item1为相似度，item2为向量库下标**

```py
similarity = tb.get_vector_similarity(query_vect,vec_list=[vect1, vect2, vect3, vectn])
```