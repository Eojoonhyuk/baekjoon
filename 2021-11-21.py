#1427
# s = input()
# num = list(map(int, str(s)))
# num.sort()
# num.reverse()
# for i in range(len(num)):
#     print(num[i], end = "")

#1181
n = int(input())
S = []
for i in range(n):
    S.append(input())

S = list(set(S))
S.sort(key = lambda x : (len(x), x))

for i in range(len(S)):
    print(S[i])

