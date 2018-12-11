# input-> DataFrame型
#　list型で返す
def create_scene_docs(comments,RETURN_TYPE=""):
    scene_docs = []
    for _,com in comments.groupby("current_position_10"):
        s=[]
        for words in com["wakati"].values:
            for word in words.split(" "):
                if word=="":
                    continue
                s.append(word)
        if RETURN_TYPE=="string":
            scene_docs.append(" ".join(s))
        else:
            scene_docs.append(s)
    return scene_docs
