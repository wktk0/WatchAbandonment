## Script
前処理に利用したスクリプト置き場

|file name|概要|
|:--|:--|
|wakati_juman.py|形態素解析ライブラリJumanを用いた分かち書きする関数|
|preprocessing_nlp.py|コメントの前処理適用後,Jumanで分かち書きする関数|
|create_scene_docs.py|各セグメント毎に分割して文書化するシーン文書を作成する関数|
|lda.py|gensimを用いたLDA|
|predict_lda.py|LDA,dictionary,corpusを引数にシーン文書のLDAのスコアを出力|
|kmeans_tsne.py|各シーン文書のトピックスコアをK-meansでクラスタリング後にT-SNEで可視化|
|CountingAbandonment.py|視聴数と離脱数とカウンティングするプログラム|

