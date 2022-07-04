# 2750
# n = int(input())
# S = []
# for i in range(0, n):
#     a = int(input())
#     S.append(a)

# S.sort()
# for i in range(len(S)):
#     print(S[i])


#2309
S = []
for i in range(9):
    n = int(input())
    S.append(n)
total = sum(S)
for i in range(9):
    for j in range(i+1, 9):
        if total - (S[i]  + S[j]) == 100:
            num1, num2 = S[i],S[j]
            S.remove(num1)
            S.remove(num2)
            S.sort()
        for i in range(len(S)):
            print(S[i])
        break

