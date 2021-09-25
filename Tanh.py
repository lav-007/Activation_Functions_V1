def tanh_fun(x):
    y=0
    diff_y=0
    fun_name='Tanh_function'
    y=(np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
    diff_y=4/((np.exp(x)+np.exp(-x))**2)
    return y,diff_y,fun_name

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
