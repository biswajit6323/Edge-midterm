from docutils.nodes import header
Scores=[]
fpr=open("G:\\onedrive\\Desktop\\2019.csv","r")
head=fpr.readline()
fpr_file=fpr.readline()
while(len(fpr_file)>0):
    arr = fpr_file.strip().split(',')
    Scores.append(float(arr[2]))
    fpr_file = fpr.readline()
fpr.close()
import numpy as np
Scores=np.array(Scores)
print("the average happiness score")
print(Scores.mean())
print("the lowest happiness score")
print(Scores.min())
print("the highest happiness score")
print(Scores.max())