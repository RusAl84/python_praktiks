import numpy as np
a=np.zeros((4,4))
print(a)
a=a+1
a=a*7
a[1][1]=0
b=a
a[0][0]=100
a[1][1]=1000
print(b)