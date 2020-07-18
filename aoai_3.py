# -*- coding: utf-8 -*-
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style 
from sklearn import svm 
#Ulazni podaci 
x = [3,5,8,13,15,20,25,40,55,60,65,68,70,75,76,78,80,82,84,86,88,90,98,100,105,107,108,110]
y = [1,5,2,4,3,6,4,8,5,10,6,12,7,14,4,7,3,5,14,38,12,28,14,2,13,10,14,10]
#Grafički prikaz točaka 
plt.scatter(x,y)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#Priprema podataka za treniranje   
X = np.array([[3,1],
              [5,5],
              [8,2],
              [13,4],
              [15,3],
              [20,6],
              [25,4],
              [40,8],
              [55,5],
              [60,10],
              [65,6],
              [68,12],
              [70,7],
              [75,14],
              [76,4],
              [78,7],
              [80,3],
              [82,5],
              [84,14],
              [86,38],
              [88,12],
              [90,28],
              [98,14],
              [100,2],
              [105,13],
              [107,10],
              [108,14],
              [110,10]])
y = [0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,1,1,1,1,0,1,1,1,1]
#Pozivanje algoritma 
clf = svm.SVC(kernel = 'linear', C = 1.0)
clf.fit(X,y)
#Testiranje predikcije 
print ("T1(0.5,20) = " + str(clf.predict([[0.5,20]])))
print ("T2(5,9) = " + str(clf.predict([[5,9]])))

#Konstrukcija hiper ravnine za grafički prikaz 
w = clf.coef_[0]
print ("w = " + str(w))
a = -w[0]/w[1]
print ("a = " + str(a))
xx = np.linspace(0,112)
yy = a * xx  - clf.intercept_[0]/w[1]
#Grafički prikaz podataka
h0 = plt.plot(xx,yy, 'k-')
plt.scatter(X[:,0],X[:,1],c = y)
plt.grid(True)
plt.xlabel('x')
plt.xlim(0,112)
plt.ylabel('y')
plt.show()