import sys

n = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

l ,r = 0, max(budget)
while l <= r:
    mid = (l + r)//2
    total = 0
    for i in budget:
        if i >= mid:
            total += mid
        else:
            total += i

    if total <= m:
        l = mid + 1
    else:
        r = mid -1

print(r)


