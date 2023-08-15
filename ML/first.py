# import matplotlib.pyplot as plt
import math

s = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
x = [105, 104, 102, 101, 100, 99, 98, 96, 93, 92]
y = [101, 103, 100, 98, 95, 96, 104, 92, 97, 94]
# x=[1,2,3,4]
# y=[5,7,9,11]
sumx = sum(x)
sumy = sum(y)
n = len(x)
avgx = sumx / n
avgy = sumy / n
print("S = ", s)
print("x = ", x, "\t\t\tsum=", sumx)
X = [v - avgx for v in x]
print("X = ", X)
print("y = ", y, "\t\t\tsum=", sumy)
Y = [v - avgy for v in y]
print("Y = ", Y)
x2 = [v * v for v in X]
sumx2 = sum(x2)
print("X2 = ", x2, "\t\tSum = ", sumx2)
y2 = [v * v for v in Y]
sumy2 = sum(y2)
print("Y2 = ", y2, "\t\tSum = ", sumy2)
XY = [X[i] * Y[i] for i in range(n)]
sumXY = sum(XY)
print("XY = ", XY, "\tSum = ", sumXY)
# plt.plot(x,y)
# plt.plot(X,x)
# plt.scatter(Y,y)
# plt.show()
X2Y2 = math.sqrt(sumx2) * math.sqrt(sumy2)
r = sumXY / X2Y2
print("\nr = ", r)

