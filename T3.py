# Open CSV and load data
import numpy as np
x=[]
for line in open('G:\IET_LKO\Semester I\B.Tech III\Lecture Series\Introduction to Programming with python\machine_learning_examples-master\machine_learning_examples-master\linear_regression_class\data_2d.csv'):
    raw=line.split(',')
    sample=list(map(float,raw))
    x.append(sample)
x=np.array(x)
print(x.shape)
