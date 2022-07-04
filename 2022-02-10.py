n = int(input())
cards = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

hash = {}
for i in cards:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

ans = []
for i in targets:
    if i in hash:
        ans.append(hash[i])
    else:
        ans.append(0)

for i in ans:
    print(i, end = ' ')