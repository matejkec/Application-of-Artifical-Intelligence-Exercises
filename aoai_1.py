import numpy as np 
import matplotlib.pyplot as plt 

def Sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.arange(-5,5,0.1)
y = list()
for i in range(0, len(x)):
    y.append(Sigmoid(x[i]))  
    
#Crtanje sigmoid aktivacijske funckije 
plt.figure() 
plt.plot(x,y,label = "Sigmoid activation function" )
plt.xlabel("X")
plt.ylabel("Sigmoid(x)")
plt.grid(True)
plt.legend()
plt.show()

#ulazni podaci
X = np.array([[1,1,1,0,0,0],
              [1,1,0,0,0,0],
              [1,1,1,0,0,0],
              [1,0,1,1,1,1],
              [1,0,1,1,1,1],
              [1,0,0,1,1,1],
              [1,1,1,0,0,0],
              [1,0,1,1,1,1],
              [1,1,1,0,0,0],
              [1,0,1,1,1,1],
              [0,1,1,0,0,0],
              [0,1,0,0,0,0],
              [0,1,1,0,0,0],
              [0,0,0,1,1,1],
              [0,0,1,1,1,1],
              [0,0,0,1,1,1],
              [0,1,1,0,0,0],
              [0,1,1,0,0,0]])

#Izlazni podaci 
y = np.array([[1,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,1,1]]).T
np.random.seed(1)
#Inicijaliziraj težinkse faktore 
syn0 = 2*np.random.random((6,1)) - 1 
noOfIterations = np.arange(0,100000,1)

OutValues = [[] for i in range(18)]

syn0_1 = list()
for i in range(0,len(noOfIterations)):
    l0 = X 
    l1 = Sigmoid(np.dot(l0, syn0))
    print("l1 = " + str(l1))
    for i in range(18):
        OutValues[i].append(l1[i])

    l1_error = y - l1
    print("l1_error = " + str(l1_error))
    l1_delta = l1_error * Sigmoid(l1)
    print("l1_delta = " + str(l1_delta))
    syn0_1.append(syn0[0])
    syn0 += np.dot(l0.T, l1_delta)
    print("Syn0_1 = " + str(syn0[0]))

print ("Output After Training: " )
print (l1 )
print ("Weight Factors After Training: " )
print (syn0)


#Prikaz promjene izračunate (izlazne) vrijednosti iz aktivacijske funkcije
#tijekom postupka učenja
plt.figure()
for i in range(18):
    plt.plot(noOfIterations, OutValues[i], label = "OutValue"+str(i+1))
plt.xlabel("Number of Iterations")
plt.xlim(0,100)
plt.ylabel("OutValue")
plt.grid(True)
plt.legend()
plt.show()