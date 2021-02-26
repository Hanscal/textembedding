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
pip3 install pycapt
```

## 使用 textembedding

### 加载word2vector模型

```py
import textembedding
model = textbedding.load_word2vect(modelpath)
vect_dim = model.vector_size
```

### 获得词向量

**two_valve : 二值化方法，必选参数 img 为图片，可选参数 Threshold** 是灰度阀值，这里可以选择适合的值，默认值是 100 . **返回新处理过的图片**

```py
word_vect = textbedding.get_word_embedding(model,'中国')
```

### 获得句子向量

**dele_noise ：消除噪点方法，该方法使用的是八领域去噪点法，N 是领域异点个数，Z 是处理次数，处理次数越多 图形越圆滑**。

```py
sent_vect = textbedding.get_sentence_embedding(model,'我是中国人，我爱我的祖国。',stop_words_path='')
```
