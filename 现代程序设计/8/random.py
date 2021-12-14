import tqdm
from tqdm import tqdm
import random
import memory_profiler
import os
from playsound import playsound
import urllib.request

filepath=r"C:\Users\86186\Desktop\现代程序设计\8\result.txt"

def tqdm_decorator(func):
   def wrapper(*args,**kwargs):
      with tqdm(total=200000,desc='Example', leave=True, ncols=100, unit='B', unit_scale=True) as pbar:
         for i in range(200):
            func(*args,**kwargs)
            pbar.update(1000)
      
   return wrapper

def path_check(func):
   def wrapper(*args,**kwargs):
      if not os.path.exists(args[1]):
         print("File not found!create now.")
      f=open(args[1],'w',encoding='utf-8')
      f.close()
      return func(*args,**kwargs)
   return wrapper

def end_mark(func):
   def wrapper(*arg,**kwargs):
      func(*arg,**kwargs)
      curr_path = os.path.dirname(os.path.realpath(__file__))
      url = 'http://dict.youdao.com/dictvoice?type=0&audio=yes'
      tmp_file = 'tmp_voice.mp3'
      tmp_path =os.path.join(curr_path, tmp_file)
      urllib.request.urlretrieve(url, tmp_path)
      playsound(tmp_path)
      os.remove(tmp_path)
   return wrapper


class sort_list:
   def __init__(self,n,filepath) -> None:
       self.n=n
       self.filepath=filepath
   def random_sort(self):
      res=sorted ([random.random() for i in range (self.n)])
      with open(self.filepath,'w',encoding='utf-8') as f:
         f.write(str(res))
#@profile
#@memory_profiler.profile
#@tqdm_decorator
#@path_check
@end_mark
def test(n,filepath):
   t=sort_list(n,filepath)
   t.random_sort()

test(200000,filepath)



