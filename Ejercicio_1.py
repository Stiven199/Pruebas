a=[1,2,3,4]
b=[5,6,7,8]
c=[]
j=0
for i in range(4):
    j=j+1
    c[j]=a[i]
    c.append(a[i])
    j=j+1
    c[j]=b[i]
    c.append(b[i])