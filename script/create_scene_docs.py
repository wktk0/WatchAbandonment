# input-> DataFrame型
#　string型で返す
def create_scene_docs(comments):
    scene_docs = []
    for _,com in comments.groupby("current_position_10"):
        s=[]
        for words in com["wakati"].values:
            for word in words.split(" "):
                if word=="":
                    continue
                s.append(word)
        scene_docs.append(" ".join(s))
    return scene_docs
