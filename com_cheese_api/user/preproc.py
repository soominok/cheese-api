import MeCab
import os
import pandas as pd

#from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def searchFiles(path):
    filelist = []
    filenames = os.listdir(path)
    for filename in filenames:
        file_path = os.path.join(path, filename)
        filelist.append(file_path)
    return filelist

def getNVM_lemma(text):
    tokenizer = MeCab.Tagger()
    parsed = tokenizer.parse(text)
    word_tag = [w for w in parsed.split("\n")]
    pos = []
    tags = ['NNG', 'NNP', 'VV', 'VA', 'VX', 'VCP', 'VCN', 'MAG']
    for word_ in word_tag[:-2]:
        word = word_.split("\t")
        tag = word_.split("\t")
        tag = word[1].split(",")
        if (len(word[0]) < 2):
            continue
        if(tag[-1] != '*'):
            t = tag[-1].split('/')
            if(len(t[0])>1 and ('VV' in t[1] or 'VA' in t[1] or 'VX' in t[1])):
                pos.append(t[0])
            else:
                if(tag[0] in tags):
                    pos.append(word[0])
        return pos

def main():
    buyLists = []
    for filePath in searchFiles('com_cheese_api/user/data'):
        buyList = pd.read_csv(filePath, encoding = 'utf-8')
        buyLists.append(buyList)
    docs = pd.concat(buyLists, ignore_index = True)
    print(docs)

if __name__ == '__main__':
    main()

