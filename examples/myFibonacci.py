# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

a=[1 ,2 ,3]
b=1,2,3
print a
print b

# <codecell>

a=1
b=1
b.append(b+a)

# <codecell>


# <codecell>


# <codecell>


# <codecell>

a=b=1
result=[a,b]
n=input("Print Fibonacci series upto digit ")
if n<=len(result):
    for i in range(0,n):
        print result[i],
else:
    while(len(result)<n):
        c=a+b
        a=b
        b=c
        result.append(c)
    print result

# <codecell>


