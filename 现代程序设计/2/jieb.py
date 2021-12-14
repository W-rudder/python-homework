import jieba
import collections
import numpy as np
import matplotlib.pyplot as plt
import wordcloud
filename="C:/Users/86186/Desktop/jd_comments.txt"
stopwords_file="C:/Users/86186/Desktop/stopwords_list.txt"

#构建停用词表
def stopwordslist():
    stopwords=[]
    with open(stopwords_file,"r",encoding='utf-8') as sw:
        for line in sw.readlines():
            stopwords.append(line)
    stopwords.append('\n  \n')
    return stopwords

#分词并进行统计输出，以字典形式输出
def word_depart():
    jieba.load_userdict(r"C:\Users\86186\AppData\Local\Programs\Python\Python37\Lib\site-packages\jieba\dict1.txt")
    res={}
    stopwords=stopwordslist()
    with open(filename,"r",encoding='utf-8') as f:
        for line in f.readlines():
            data1=jieba.lcut(line)
            for i in data1:
                if i+"  \n" not in stopwords:
                    if i in res.keys():
                        res[i] += 1
                    else:
                        res[i] = 1
    res=collections.OrderedDict(sorted(res.items(),key=lambda dc:dc[1],reverse=True))
    return res

#获取第i条评论的特征向量
def vectorize(x):
    key1=list(word_depart().keys())[:50]
    res1=[]
    i=1
    with open(filename,"r",encoding='utf-8') as f:
        for line in f.readlines():
            if i == x:
                data2=jieba.lcut(line)
                for m in range(50):
                    if key1[m] in data2:
                        res1.append(1)
                    else:
                        res1.append(0)
            i=i+1
    print("第%d条评论的向量：\n" % x)
    print(res1)
    return res1

#获取第x条和第y条评论的欧氏距离
def getdist(x,y):
    m=vectorize(x)
    n=vectorize(y)
    dist = np.sqrt(np.sum(np.square(np.array(m)-np.array(n))))
    return dist

#获取重心评论并输出原文
def getcenter():
    key1=list(word_depart().keys())[:100]
    allx=[]
    distance=[]
    with open(filename,"r",encoding='utf-8') as f:
        for line in f.readlines():
            res2=[]
            data2=jieba.lcut(line)
            for m in range(100):
                if key1[m] in data2:
                    res2.append(1)
                else:
                    res2.append(0)
            allx.append(res2)
    for i in range(1002):
        dist=np.sqrt(np.sum(np.square(np.array(allx)-np.array(allx[i]))))
        distance.append(dist)
        print("第%d条评论到重心的距离为：%.5f" % (i+1,dist))
    k=distance.index(min(distance))+1
    print("评论重心为第%d条评论" % k)
    print("内容为：")
    num=1
    with open(filename,"r",encoding='utf-8') as f:
        for line in f.readlines():
            if num==k:
                print(line)
            num=num+1

#绘制词云图
def draw_cloud(res):
    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simhei.ttf', 
        max_words=150,      
        max_font_size=100,   
        background_color='white'
    )
    wc.generate_from_frequencies(res) 
    plt.imshow(wc) 
    plt.axis('off') 
    plt.show() 

        
def main():
    res=word_depart()
    vectorize(3)
    print(getdist(3,4))
    getcenter()
    draw_cloud(res)


if __name__=="__main__":
    main()












                
