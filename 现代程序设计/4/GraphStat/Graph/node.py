
def init_node(filepath):
    res=[]
    with open(filepath,'r',encoding="utf-8") as f:
        for line in f.readlines():
            if line == "*Vertices 34282\n":
                continue
            elif line =="*Edges\n":
                break
            else:
                dict={}
                infor=list(line.strip().split('\t'))
                dict["节点id"]=infor[0]
                dict["节点名称"]=infor[1]
                dict["节点权重"]=infor[2]
                dict["节点类型"]=infor[3]
                dict["节点其他信息"]=infor[4]
                dict["节点连接信息"]={}
                res.append(dict)
    return res

def print_node(nodelist):
    for i in range(len(nodelist)):
        print("id:{}\nname:{}\nweigh:{}\nnodetype:{}\notherinformation:{}".format(nodelist[i]["节点id"],nodelist[i]["节点名称"],nodelist[i]["节点权重"],nodelist[i]["节点类型"],nodelist[i]["节点其他信息"]))



