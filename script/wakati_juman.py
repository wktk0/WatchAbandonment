from pyknp import Juman

def juman_wakati(text, hinshi=(),DEBUG=False, STEM_FLAG=False):
    juman = Juman()
    output = ""
    # wakati
    result = juman.analysis(text)
    for mrph in result.mrph_list():
        if STEM_FLAG and mrph.hinsi in hinshi:
            output += mrph.repname.split("/")[0]+" "
        if DEBUG:
            print("stem:",mrph.repname)
            print("midashi:",mrph.repname)
            print("hinsi:",mrph.hinsi)
            print("yomi:",mrph.yomi)
    return output.strip()

if __name__ == '__main__':
    juman_wakati("かわいーすぎないか?",hinshi=("形容詞"),DEBUG=True,STEM_FLAG=True)
