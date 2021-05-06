import matplotlib.pyplot as plt
ts = 0.01
g = 9.8 #gravity
e = 0.6
v = [] #empty list
p = []
t = []
v.append(0)
p.append(10)
t.append(0)
for i in range(1,1000):
    t.append(i/100) # time
    v.append(v[i-1] -g*ts) # velocity
    p.append(p[i-1] +v[i-1]*ts)
    if p[i] < 0:
        p[i] = - e*p[i]
        v[i] = -e*v[i]
        plt.plot(t, p)
        plt.show()