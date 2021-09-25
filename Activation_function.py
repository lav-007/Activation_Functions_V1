import numpy as np
import matplotlib.pyplot as plt
def plotter_fun(x,y,diff_y,fun_name):
    x_label='Vk'
    y_label='y'
    plt.plot(x,y,label='Function')
    plt.plot(x,diff_y,label='Diff_function')
    plt.grid()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(fun_name)
    plt.legend()
    plt.show()

def binary_fun(x):
    y=[]
    y1=[]
    k=0
    fun_name='binary function'
    for i in x:
        if i<0:
            k=0
            k1=0
        elif i>0:
            k=1
            k1=0
        y.append(k)
        y1.append(k1)
    return y,y1,fun_name

def sigmoid_fun(x):
    fun_name='sigmoid_fun'
    y=1/(1+np.exp(-x))
    y1=np.exp(-x)/((1+np.exp(-x))**2)
    return y,y1,fun_name

def tanh_fun(x):
    y=0
    diff_y=0
    fun_name='Tanh_function'
    y=(np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
    diff_y=4/((np.exp(x)+np.exp(-x))**2)
    return y,diff_y,fun_name

x=np.linspace(-10,10,1000)

y,y1,fun_name=sigmoid_fun(x)

plt.plot(x,y,label='Function')
plt.plot(x,y1,label='Diff_function')
plt.title(fun_name)
plt.grid()
plt.legend()
plt.show()
