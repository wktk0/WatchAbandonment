def predict_lda(scene_docs, lda=lda, dictionary=dictionary, K=K):
    # コーパス作成
    test_corpus = []
    for word in scene_docs:
        bow = dictionary.doc2bow(word)
        test_corpus.append(bow)
    # 予測スコア
    pred_score = {}
    for _ in range(0, K):
        pred_score[_] = []
    # 予測
    for c  in test_corpus:
        score = [0 for i in range(0,K)]
        for n,s in lda[c]:
            score[n] = s
        for i in range(0,K):
            pred_score[i].append(score[i])
    return pred_score
