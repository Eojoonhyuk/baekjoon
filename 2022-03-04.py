n, k = map(int, input().split())
list = []

for i in range(n):
    list.append(i + 1)

ans = []
i = 0
while len(list) > 0:
    i += k - 1
    if i > len(list) - 1:
        i = i % len(list)
    ans.append(list[i])
    list.pop(i)

    
print("<"+", ".join(map(str,ans))+">")

