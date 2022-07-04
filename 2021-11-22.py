#1978
n = int(input())
num = list(map(int, input().split()))
resCnt = 0

for i in num:
    cnt = 0
    if (n == 1):
        continue
    for j in range(2, i + 1): 
        if(i % j == 0):
            cnt += 1
    if(cnt == 1):
        resCnt += 1


print(resCnt)
