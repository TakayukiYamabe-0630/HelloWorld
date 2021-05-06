import matplotlib.pyplot as plt

def main():
    my_code()
    
def my_code():
    dt = 0.01
    g = 9.80665
    e = 0.7
    V = [0]
    P = [10]
    T = [i*dt for i in range(1000)]
    for i in range(1,1000):
        V.append(V[i-1] - g*dt)
        P.append(P[i-1] + V[i-1]*dt)
        if P[i] < 0:
            P[i] = -e*P[i]
            V[i] = -e*V[i]
    plt.plot(T, P)
    plt.show()
    
def sample():
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
            
if __name__ == '__main__':
    main()