import pandas as pd
import numpy as np
from glob import glob

fpath=""
comments = pd.read_csv(fpath)
logname = glob("datasets/raw_log/*")

for fname in logname[:10]:
    slot_id = fname.split("/")[-1].split("_")[1]
    print("slot_id:",slot_id)
    # コメントログ(シーン文書作成について)
    output = comments.query("slot_id == @slot_id")
    output = output.dropna()
    
    scene_docs = create_scene_docs(output)
    # 視聴ログ
    logs = pd.read_csv(fname)
    logs["watch_time"] = logs["end_position"] - logs["start_position"]
    # ログの視聴時間が5分以上のログに限定する
    logs = logs.query("watch_time >= {}".format(300)) 
    logs = logs.reset_index()
    
    MAX_TIME = len(scene_docs)
    #print(MAX_TIME)
    
    # 離脱ログについて
    leaving_uu = [0 for _ in range(0, MAX_TIME+1)]
    for i, j in zip(logs.groupby("end_position_10").size().index, logs.groupby("end_position_10").size().values):
        if i > MAX_TIME:
            break
        leaving_uu[i] = j
    
    # リアルタイム視聴数(5分以上視聴ユーザについて)について
    realtime_uu = []
    users = []
    for t in range(0, MAX_TIME):
        users=logs.query("start_position_10 <= @t and end_position_10 > @t")["user_id"].unique().tolist()
        realtime_uu.append(len(users))
    #print(len(realtime_uu))
