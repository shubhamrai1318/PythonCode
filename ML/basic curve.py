from matplotlib import pyplot as plt

def f(x, m, c):
    return m * x + c

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21,22,23,24,25,26,27,28,29,30]
n = len(x)
y = [429,429,431,431,429,431,432,432,433,443,463, 454, 437, 438, 438, 449, 440, 446, 444, 450, 453, 451, 463, 464, 457, 457, 458, 469, 483, 482]
sumx = sum(x)
sumy = sum(y)
avgx = sum(x) / n
avgy = sum(y) / n
dx = [v - avgx for v in x]
dy = [v - avgy for v in y]
sigmadx = sum(dx)
sigmady = sum(dy)
dxdy = [dx[i] * dy[i] for i in range(n)]
# print(dxdy)
dxdx = [v * v for v in dx]
# print(dxdx)
dydy = [v * v for v in dy]
sigmadxdy = sum(dxdy)
sigmadxdx = sum(dxdx)
sigmadydy = sum(dydy)
n = len(x)
num = (sigmadxdy - sigmadx * sigmady / n)
den = (sigmadxdx - sigmadx * sigmadx / n)
m = num / den
c = avgy - m * avgx
inputx = [x for x in range(1, n + 3)]
inputy = [f(x, m, c) for x in inputx]
print(m, c)
print(f(8, m, c))
plt.scatter(x, y)
plt.plot(x, y, label="Original")
plt.plot(inputx, inputy,label="Prediction")
plt.legend()
plt.show()
