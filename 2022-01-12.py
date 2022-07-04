#2805
# import sys
# input =  sys.stdin.readline
# n, m = map(int, input().split())
# trees = list(map(int, input().split()))
# left, right, ans = 1, max(trees), 0
# while left <= right:
#     mid = (left + right) // 2
#     tree = 0
#     for i in range(n):
#         if mid < trees[i]:
#             tree += (trees[i] - mid)
#     if tree >= m:
#         ans = mid
#         left = mid + 1
#     else:
#         right = mid - 1

# print(ans)

#1654
k, n = map(int, input().split())
lans = []
for i in range(k):
    lans.append(int(input()))
start, end = 1, max(lans)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in lans:
        total = total + (i // mid)
    if total >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)