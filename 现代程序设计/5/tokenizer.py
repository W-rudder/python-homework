import sys
sys.path.append(r"C:\Users\86186\Desktop\现代程序设计\4")

from GraphStat.Visualization import plotnodes
import jieba

filepath=r"C:\Users\86186\Desktop\现代程序设计\jd_comments.txt"

class Tokenizer:

    def __init__(self,chars,coding='c',PAD=0) :
        self.chars=chars
        self.coding=coding
        self.PAD=PAD
        self.dict={}
        self.dict["PAD"]=PAD
        self.count=1
        if self.coding == 'c':
            for i in self.chars:
                for j in list(i):
                    if j not in self.dict.keys() and '\u4e00' <= j <= '\u9fff':
                        self.dict[j]=self.count
                        self.count += 1
        else:
            for i in self.chars:
                for j in jieba.lcut(i):
                    if j not in self.dict.keys() and '\u4e00' <= j <= '\u9fff':
                        self.dict[j]=self.count
                        self.count += 1

    def tokenize(self,sentence):
        res=[]
        if self.coding == 'c':
            for i in list(sentence):
                if '\u4e00' <= i <= '\u9fff':
                    res.append(i)
        else:
            for i in jieba.lcut(sentence):
                if '\u4e00' <= i <= '\u9fff':
                    res.append(i)
        return res


    def encode(self,list_of_chars):
        res=[]
        for i in list_of_chars:
            res.append(self.dict[i])
        return res

    def trim(self,tokens,seq_len):
        while(len(tokens) < seq_len):
            tokens.append(self.PAD)
        while(len(tokens) > seq_len):
            tokens.pop()
        return tokens

    def decode(self,tokens):
        res=[]
        ls=list(self.dict.keys())
        for i in tokens:
            res.append(ls[i])
        
        for j in res:
            print(j,end='')
    
    def encode_all(self,seq_len):
        res=[]
        for i in self.chars:
            if len(i) == seq_len:
                list_of_chars=self.tokenize(i)
                tokens=self.encode(list_of_chars)
                res.append(self.trim(tokens,len(i)))
        return res


chars=[]   
with open(filepath,'r',encoding="utf-8") as f:
    for line in f.readlines():
        chars.append(line.strip())

t=Tokenizer(chars,'w')

list_of_chars=t.tokenize(chars[55])
tokens=t.encode(list_of_chars)
tokens=t.trim(tokens,len(chars[55]))

len_list=[]
for i in chars:
    len_list.append(len(i))
plotnodes.plotlen(len_list)


