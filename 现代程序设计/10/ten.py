import abc
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import wordcloud
import collections
import jieba
from tqdm import tqdm
import os
from PIL import Image,ImageFilter
import imageio
import cv2


stopwords_file=r"C:\Users\86186\Desktop\现代程序设计\stopwords_list.txt"
filepath=r"C:\Users\86186\Desktop\现代程序设计\jd_comments.txt"
picpath=r"C:\Users\86186\Desktop\现代程序设计\6\images"
gifpath=r"C:\Users\86186\Desktop\现代程序设计\10\gif-sources"
videopath=r"C:\Users\86186\Desktop\现代程序设计\10\video.mp4"
vcresultpath=r"C:\Users\86186\Desktop\现代程序设计\10\vcresult"

class Plotter(abc.ABC):
    @abc.abstractclassmethod
    def plot(self,data, *args, **kwargs):
        pass

class PointPlotter(Plotter):

    def plot(self, data, *args, **kwargs):
        x=[]
        y=[]
        for i in data:
            x.append(i[0])
            y.append(i[1])
        x=np.array(x)
        y=np.array(y)
        plt.scatter(x,y)
        plt.show()

class ArrayPlotter(Plotter):
    def plot(self, data, *args, **kwargs):
        fig = plt.figure()
        v=len(data)
        if v == 2:
            ax=plt.axes()
            x=np.array(data[0])
            y=np.array(data[1])
            ax.scatter(x,y)
            plt.show()
        
        elif v == 3:
            ax = Axes3D(fig)
            x=np.array(data[0])
            y=np.array(data[1])
            z=np.array(data[2])
            ax.scatter3D(x,y,z)
            plt.show()

class TextPlotter(Plotter):
    def stopwordslist(self):
        self.stopwords=[]
        with open(stopwords_file,"r",encoding='utf-8') as sw:
            for line in sw.readlines():
                self.stopwords.append(line.strip())

    def word_depart(self,filepath):
        jieba.load_userdict(r"C:\Users\86186\AppData\Local\Programs\Python\Python37\Lib\site-packages\jieba\dict1.txt")
        
        res={}
        self.stopwordslist()
        stopwords=self.stopwords
        with open(filepath,"r",encoding='utf-8') as f:
            pbar=tqdm(total=1000)
            for line in f.readlines():
                data1=jieba.lcut(line.strip())
                for i in data1:
                    if i not in stopwords:
                        if i in res.keys():
                            res[i] += 1
                        else:
                            res[i] = 1
                pbar.update(1)
            pbar.close()
        self.depart_res=collections.OrderedDict(sorted(res.items(),key=lambda dc:dc[1],reverse=True))

    def plot(self, data, *args, **kwargs):
        self.word_depart(data)
        wc = wordcloud.WordCloud(
            font_path='C:/Windows/Fonts/simhei.ttf', 
            max_words=150,      
            max_font_size=100,   
            background_color='white'
        )
        wc.generate_from_frequencies(self.depart_res) 
        plt.imshow(wc) 
        plt.axis('off') 
        plt.show() 

class ImagePlotter(Plotter):
    def __init__(self):
        self.info={}
        
        self.info["images_list"]=[]

    def load_images(self,path,**kwargs):
        self.info["path"]=path
        type_list=list(kwargs["ptype"])
        if os.path.isfile(self.info["path"]):
            a,b=os.path.split(self.info["path"])
            m,n=os.path.splitext(b)
            if n in type_list:
                self.info["images_list"].append(Image.open(self.info["path"]))
                self.info["image_type"]=b

        elif os.path.isdir(self.info["path"]):
            self.info["images_type"]=[]
            for dirpath,dirnames,files in os.walk(self.info["path"]):
                for file in files:
                    f,e = os.path.splitext(file)
                    if e in type_list:
                        self.info["images_list"].append(Image.open(os.path.join(self.info["path"],file)))
                        self.info["images_type"].append(file)

    def plot(self, data, *args, **kwargs):
        self.load_images(data,**kwargs)
        if os.path.isfile(self.info["path"]):
            self.info["images_list"][0].show()
        else:
            max=len(self.info["images_list"])
            m=args[0]
            n=args[1]
            if max > m*n:
                for i in range(1,m*n+1):
                    plt.subplot(m,n,i)
                    plt.imshow(self.info["images_list"][i-1])
                    plt.xticks([])
                    plt.yticks([])
                    plt.axis('off')
                plt.show()
            else:
                for i in range(1,max+1):
                    plt.subplot(m,n,i)
                    plt.imshow(self.info["images_list"][i-1])
                    plt.xticks([])
                    plt.yticks([])
                    plt.axis('off')
                plt.show()

class GifPlotter(Plotter):
    def plot(self, data, *args, **kwargs):
        files=os.listdir(data)
        files.sort(key=lambda x:int(x[3:5]))
        length=len(files)
        frames=[]
        for i in range(length):
            frames.append(imageio.imread(os.path.join(data,files[i])))
        imageio.mimsave(args[0], frames, 'GIF', duration =args[1])

class video_to_gif_Plotter(Plotter):
    def cv_imwrite(self,file_path, frame): 
        cv2.imencode('.jpg', frame)[1].tofile(file_path)

    def plot(self, data, *args, **kwargs):
        vc = cv2.VideoCapture(data)
        n = 1
        
        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False
        
        timeF = args[0]
        
        i = 0
        while(rval):
            if (n % timeF == 0):
                i += 1
                self.cv_imwrite(os.path.join(vcresultpath,"res{:0=2}.jpg".format(i)),frame)
            n = n + 1
            rval, frame = vc.read()  
        vc.release()

        duration=timeF/60
        p=GifPlotter()
        p.plot(vcresultpath,"result.gif",duration)


"""ls=[(1,2,2),(2,3,2),(3,5,3)]
p=ArrayPlotter()
p.plot(ls)"""

"""p=TextPlotter()
p.plot(filepath)"""

"""p=ImagePlotter()
p.plot(picpath,3,3,ptype=(".jpg",))"""

"""p=GifPlotter()
p.plot(gifpath,"result.gif",0.2)"""

p=video_to_gif_Plotter()
p.plot(videopath,12)