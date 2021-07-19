import random
import os
path = r"D:\Data_Science\Code\Lec_4\ASS_4\thanos\Universe"
img_names = os.listdir(path)  
img_names = random.sample(img_names,25)  
for ima in img_names:  
    f = os.path.join(path, ima)  
    os.remove(f)  