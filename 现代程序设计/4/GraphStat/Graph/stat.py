def cal_graphavg(graphlist,edgelist):
    count = len(graphlist)
    edge =2* len(edgelist)
    avg = edge/count
    return avg

def typestat(graphlist):
    res=[]
    for i in range(len(graphlist)):
        resdict = {}
        resdict["节点id"] = graphlist[i]["节点id"]
        resdict["节点名称"] = graphlist[i]["节点名称"]
        resdict["节点类型"] = graphlist[i]["节点类型"]
        res.append(resdict)
    return res

def weighstat(graphlist):
    res=[]
    for i in range(len(graphlist)):
        resdict = {}
        resdict["节点id"] = graphlist[i]["节点id"]
        resdict["节点名称"] = graphlist[i]["节点名称"]
        resdict["节点权重"] = graphlist[i]["节点权重"]
        res.append(resdict)
    return res

def degreestat(graphlist):
    res=[]
    for i in range(len(graphlist)):
        resdict = {}
        resdict["节点id"] = graphlist[i]["节点id"]
        resdict["节点名称"] = graphlist[i]["节点名称"]
        degree=sum(list(graphlist[i]["节点连接信息"].values()))
        resdict["节点度"] = degree
        res.append(resdict)
    return(res)
    


