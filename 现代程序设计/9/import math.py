import numpy as np
import os
from PIL import Image

filepath = r"C:\Users\86186\Desktop\现代程序设计\originalPics"

def random_walk(mu,X_0,sigma,N):
    count = 0
    X_b = X_0
    while(count<N):
        Norm=np.random.normal(loc=0,scale=sigma,size=1)
        X_a=mu+X_b+Norm
        yield X_a
        X_b = X_a
        count += 1
    return None

class FaceDataset:
    def __init__(self,filepath) -> None:
        self.filepath = filepath
        self.photo_list = []
        self._n= 0

    def ptoto_list_generate(self,filepath):
        for a,b,c in os.walk(filepath):
            if b==[]:
                for i in c:
                    self.photo_list.append(os.path.join(a,i))

    def transform_to_ndarray(self,img):
        return np.array(img)
    
    def __iter__(self):
        return self

    def __next__(self):
        if self._n < len(self.photo_list):
            img=Image.open(self.photo_list[self._n])
            self._n += 1
            print(self.transform_to_ndarray(img))
        else:
            raise StopIteration('大于max:{}'.format(len(self.photo_list)))


#if __name__ =="__main__":
#    r=random_walk(3,5,3,5)
#    while True:
#        try:
#            print(next(r))
#        except StopIteration as si:
#            print(si.value)
#            break
    
#    r1=random_walk(3,5,3,10)
#    r2=random_walk(3,6,4,10)
#    while True:
#        try:
#            print(next(zip(r1,r2)))
#        except StopIteration as si:
#            print(si.value)
#            break

fd=FaceDataset(filepath)
fd.ptoto_list_generate(filepath)
fditer=iter(fd)
for i in range(100):
    next(fditer)

 

