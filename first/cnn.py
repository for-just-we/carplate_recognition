import os
import numpy as np
import random

#dir = 'E:/MyDownloads/images/cnn_plate_train'

#result = np.random.choice(1000,100,replace=False)

#num = []
#for i in range(1500):
    #n = random.randint(1,2000)
    #num.append(n)

n=np.array([0.01,0.02,0.1,0.9,0.2,0.6,0.89])

c=n.astype(int)
print(c)
#def list_all_files(root):
    #files = []
    #list = os.listdir(root)
    #for i in range(len(list)):
        #element = os.path.join(root, list[i])
        #if os.path.isdir(element):
            #files.extend(list_all_files(element))
        #elif os.path.isfile(element):
            #files.append(element)
    #return files

#files = list_all_files(dir)
#for file in files:
   # print (file)

#labels = [os.path.split(os.path.dirname(file))[-1] for file in files]

#for label in labels:
    #print (label)


