import pandas as pd
import mojimoji
import neologdn
from tqdm import tqdm_notebook as tqdm

# 入力:DataFrame想定で
def preprocessing_nlp(comments, OUTPUT_INDEX=["origin","norm","current_position"]):
    OUTPUT_INDEX = ["origin","norm","wakati","current_position", "current_position_10"]
    output = pd.DataFrame()
    output["current_position"] = comments["current_position"]
    # {5,10,20}のセグメントを作成:シーン分割
    output["current_position_5"] = output["current_position"]//5
    output["current_position_10"] = output["current_position"]//10
    output["current_position_20"] = output["current_position"]//20
    # オリジナル
    #output["origin"] = comments["comment_text"]
    output["origin"] = comments["origin"]
    # アルファベットの小文字化
    output["origin"] = output["origin"].str.lower()
    # 全角変換
    output["origin"] = [mojimoji.han_to_zen(text) for text in output["origin"].values]
    # 繰り返し正規化
    output["norm"] = [neologdn.normalize(str(text), repeat=2) for text in output["origin"]]
    # 15文字以下に限定する
    output = output[output["norm"].str.len() <= 15]
    print(output.shape)
    # NaNの削除
    output = output.dropna()
    output = output.reset_index()
    # 分かち書き
    output["wakati"] = [juman_wakati(output.norm.loc[idx], hinshi=("形容詞"), STEM_FLAG = True) for idx in tqdm(range(0, output.shape[0]))]
    
    return output[OUTPUT_INDEX]
