import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
import numpy as np

file_path = '/scratch/wd2148/data_1106.csv'

data = pd.read_csv(file_path)

background_texts = data['Background_Prompt'].astype(str)
print(background_texts.head())

model = SentenceTransformer('all-MiniLM-L6-v2')  # 需要调试
# 记录结果 for loop里面更新文件
embeddings = model.encode(background_texts)

# 尝试不同的 K 值，计算轮廓系数，选择最佳 K
silhouette_scores_s = []
K_s = range(2, 80)
for k in K_s:
    kmeans_s = KMeans(n_clusters=k, random_state=42)
    kmeans_s.fit(embeddings)
    score_s = silhouette_score(embeddings, kmeans_s.labels_)
    silhouette_scores_s.append(score_s)
    print(f"K = {k}, Silhouette Score = {score_s:.4f}")
    
scores_df = pd.DataFrame(list(zip(K_s, silhouette_scores_s)), columns=['K', 'Silhouette_Score'])
scores_df.to_csv('/scratch/wd2148/silhouette_scores.csv', index=False)


plt.plot(K_s, silhouette_scores_s, 'bx-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Selecting k with the Silhouette Score Method')
plt.show()
plt.savefig('/scratch/wd2148/sen2vec_iw_2.png')

best_k = K_s[silhouette_scores_s.index(max(silhouette_scores_s))]
print(f"Best number of clusters based on Silhouette Score: {best_k}")

# bestK值 最终聚类
kmeans = KMeans(n_clusters=best_k, random_state=42)
kmeans.fit(embeddings)

# print聚类标签
cluster_labels = kmeans.labels_
data['Cluster_Labels'] = kmeans.labels_
data.to_csv('/scratch/wd2148/clustered_data_sen_iw_2.csv', index=False)


