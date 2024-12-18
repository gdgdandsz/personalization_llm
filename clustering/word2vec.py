import pandas as pd
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModel
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import torch
from sentence_transformers import SentenceTransformer

file_path = '/scratch/wd2148/data_1106.csv'

data = pd.read_csv(file_path)

nltk_data_path = '/scratch/wd2148/nltk_data'  # Adjust the path as needed
if nltk_data_path not in nltk.data.path:
    nltk.data.path.append(nltk_data_path)

nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)


background_texts = data['Background_Prompt'].astype(str)
print(background_texts.head())


def preprocess_text(text):
    # 去除特殊字符和数字
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)

    # 转换为小写
    text = text.lower()

    # 分词
    tokens = word_tokenize(text)

    # 去除停用词
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    return tokens

# 对所有文本进行预处理
processed_texts = background_texts.apply(preprocess_text)

# 构建词汇表
sentences = processed_texts.tolist()


w2v_model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)


# w2v_model.save('w2v_model.model')

def text_to_vector(text):
    vectors = []
    for word in text:
        if word in w2v_model.wv:
            vectors.append(w2v_model.wv[word])
    if len(vectors) > 0:
        # 计算平均向量
        vector = np.mean(vectors, axis=0)
    else:
        # 如没有词汇在词汇表中，返回零向量
        vector = np.zeros(w2v_model.vector_size)
    return vector

# 将所有文本转换为向量
text_vectors = processed_texts.apply(text_to_vector)

# 转换为二维数组
X = np.array(text_vectors.tolist())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 确定聚类数目 K
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# 尝试不同的 K 值，计算轮廓系数，选择最佳 K
silhouette_scores_w = []
K_w = range(2, 80)
for k in K_w:
    kmeans_w = KMeans(n_clusters=k, random_state=42)
    kmeans_w.fit(X_scaled)
    score_w = silhouette_score(X_scaled, kmeans_w.labels_)
    silhouette_scores_w.append(score_w)
    print(f"Round: {k}")

plt.plot(K_w, silhouette_scores_w, 'bx-')
plt.xlabel('k')
plt.ylabel('Silhouette Score')
plt.title('Selecting k with the Silhouette Score Method')
plt.show()
plt.savefig('/scratch/wd2148/silhouette_plot_word2vec.png')

best_k = K_w[silhouette_scores_w.index(max(silhouette_scores_w))]
print(f"Best number of clusters based on Silhouette Score: {best_k}")


kmeans_w = KMeans(n_clusters=best_k, random_state=42)
kmeans_w.fit(X_scaled)
labels = kmeans_w.labels_

data['Cluster'] = labels
data.to_csv('/scratch/wd2148/clustered_data_word2vec.csv', index=False)





