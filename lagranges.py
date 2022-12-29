import numpy as np
import matplotlib.pyplot as plt

def lagrange(points, x):
    sum =0
    n=len(points)
    for i in range(n):
        xi, yi = points[i]
        def L(i):
            Lvalue =1
            for j in range(n):
                if i==j:
                    continue
                xj,yj = points[j]
                Lvalue *=float(x-xj)/float(xi-xj)
            return Lvalue
        sum +=yi*L(i)
    return sum
mydata= np.array([[2,7.2],[4.25,7.1],[5.25,6.0],[7.81,5.0],[9.20,3.5],[10.60,5.0]])
z=[]
for i in range(13):
    z.append([i,np.round(lagrange(mydata,i),12)])
z=np.array(z)
print(z)


plt.plot(mydata[:,0],mydata[:,1],'r')
plt.show()

# if __name__ == '__main__':
#     main()