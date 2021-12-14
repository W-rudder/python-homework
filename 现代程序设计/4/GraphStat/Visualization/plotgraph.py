import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def plotdegree(degree):
    degreelist=[]
    for i in range(len(degree)):
        degreelist.append(int(degree[i]["节点度"]))
    sumdegree=len(degreelist)
    x=list(set(degreelist))
    y=[]
    for i in x:
        caly=degreelist.count(i)/sumdegree
        y.append(caly)
    x=np.array(x)
    y=np.array(y)
    plt.plot(x,y,ls='-', lw=0.5,  color='purple')
    plt.xlabel("节点的度")
    plt.ylabel("频率")
    plt.title("度的分布")
    plt.grid(alpha=0.5,linestyle='-.') 
    plt.show()

def plotgraph(filepath):
    mark=0
    with open(filepath,'r',encoding="utf-8") as f:
        mid=[]
        for line in f.readlines():
            if line == "*Edges\n":
                mark = 1
            elif mark == 1:
                mid.append(tuple(map(int,line.strip().split('\t'))))
    G=nx.Graph()
    G.add_weighted_edges_from(mid[:500])
    nx.draw(G,with_labels=True)
    plt.show()

    





