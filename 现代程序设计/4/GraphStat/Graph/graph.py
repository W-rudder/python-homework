import json
def init_edge(filepath):
    mark=0
    with open(filepath,'r',encoding="utf-8") as f:
        mid=[]
        for line in f.readlines():
            if line == "*Edges\n":
                mark = 1
            elif mark == 1:
                mid.append(list(line.strip().split('\t')))

    return mid

def init_graph(nodelist,edgelist):
    for i in range(len(edgelist)):

        if edgelist[i][1] in nodelist[int(edgelist[i][0])]["节点连接信息"].keys():
            nodelist[int(edgelist[i][0])]["节点连接信息"][edgelist[i][1]] += 1
        else:
            nodelist[int(edgelist[i][0])]["节点连接信息"][edgelist[i][1]] = 1
        
    return nodelist



def save_graph(graphlist):
    return json.dumps(graphlist)

def load_graph(graphlist):
    return json.loads(graphlist)
