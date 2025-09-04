import matplotlib.pylab as plt
x1 = []
y1 = []
x2 = []
y2 = []
plt.clf()
for z in range(8):
    x1.append(z)
    x2.append(-z)
    y1.append(z*5)
    y2.append(z * 5)
plt.figure('fat carrot')
plt.title('fat carrot')
plt.plot(x1, y1, label = 'line')
plt.plot(x2, y2, label = 'line 2')
plt.xlabel('slurp')
plt.ylabel('yum')
plt.legend(loc = 'upper left')

plt.show()
