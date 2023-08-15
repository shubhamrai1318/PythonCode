import numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
data=pd.read_csv("../pandasuse/vns.csv")
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [463,454,437,438,438,449,440,446,444,450,453,451,463,464,457,457,458,469,483,482]
n=len(x)
predictx=list(range(1,n+1))

#y=data["Celsius"]
#y=[]

x=list(range(1,n + 1))
#predictx=x
print(n)
print(y)
pf=numpy.polyfit(x,y,1)
print(pf)
print(type(pf))
model = numpy.poly1d(pf)
drv=model.deriv()
print(type(drv))
print(model)
print(drv)
plt.title("Varanasi Temperature")
plt.scatter(x, y,color="red",linewidth=10,label="Temp data")
plt.plot(x, y,color="pink",linewidth=10,label="Temp data",alpha=0.6)
plt.plot(predictx, model(predictx),color="blue",linewidth=1,label="Predicted Data")
plt.scatter(predictx, model(predictx),color="blue",linewidth=1,label="Predicted Data")
#plt.plot(predictx, drv(predictx),color="green",linewidth=4,label="Derivative")
plt.legend()
plt.show()
