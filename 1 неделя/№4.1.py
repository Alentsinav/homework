from os import write

a = open("text1", "r+")
b = list(map(float, a.readline().split()))
c = a.readlines()
d = c[0]
if d == '+':
    print(b[1]+b[0])
    a.write(str(b[1]+b[0]))
elif d == '-':
    print(b[1]-b[0])
    a.write(str(b[1] - b[0]))
elif d == '*':
    print(b[1]*b[0])
    a.write(str(b[1] * b[0]))