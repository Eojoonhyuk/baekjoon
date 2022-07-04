n = int(input())
S = []
for i in range(0, n):
    a, S = input().split()
    a = int(a)
    for i in range(len(S)):
        print(S[i] * a, end = '')
    print()
