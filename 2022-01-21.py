#2798
# n, m = map(int, input().split())
# cards = list(map(int, input().split()))
# answer = 0
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             sum = cards[i] + cards[j] + cards[k]
#             if sum <= m:
#                 answer = max(answer, sum) 

# print(answer)

#1018
n, m = map(int, input().split())
list = []
count = []
for _ in range(n):
    list.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        num1 = 0
        num2 = 0
        for k in range(i, i + 8):
            for h in range(j, j + 8):
                if (k + h) % 2 == 0:
                    if list[k][h] != 'W':
                        num1 += 1
                    else:
                        num2 += 1
                else:
                    if list[k][h] != 'B':
                        num1 += 1
                    else:
                        num2 += 1
            
        count.append(num1)
        count.append(num2)            

print(min(count))