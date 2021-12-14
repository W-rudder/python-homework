import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def plotweigh(weigh):
    weighlist=[]
    for i in range(len(weigh)):
        weighlist.append(int(weigh[i]["节点权重"]))
    x=list(set(weighlist))
    y=[]
    for i in x:
        caly=weighlist.count(i)
        y.append(caly)
    x=np.array(x)
    y=np.array(y)
    print(x,y)
    plt.bar(x,y,color='purple')
    plt.xlabel("节点的权重")
    plt.ylabel("次数")
    plt.title("节点权重的分布")
    plt.grid(alpha=0.5,linestyle='-.') 
    plt.show()

def plottype(type):
    typelist=[]
    for i in range(len(type)):
        typelist.append(type[i]["节点类型"])
    x=["writer","starring","director","movie"]
    y=[]
    for i in x:
        caly=typelist.count(i)
        y.append(caly)
    x=np.array(x)
    y=np.array(y)
    plt.bar(x,y, color='purple')
    plt.xlabel("节点的类型")
    plt.ylabel("次数")
    plt.title("节点类型的分布")
    plt.grid(alpha=0.5,linestyle='-.') 
    plt.show()

def plotlen(len_list):
    x=list(set(len_list))
    y=[]
    for i in x:
        caly=len_list.count(i)
        y.append(caly)
    x=np.array(x)
    y=np.array(y)
    print(x,y)
    plt.bar(x,y,color='purple')
    plt.xlabel("文本长度")
    plt.ylabel("频数")
    plt.title("文本长度的分布")
    plt.grid(alpha=0.5,linestyle='-.') 
    plt.show()

