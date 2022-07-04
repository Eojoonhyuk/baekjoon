#2751번
# n = int(input())
# S = []
# for i in range(n):
#     a = int(input())
#     S.append(a)
    
# S.sort()

# for i in range(n):
#     print(S[i])

#2839번
n = int(input())
count = 0
while n >= 0:
    if n % 5 == 0:
        count = count + (n // 5)
        print(count)
        break
    n -= 3
    count += 1
else:
    print(-1)