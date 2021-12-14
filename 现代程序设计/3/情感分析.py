import re
from time import time
from types import resolve_bases
import jieba
import numpy as np
import pandas as pd
from datetime import datetime
import itertools
from geopy.distance import geodesic, geodesic


angerfile=r'C:\Users\86186\Desktop\现代程序设计\anger.txt'
disgustfile=r'C:\Users\86186\Desktop\现代程序设计\disgust.txt'
fearfile=r'C:\Users\86186\Desktop\现代程序设计\fear.txt'
joyfile=r'C:\Users\86186\Desktop\现代程序设计\joy.txt'
sadnessfile=r'C:\Users\86186\Desktop\现代程序设计\sadness.txt'
stopwordsfile=r"C:\Users\86186\Desktop\现代程序设计\stopwords_list.txt"
filename=r'C:\Users\86186\Desktop\现代程序设计\3\weibo.txt'

anger=[]
disgust=[]
fear=[]
joy=[]
sadness=[]

with open(angerfile,'r',encoding='utf-8') as f:
    for line in f.readlines():
        anger.append(line.strip())

with open(disgustfile,'r',encoding='utf-8') as f:
    for line in f.readlines():
        disgust.append(line.strip())

with open(fearfile,'r',encoding='utf-8') as f:
    for line in f.readlines():
        fear.append(line.strip())  

with open(joyfile,'r',encoding='utf-8') as f:
    for line in f.readlines():
        joy.append(line.strip())

with open(sadnessfile,'r',encoding='utf-8') as f:
    for line in f.readlines():
        sadness.append(line.strip())


def clean(line):#去除文本中的噪声(只保留中文)
    pattern = r'[^\u4e00-\u9fa5]'
    line = re.sub(pattern,'',line) #将其中所有非中文字符替换
    return line

def stopwordslist():
    stopwords=[]
    with open(stopwordsfile,"r",encoding='utf-8') as sw:
        for line in sw.readlines():
            stopwords.append(line.strip())
    stopwords.append(' ')
    return stopwords

def worddepart():
    jieba.load_userdict(angerfile)
    jieba.load_userdict(disgustfile)
    jieba.load_userdict(fearfile)
    jieba.load_userdict(joyfile)
    jieba.load_userdict(sadnessfile)
    res=[]
    stoplist=stopwordslist()

    with open(filename , 'r' , encoding='utf-8') as f:
        for line in f.readlines():
            midres=[]
            s=clean(line)
            s=jieba.lcut(s)
            for i in s:
                if i not in stoplist:
                    midres.append(i)
            res.append(midres)
    return res

def getvector(anger,disgust,fear,joy,sadness):
    emodict={}
    emodict['anger']=anger
    emodict['disgust']=disgust
    emodict['fear']=fear
    emodict['joy']=joy
    emodict['sadness']=sadness
    def inget(comment):
        vector=[0,0,0,0,0]
        for i in comment:
            if i in emodict['anger']:
                vector[0] +=1
            elif i in emodict['disgust']:
                vector[1] +=1
            elif i in emodict['fear']:
                vector[2] +=1
            elif i in emodict['joy']:
                vector[3] +=1
            elif i in emodict['sadness']:
                vector[4] +=1
        return vector
    return inget

def getvalue(anger,disgust,fear,joy,sadness):
    emodict={}
    emodict['anger']=anger
    emodict['disgust']=disgust
    emodict['fear']=fear
    emodict['joy']=joy
    emodict['sadness']=sadness
    def inget(comment):
        vector=[0,0,0,0,0]
        for i in comment:
            if i in emodict['anger']:
                vector[0] +=1
            elif i in emodict['disgust']:
                vector[1] +=1
            elif i in emodict['fear']:
                vector[2] +=1
            elif i in emodict['joy']:
                vector[3] +=1
            elif i in emodict['sadness']:
                vector[4] +=1
            
        vector = np.array(vector)
        pos = np.where(vector == vector.max())
        length = np.size(pos)
        if length == 1:
            if 0 in pos:
                return 'anger'
            elif 1 in pos:
                return 'disgust'
            elif 2 in pos:
                return 'fear'
            elif 3 in pos:
                return 'joy'
            elif 4 in pos:
                return 'sadness'
        elif length == 5:
            return 'noneemotion'
        else:
            return 'complexemotion'
    return inget

