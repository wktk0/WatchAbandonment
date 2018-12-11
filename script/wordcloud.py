import matplotlib.pyplot as plt
from wordcloud import WordCloud
%matplotlib inline

#WordCloudは入力はstring型(文字列で半角空白で区切る)
mel = "おはよう おはよう おやすみ おはよー"

#fpath = "/Library/Fonts/AppleMyungjo.ttf"
fpath = "/System/Library/Fonts/ヒラギノ明朝 ProN.ttc"

wordcloud = WordCloud(width=800, height=400,
                          collocations=False,
                          font_path=fpath,
                         ).generate(mel)

plt.figure(figsize=(15,12))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.title(6, fontsize=25,color='w')
plt.tight_layout(pad=0)
plt.show()
