from numpy import *
from matplotlib.pyplot import *
from time import sleep

x=loadtxt('cluster_circle.txt')
N=x.shape[0]

k=6 # number of cluster

z=zeros([k,x.shape[1]])
z1=zeros([k,x.shape[1]])
d=zeros([N,k])
mu=zeros(N)
print(N)

z=x[:k,:].copy() ##step 0

claster=[[] for i in range(k)]


f = True
while f:
    for i in range(0,N):
        for j in range(0,k):
            d[i,j] = sqrt((x[i,0]-z[j,0])**2+(x[i,1]-z[j,1])**2)  ##step 1
        mu = argmin(d[i,:])
        claster[mu].append(i)
            
    for cl in claster:
        x2=x.take(cl,0)
        plot(x2[:,0], x2[:,1], '.')
    plot(z[:,0], z[:,1], '*k')
    
    for num,cl in enumerate(claster):  ##step 2
        x2=x.take(cl,0)
        z1[num,:]=mean(x2, 0)
    
    plot(z1[:,0], z1[:,1], '+k')
    grid()
    show()

    if (z1==z).all():
        f = False
    else:
        z=z1.copy()
        claster=[[] for i in range(k)]
