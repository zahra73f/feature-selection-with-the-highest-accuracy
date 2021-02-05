"""
@author: zahra fathollahi - shiraz University
"""
import numpy as np
from pyitlib import discrete_random_variable as drv
import random as rn
from random import randrange
import math  

def calculate(i,j,selected_index,thisdict):

    if (i,int(selected_index[j])) in thisdict:
        tt=thisdict[i,int(selected_index[j])]
    else:
        cond_inf=drv.information_mutual_conditional(featurs[i],Y,featurs[int(selected_index[j])])
        d=[featurs[i],Y,featurs[int(selected_index[j])]]
        
        intraction_inf=drv.information_interaction(d)
        tt=cond_inf-intraction_inf
        thisdict[i,int(selected_index[j])]=tt

    return tt


def writeInFile(selected_index):
    a1=selected_index[0:round(0.1*len(featurs))];
    b1=selected_index[0:round(0.2*len(featurs))];
    c1=selected_index[0:round(0.3*len(featurs))];
    d1=selected_index[0:round(0.4*len(featurs))];
    e1=selected_index[0:round(0.5*len(featurs))];

    np.savetxt(file_name + '_01D.txt', a1, delimiter=',')
    np.savetxt(file_name + '_02D.txt', b1, delimiter=',')
    np.savetxt(file_name + '_03D.txt', c1, delimiter=',')
    np.savetxt(file_name + '_04D.txt', d1, delimiter=',')
    np.savetxt(file_name + '_05D.txt', selected_index, delimiter=',')


file_name = 'Colon'
Data=np.loadtxt(file_name+'.txt', dtype=int, delimiter=',')
print("Data set ",file_name ," is running")
numRow=len(Data)
numColumn=len(Data.T)
datat=Data.T
Y=datat[numColumn-1]
featurs=datat[0:numColumn-1]

print("features number:",len(featurs))
k=math.ceil(0.5*len(featurs))
mu_inf=np.zeros(len(featurs),)
selected_index=np.zeros(k,)
selected_index[:,]=50000
for i in range(len(featurs)):
    x=featurs[i]
    mu_inf[i]=drv.information_mutual(x,Y)
#select first featur
selected_index[0]=np.argmax(mu_inf)
#select other featur
Jfunc=np.zeros(len(featurs),)
Jfunc[:,]=-10000
kk=1
thisdict =	{
  (50000,2): 1.25,
}

while kk<k :
    list_selectd=list(selected_index)
    t=list_selectd.count(50000)
    numSeleted=len(selected_index)-t
    for i in range(len(featurs)):

        if i not in selected_index:
            Jfunc[i]=0
            for j in range(0, numSeleted, 3):

                tt1 = calculate(i,j,selected_index,thisdict)
                Jfunc[i]+=tt1
                
                if j+1 <numSeleted:
                    tt2 = calculate(i,j+1,selected_index,thisdict)
                    Jfunc[i]+=tt2

                if j+2 <numSeleted:
                    tt3 = calculate(i,j+2,selected_index,thisdict)
                    Jfunc[i]+=tt3


    selected_index[kk]=np.argmax(Jfunc)
    #print(selected_index)
    Jfunc[:,]=-1000
    print(kk)
    kk+=1            

print(selected_index)
    
writeInFile(selected_index)

print('don!')
