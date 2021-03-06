# Twitterにおける実況書き込み検出手法の検討(映像情報メディア学会技術報告 2010)
(小林 尊志, 野田 雅文, 出口 大輔, 高橋 友和, 井手 一郎, 村瀬 洋)
https://www.jstage.jst.go.jp/article/itetr/34.25/0/34.25_129/_article/-char/ja/

>### あらまし
>Twitterでは実際にスポーツを観戦したりTV番組を視聴したりしながらリアルタイムに書き込む"実況書き込み"が増加している.
本報告では, 実際に観戦・視聴していないユーザの書き込みなど, 他の様々な書き込みの中から"実況書き込み"を検出する手法を提案する.
実験では, TV番組において「番組によらない情報」と「番組固有の情報」に注目して単語の出現頻度を学習して実況書き込みの検出を行なった.

#### メモ
小林ら(2010)はTwitterにおいて実際にスポーツを観戦したりしながらリアルタイムに書き込む"実況書き込み"が増加している現象に目をつけ, これを検出する手法を提案した. 放送開始直後の書き込みは「なう」や「はじまた」等イベント内容に依存しないものが多い。
そこで視聴内容に依存しない表現を抽出し, 開始直後の単語の出現頻度を学習することで識別器を構築したあと、「閲覧」「不閲覧」のラベルづけを行った. 

#### 実験手順
##### 番組のよらない情報によるラベル付け精度
2010.1-3月のTVドラマ5タイトル(1回45分程度)の放送1回分に対して, 放送開始5分間に書き込まれた614件の実況書き込み候補を用いて, ユーザへのラベルづけ実験を行なった.
各実況候補を形態素解析し, 単語の出現頻度上位200語を要素とする200次元の特徴ベクトルで表現した.  
SVMを利用して90.1%の精度で識別できた.(3 fold cross-validation)
##### 番組固有の情報による絞り込み精度
TVドラマ1タイトルの書き込み815件について, 番組固有の情報による絞り込み実験を行なった.
イベントによらない情報よらない情報を用いた1段階目のラベル付けは人手で行ったものを用いた.
出現頻度上位500語を要素とする500次元の特徴ベクトルを生成して,"名詞のみ","名詞, 動詞, 形容詞", "名詞,動詞,助動詞,形容詞,形容動詞"の3手法で検出率を見た. 手法3が一番よく79.8%だった.
