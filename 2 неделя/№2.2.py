G, n= input().split()
G=int(G)
g_len=len(n)//G
res=''
for i in range(0, len(n), g_len):
    res += n[i:i+g_len][::-1]
print(res)