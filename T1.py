import numpy as np
from datetime import datetime as datetime

a=np.random.randn(100)
b=np.random.randn(100)
T=10000

def slow_dot_product(a,b):
    result=0
    for e,f in zip(a,b) :
         result+=e*f
    return result
t0=datetime.now()
for t in range(T):
    A=slow_dot_product(a,b)
dt1=datetime.now()-t0
def fast_product(a,b):
    for t in range(T):
        B=a.dot(b)
    return B
t0=datetime.now()
B=fast_product(a,b)
dt2=datetime.now()-t0
print(dt1.total_seconds())
print("dt1/dt2:=", dt1.total_seconds()/dt2.total_seconds())
