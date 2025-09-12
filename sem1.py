#a=int(input())
#b=int(input())
#c=(a**2+b**2)**0.5
#print(a,b,c,sep=',\n')
#x='hello'
#print(x[0:4:2])
#a=[1,2,3]
#b=[[a]*10]*2
#a[0]=0
#print(b)
"""a=['1','2','3']
a=list(map(int,input().split()))
print(a)
a=int(input())
b=int(input())
print(a+b,a-b,a*b)
a=str(input())
b=a[-1]
print(b)
f=open('text.txt','r')
#print(f.read())
lines=f.readlines()
print(lines)
f.close()
with open('1 2 3 4 5.txt','r') as f:
    lines = f.readlines()
    numbers=list(map(int,lines[0].split()))
    op=lines[1].strip()
    if op == '+':
        res = 0
        for i in numbers:
            res =+ 1
    elif op == '*':
        res =1
        for i in numbers:
            res *= i
    else:
        res = numbers[0]
        for i in range(1,len(numbers)):
            res -= numbers[i]
    print(res)"""
N,b,c=int(input()),int(input()),int(input())
a=[]
if (b==c):
    print(N)
else:
    while (N!=0):
        N=N//c
        k=N%c
        a.append(k)
a[::-1]
print(a)