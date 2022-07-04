#2908번
# a, b = input().split()
# a = int(a[::-1])
# b = int(b[::-1])

# if(a > b):
#     print(a)
# else:
#     print(b)

#2475번
S = list(map(int, input().split()))
list1 = []
for i in range(len(S)):
    list1.append(S[i] * S[i])

print(sum(list1) % 10)