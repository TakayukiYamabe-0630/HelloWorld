import numpy as np

with open('hello.txt') as f:
    print(f.read())

L = np.loadtxt('hello.txt')
print(L)
L = np.array(L)
np.savetxt('hello.txt', L)