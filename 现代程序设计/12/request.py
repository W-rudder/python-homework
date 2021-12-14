# coding = utf-8
from threading import Thread, Condition,currentThread
import random
import requests
import json
from lxml import etree
from pprint import pprint


con=Condition()
q=[]


def consume():
	with con:
		con.wait_for()
		print("%s consume %s" %(currentThread().name,q.pop()))

def produce():
	with con:
		for i in range(2):
			q.append(random.random())
		con.notify_all()

class Produce(Thread):
    def __init__(self) -> None:
        super().__init__()
        self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
        self.url= "https://music.163.com/playlist?id=2695101341"
    def run(self):
        response = requests.get(self.url,headers=self.headers)
        with open(r'.\wangyi.html','w',encoding='utf-8') as f:
            f.write(response.content.decode())

        

if __name__ == '__main__':
    p=Produce()
    p.run()

"""clist=[]
for i in range(20):
	c=Thread(target=consume,name='c-'+str(i+1))
	clist.append(c)
plist=[]
for i in range(20):
	p=Thread(target=produce,name='p-'+str(i+1))
	plist.append(p)
for c in clist:
	c.start()
for p in plist:
	p.start()"""