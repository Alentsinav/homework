N, b, c = map(int, input().split())
l = list(map(int, str(N)[::1]))
k = 0
p = []
for i in range(0, len(l)):
    k = k + l[i]*b**(len(l)-1-i)
s = list(map(int, str(k)[::1]))
print(k, s)
while k!=0:
    p.append(k % c)
    k = k // c
print(p)
print(''.join(map(str, p[::-1])))