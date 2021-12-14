from PIL import Image,ImageFilter
from matplotlib import pyplot as plt
import os

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

picpath=r"C:\Users\86186\Desktop\现代程序设计\6\images"
resultpath=r"C:\Users\86186\Desktop\现代程序设计\6\result"

class Filter:
    def __init__(self,image) -> None:
        self.parmlist=[]
        self.im=image
    
    def filter(self):
        pass

class Edgefilter(Filter):
    def __init__(self, image) -> None:
        self.im=image

    def filter(self):
        self.im=self.im.filter(ImageFilter.FIND_EDGES)
        #self.im.show()
        return self.im

class Sharpenfilter(Filter):
    def __init__(self, image) -> None:
        self.im=image

    def filter(self):
        self.im=self.im.filter(ImageFilter.SHARPEN)
        #self.im.show()
        return self.im

class Blurfilter(Filter):
    def __init__(self, image) -> None:
        self.im=image

    def filter(self):
        self.im=self.im.filter(ImageFilter.BLUR)
        #self.im.show()
        return self.im

class resizefilter(Filter):
    def __init__(self, image) -> None:
        self.im=image

    def filter(self,m,n):
        self.im=self.im.resize((m,n))
        #self.im.show()
        return self.im

class Contourfilter(Filter):
    def __init__(self, image) -> None:
        self.im=image

    def filter(self):
        self.im=self.im.filter(ImageFilter.CONTOUR)
        #self.im.show()
        return self.im

class Edge_enhancefilter(Filter):
    def __init__(self, image) -> None:
        self.im=image

    def filter(self):
        self.im=self.im.filter(ImageFilter.EDGE_ENHANCE_MORE)
        #self.im.show()
        return self.im


class ImageShop:
    def __init__(self,path):
        self.info={}
        self.info["path"]=path
        self.info["images_list"]=[]
        self.info["images_dealt"]=[]

    def load_images(self,*ptype):
        type_list=list(ptype)
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
    
    def __batch_ps(self,filterway,*arg):
        ways_list=["BLUR","RESIZE","SHARPEN","EDGE","CONTOUR","EDGE-ENHANCE"]
        if filterway not in ways_list:
            print("filter not exist")
        else:
            if filterway == ways_list[0]:
                if self.info["images_dealt"] == []:
                    for j in self.info["images_list"]:
                        self.info["images_dealt"].append(Blurfilter(j).filter())
                else:
                    length=len(self.info["images_dealt"])
                    for i in range(length):
                        self.info["images_dealt"][i] = resizefilter(self.info["images_dealt"][i]).filter()
            elif filterway == ways_list[1]:
                if self.info["images_dealt"] == []:
                    for j in self.info["images_list"]:
                        self.info["images_dealt"].append(resizefilter(j).filter(arg[0],arg[1]))
                else:
                    length=len(self.info["images_dealt"])
                    for i in range(length):
                        self.info["images_dealt"][i] = resizefilter(self.info["images_dealt"][i]).filter(arg[0],arg[1])
            elif filterway == ways_list[2]:
                if self.info["images_dealt"] == []:
                    for j in self.info["images_list"]:
                        self.info["images_dealt"].append(Sharpenfilter(j).filter())
                else:
                    length=len(self.info["images_dealt"])
                    for i in range(length):
                        self.info["images_dealt"][i] = Sharpenfilter(self.info["images_dealt"][i]).filter()
            elif filterway == ways_list[3]:
                if self.info["images_dealt"] == []:
                    for j in self.info["images_list"]:
                        self.info["images_dealt"].append(Edgefilter(j).filter())
                else:
                    length=len(self.info["images_dealt"])
                    for i in range(length):
                        self.info["images_dealt"][i] = Edgefilter(self.info["images_dealt"][i]).filter()
            elif filterway == ways_list[4]:
                if self.info["images_dealt"] == []:
                    for j in self.info["images_list"]:
                        self.info["images_dealt"].append(Contourfilter(j).filter())
                else:
                    length=len(self.info["images_dealt"])
                    for i in range(length):
                        self.info["images_dealt"][i] = Contourfilter(self.info["images_dealt"][i]).filter()
            elif filterway == ways_list[5]:
                if self.info["images_dealt"] == []:
                    for j in self.info["images_list"]:
                        self.info["images_dealt"].append(Edge_enhancefilter(j).filter())
                else:
                    length=len(self.info["images_dealt"])
                    for i in range(length):
                        self.info["images_dealt"][i] = Edge_enhancefilter(self.info["images_dealt"][i]).filter()
    
    def batch_ps(self,*arg):
        for i in arg:
            if isinstance(i,tuple) and i[0] == "RESIZE":
                ImageShop.__batch_ps(self,i[0],int(i[1]),int(i[2]))
            else:
                ImageShop.__batch_ps(self,i)

    def display(self,*arg):
        if os.path.isfile(self.info["path"]):
            self.info["images_list"][0].show()
        else:
            max=len(self.info["images_dealt"])
            m=arg[0]
            n=arg[1]
            if max > m*n:
                for i in range(1,m*n+1):
                    plt.subplot(m,n,i)
                    plt.imshow(self.info["images_dealt"][i-1])
                    plt.xticks([])
                    plt.yticks([])
                    plt.axis('off')
                plt.show()
            else:
                for i in range(1,max+1):
                    plt.subplot(m,n,i)
                    plt.imshow(self.info["images_dealt"][i-1])
                    plt.xticks([])
                    plt.yticks([])
                    plt.axis('off')
                plt.show()




    def save(self,path,mode = 0):
        if mode == 0:
            if len(self.info["images_dealt"]) == 1:
                self.info["images_dealt"][0].save(os.path.join(path,self.info["image_type"]))
            else:
                for i in range(len(self.info["images_dealt"])):
                    self.info["images_dealt"][i].save(os.path.join(path,self.info["images_type"][i]))
        else:
            if len(self.info["images_dealt"]) == 1:
                self.info["images_dealt"][0].save(os.path.join(path,os.path.splitext(self.info["image_type"])[0]),mode)
            else:
                for i in range(len(self.info["images_dealt"])):
                    self.info["images_dealt"][i].save(os.path.join(path,os.path.splitext(self.info["images_type"][i])[0])+"."+mode)

class TestImageShop:
    def __init__(self) -> None:
        self.t=ImageShop(picpath)

    def loadtest(self):
        self.t.load_images(".jpg")
        print(self.t.info)

    def displaytest(self):
        self.t.batch_ps("BLUR",("RESIZE",300,500))
        self.t.display(3,3)

    def savetest(self):
        self.t.save(resultpath,"png")

s=TestImageShop()
s.loadtest()
s.displaytest()
s.savetest()


