from multiprocessing import Process
from multiprocessing import Queue
import os
import jieba
import re
import math
import pickle
from tqdm import tqdm
import collections
import time

filepath = r"C:\Users\86186\Desktop\现代程序设计\11\news_sohusite_xml.dat"
respath=r"C:\Users\86186\Desktop\现代程序设计\11"
txtlist = []

def give_out(filepath,process_num):
    global txtlist
    i=1
    with open(filepath,'r',encoding='ansi') as f:
        for line in f.readlines():
            if i % 6 == 5:
                txtlist.append(line.strip())
            i += 1
    #txtlist=txtlist[:100]
    length = len(txtlist)
    n=int(math.ceil(length/process_num))
    return n


def map_task(n,count,q,txtlist):
    res = {}
    start = n*count
    end = n*(count+1)
    pattern = '[(<content>)(</content>)]'
    jieba.setLogLevel(jieba.logging.INFO)
    for i in range(start,end):
        if i < len(txtlist):
            line =re.sub(pattern,'',txtlist[i])
            data = jieba.lcut(line)
            for j in data:
                if '\u4e00'<= j <='\u9fff':
                    if j not in res.keys():
                        res[j] = 1
                    else:
                        res[j] += 1
    with open(os.path.join(respath,"map_result{}.txt".format(count)),'wb') as f:
        pickle.dump(res,f)
    q.put(os.path.join(respath,"map_result{}.txt".format(count)))




class Map(Process):
    def __init__(self,n,count,q,txtlist) -> None:
        super().__init__()
        self.n = n
        self.count = count
        self.q = q
        self.txtlist = txtlist

    def run(self):
        print("Map Process {} starts.".format(self.count))
        map_task(self.n,self.count,self.q,self.txtlist)
        print("Map Process {} ends.".format(self.count))


class Reduce(Process):
    def __init__(self,q,process_num) -> None:
        super().__init__()
        self.q = q
        self.process_num = process_num
        self.result={}

    def run(self):
        print("Reduce process is runing...")
        pbar = tqdm(total=self.process_num,desc="Reduce")
        while not self.q.empty():
            path = self.q.get()
            with open(path,'rb') as f:
                res = pickle.load(f)
            for i in res.keys():
                if i in self.result.keys():
                    self.result[i] += res[i]
                else:
                    self.result[i] = res[i]
            pbar.update(1)
        pbar.close()
        self.result=dict(collections.OrderedDict(sorted(self.result.items(),key=lambda dc:dc[1],reverse=True)))
        with open(os.path.join(respath,"result.txt"),'w+',encoding='ansi') as f:
            for m,n in self.result.items():
                f.write(m+':'+str(n)+'\n')
        print("Reduce process finished.")



if __name__ == "__main__":
    a=time.time()
    p_list=[]
    process_num = 2
    q=Queue(process_num)
    n=give_out(filepath,process_num)
    for i in range(process_num):
        p=Map(n,i,q,txtlist)
        p_list.append(p)
    for i in p_list:
        i.start()
    for i in p_list:
        i.join()
    b=time.time()
    r=Reduce(q,process_num)
    r.start()
    r.join()
    print("time:{:.0f}min{:.0f}s".format((b-a)//60,(b-a)%60))
    
    