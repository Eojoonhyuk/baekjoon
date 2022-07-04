# n = int(input())
# fibonacci = [0, 1]
# for i in range(2, n + 1):
#     num = fibonacci[i-1] + fibonacci[i-2]
#     fibonacci.append(num)

# print(fibonacci[n])

#11047
# n, k = map(int, input().split())
# coin = []
# count = 0
# for i in range(n):
#     coin.append(int(input()))
    
# for i in range(n-1, -1, -1):
#     count += k // coin[i]
#     k %= coin[i]
#     if k == 0:
#         break

# print(count)

