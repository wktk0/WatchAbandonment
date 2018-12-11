import gensim
from gensim import corpora, models, similarities

def learn_lda(scene_docs, K=10, SEED=9):
    #乱数:SEED #トピック数(特徴数): K

    dictionary = corpora.Dictionary(scene_docs)
    dictionary.filter_extremes(no_below=10, no_above=1)

    corpus = []
    for word in scene_docs:
        bow = dictionary.doc2bow(word)
        corpus.append(bow)
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, num_topics=K, id2word=dictionary, random_state=SEED)
    return lda,dictionary,corpus

scene_docs = create_scene_docs(output)
lda, dictionary, corpus = learn_lda(scene_docs)