def weiboclass():
    angryclass = []
    disgustedclass = []
    happyclass = []
    sadclass = []
    scaredclass = []
    complexclass = []
    nonemotionclass = []

    jieba.load_userdict(angerfile)
    jieba.load_userdict(disgustfile)
    jieba.load_userdict(fearfile)
    jieba.load_userdict(joyfile)
    jieba.load_userdict(sadnessfile)
    stoplist=stopwordslist()
    f1=getvector(anger,disgust,fear,joy,sadness)

    with open(filename , 'r' , encoding='utf-8') as f:
        for line in f.readlines():
            midres=[]
            s=clean(line)
            s=jieba.lcut(s)
            for i in s:
                if i not in stoplist:
                    midres.append(i)
            vector=f1(midres)
            vector = np.array(vector)
            pos = np.where(vector == vector.max())
            length = np.size(pos)
            if length == 1:
                if 0 in pos:
                    angryclass.append(line)
                elif 1 in pos:
                    sadclass.append(line)
                elif 2 in pos:
                    scaredclass.append(line)
                elif 3 in pos:
                    happyclass.append(line)
                elif 4 in pos:
                    disgustedclass.append(line)
            elif length == 5:
                nonemotionclass.append(line)
            else:
                complexclass.append(line)
    weibolist = [angryclass, sadclass, scaredclass, happyclass,
    disgustedclass, complexclass, nonemotionclass]
    return weibolist

def get_time(emotionlist):
    time=[]
    i=0
    length=len(emotionlist)
    model_time = re.compile(r'\d\d\s\d\d:\d\d:\d\d')

    for i in range(length):
        content=emotionlist[i]
        t ="2013 11 "+ model_time.search(content).group()
        mid=[]
        mid.append(t)
        time.append(mid)
    
    return time

def timesum(model,weibolist,emotype):
    emotionlist=weibolist[emotype]
    time=get_time(emotionlist)

    

    time = list(itertools.chain.from_iterable(time))
    time = pd.to_datetime(pd.Series(time),format='%Y %m %d %H:%M:%S')
    diction = {'time':time}
    data = pd.DataFrame(diction)
    if model == 0:  
        m = data.resample('30T',on='time').count()
    elif model == 1:
        m = data.resample('60T',on='time').count()
    elif model == 2:
        m = data.resample('24h',on='time').count()
    return m

def get_xy(emotionlist):

    xy=[]
    i=0
    length=len(emotionlist)
    model_x = re.compile(r'116\.\d+')
    model_y = re.compile(r'39\.\d+|40\.\d+')


    for i in range(length):
        content=emotionlist[i]
        x = model_x.search(content).group()       
        y = model_y.search(content).group()
    
        xy.append((float(y),float(x)))
    
    return xy

midxy=(39.9299857781,116.395645038,)

def xysum(r,weibolist,emotype):
    xycount=0
    i=0
    emotionlist=weibolist[emotype]

    xy=get_xy(emotionlist)
    for i in xy:
        if geodesic(i,midxy) <= r:
            xycount += 1
    
    return xycount


def main():
    res=worddepart()
    #print(res)

    #f1=getvector(anger,disgust,fear,joy,sadness)
    #print(f1(res[5]))

    #f2=getvalue(anger,disgust,fear,joy,sadness)
    #print(f2(res[5]))

    weibolist=weiboclass()
    #print(timesum(1,weibolist,0))
    print(xysum(10,weibolist,3))



if __name__=='__main__':
    main()




    



