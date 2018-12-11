from sklearn.cluster import KMeans
from yellowbrick.text import TSNEVisualizer

#LDA予測
pred_score = predict_lda(scene_docs)
result = pd.DataFrame(pred_score)

clusters = KMeans(n_clusters=10)
clusters.fit(result.values)

plt.figure(figsize=(10,10))
tsne = TSNEVisualizer()
tsne.fit(result.values, ["c{}".format(c) for c in clusters.labels_])
tsne.poof()
