import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.neural_network import MLPRegressor 
from matplotlib import style 
style.use("ggplot")

x = np.arange(-4,4,0.1)
y = x**2 
plt.figure()
plt.plot(x,y, label = "f(x) = $x^2$")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

np.random.seed(0)
n = 50 
x = np.random.uniform(-15,15,size = n)
y = x**2 #+ 2*np.random.rand(n, )

plt.figure()
plt.scatter(x,y, label = "f(x) = $x^2$")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

X = np.reshape(x, [n,1])
y = np.reshape(y, [n, ])

# clf1 = MLPRegressor(alpha=0.004, hidden_layer_sizes = (30,), max_iter = 400, 
#                  activation = 'tanh', verbose = 'True', learning_rate = 'adaptive')
# clf2 = MLPRegressor(alpha=0.014, hidden_layer_sizes = (30,50,10,), max_iter = 900, 
#                  activation = 'relu', verbose = 'True', learning_rate = 'adaptive')
# clf3 = MLPRegressor(alpha=0.024, hidden_layer_sizes = (30,), max_iter = 1400, 
#                  activation = 'tanh', verbose = 'True', learning_rate = 'adaptive')
# clf4 = MLPRegressor(alpha=0.034, hidden_layer_sizes = (30,50,10,), max_iter = 1900, 
#                  activation = 'relu', verbose = 'True', learning_rate = 'adaptive')
# clf5 = MLPRegressor(alpha=0.044, hidden_layer_sizes = (30,), max_iter = 2400, 
#                  activation = 'tanh', verbose = 'True', learning_rate = 'adaptive')
# clf6 = MLPRegressor(alpha=0.054, hidden_layer_sizes = (30,50,10,), max_iter = 2900, 
#                  activation = 'relu', verbose = 'True', learning_rate = 'adaptive')
# clf7 = MLPRegressor(alpha=0.064, hidden_layer_sizes = (30,), max_iter = 3400, 
#                  activation = 'relu', verbose = 'True', learning_rate = 'adaptive')
# clf8 = MLPRegressor(alpha=0.074, hidden_layer_sizes = (30,50,10), max_iter = 3900, 
#                  activation = 'relu', verbose = 'True', learning_rate = 'adaptive')
# clf9 = MLPRegressor(alpha=0.084, hidden_layer_sizes = (30,28,10), max_iter = 4400, 
#                  activation = 'relu', verbose = 'True', learning_rate = 'adaptive')
# clf10 = MLPRegressor(alpha=0.094, hidden_layer_sizes = (30,50,10), max_iter = 4900, 
#                  activation = 'relu', verbose = 'True', learning_rate = 'adaptive')
clf11 = MLPRegressor(alpha=0.104, hidden_layer_sizes = (30,25,10), max_iter = 5400, 
                 activation = 'relu', verbose = 'True', learning_rate = 'adaptive')

# a = clf1.fit(X, y)
# a = clf2.fit(X, y)
# a = clf3.fit(X, y)
# a = clf4.fit(X, y)
# a = clf5.fit(X, y)
# a = clf6.fit(X, y)
# a = clf7.fit(X, y)
# a = clf8.fit(X, y)
# a = clf9.fit(X, y)
# a = clf10.fit(X, y)
a = clf11.fit(X, y)
x_ = np.linspace(-10, 10, 1600) 
pred_x = np.reshape(x_, [1600, 1]) 
# pred_y = clf1.predict(pred_x)
# pred_y = clf2.predict(pred_x)
# pred_y = clf3.predict(pred_x)
# pred_y = clf4.predict(pred_x)
# pred_y = clf5.predict(pred_x)
# pred_y = clf6.predict(pred_x)
# pred_y = clf7.predict(pred_x)
# pred_y = clf8.predict(pred_x)
# pred_y = clf9.predict(pred_x)
# pred_y = clf10.predict(pred_x)
pred_y = clf11.predict(pred_x) 
plt.figure() 
plt.plot(x_, x_**2, color = 'b', label = "$f_{original}$(x) = $x^2$") # plot original function
plt.plot(pred_x, pred_y, color = 'r', label = "$f_{ann}$(x)")  # plot network output
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()