# -*- coding: utf-8 -*-
"""
@author: Ali HP.J - shiraz University
"""


import numpy as np
from sklearn.model_selection import LeaveOneOut
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt


class Struct():
    pass;
def Classifiers(numSamples, SelectedFeatures):
    
    neigh = KNeighborsClassifier(n_neighbors=5)
    AccTest= np.zeros([numSamples,1]);
    AccTrain= np.zeros([numSamples,1]);
    
    PredictLabel= np.zeros([numSamples,1]);
    ind=0;
    for train_index, test_index in loo.split(SelectedFeatures):
        X_train, X_test = SelectedFeatures[train_index], SelectedFeatures[test_index];
        y_train, y_test = Labels[train_index], Labels[test_index];
        
        neigh.fit(X_train, y_train);
            
        AccTrain[ind] = accuracy_score(y_train, neigh.predict(X_train));
        
        PredictLabel[ind]= neigh.predict(X_test);
        AccTest[ind] = accuracy_score(y_test, PredictLabel[ind]);
            
        ind+=1;
    F1= f1_score(Labels, PredictLabel, average='macro');
    return np.mean(AccTest), np.mean(AccTrain), F1;


## Start
# DatasetsName= ['Breast','COIL20','ORL','Musk1'];
DatasetsName= ['Colon'];

NumDatasets= len(DatasetsName);

Data= [Struct() for i in range(NumDatasets)];
for i in range(NumDatasets):
    Data[i]= np.loadtxt(DatasetsName[i]+'.txt',dtype= float, delimiter=',');

FeatureSets1_1= [Struct() for i in range(NumDatasets)]; 
FeatureSets1_2= [Struct() for i in range(NumDatasets)]; 
FeatureSets1_3= [Struct() for i in range(NumDatasets)]; 
FeatureSets1_4= [Struct() for i in range(NumDatasets)]; 
FeatureSets1_5= [Struct() for i in range(NumDatasets)]; 
for i in range(NumDatasets):
    FeatureSets1_1[i]= np.loadtxt(DatasetsName[i]+'_01D.txt',dtype= int, delimiter=',');
    FeatureSets1_2[i]= np.loadtxt(DatasetsName[i]+'_02D.txt',dtype= int, delimiter=',');
    FeatureSets1_3[i]= np.loadtxt(DatasetsName[i]+'_03D.txt',dtype= int, delimiter=',');
    FeatureSets1_4[i]= np.loadtxt(DatasetsName[i]+'_04D.txt',dtype= int, delimiter=',');
    FeatureSets1_5[i]= np.loadtxt(DatasetsName[i]+'_05D.txt',dtype= int, delimiter=',');
   
    

loo = LeaveOneOut();

AccTest_S1=[Struct() for i in range(NumDatasets)];   
AccTrain_S1=[Struct() for i in range(NumDatasets)];  
F1_S1=[Struct() for i in range(NumDatasets)];



TempData= Data[0];
numSamples, numFeatures= TempData.shape;
Labels= TempData[:,numFeatures-1];
#AccTest_S1[0], AccTrain_S1[0], F1_S1[0] = Classifiers(numSamples, TempData[:,FeatureSets1_1[0]].reshape(-1, 1));
#AccTest_S2[0], AccTrain_S2[0], F1_S2[0] = Classifiers(numSamples, TempData[:,FeatureSets2_1[0]].reshape(-1, 1));

for i in range(NumDatasets):
    print("Date set:",DatasetsName[i])

    TempData= Data[i];
    numSamples, numFeatures= TempData.shape;
    Labels= TempData[:,numFeatures-1];
    
    AccTest_S1[i], AccTrain_S1[i], F1_S1[i] = Classifiers(numSamples, TempData[:,FeatureSets1_5[i]]);## you sould change
    
    
    print('acctest',AccTest_S1[i])
    print('acctrain',AccTrain_S1[i])
    print('F1',F1_S1[i])
    print('---------------')
    

    test=1;


N = NumDatasets
Train1 = tuple(AccTrain_S1);

Test1 = tuple(AccTest_S1);

F1 = tuple(F1_S1);


ind = np.arange(N) 
width = 0.35 
plt.figure(1)      
plt.bar(ind, Train1, width)


plt.ylabel('Train Accuracy')
plt.title('Train Accuracy for each Dataset base on 50 percent')
plt.grid(True)
plt.xticks(ind + width / 2, DatasetsName)
plt.legend(loc='best')
plt.show()



ind = np.arange(N) 
width = 0.35       
plt.figure(2) 
plt.bar(ind, Test1, width)


plt.ylabel('Test Accuracy')
plt.title('Test Accuracy for each Dataset base on 50 percent')
plt.grid(True)
plt.xticks(ind + width / 2, DatasetsName)
plt.legend(loc='best')
plt.show()



ind = np.arange(N) 
width = 0.35   
plt.figure(3)     
plt.bar(ind, F1, width)


plt.ylabel('F1')
plt.title('F1 for each Dataset base on 50 percent')
plt.grid(True)
plt.xticks(ind + width / 2, DatasetsName)
plt.legend(loc='best')
plt.show()

