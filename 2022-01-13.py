#2775
# t = int(input())
# for _ in range(t):
#     k = int(input())
#     n = int(input())
#     f0 = [x for x in range(1, n + 1)]
#     for i in range(k):
#         for j in range(1, n):
#             f0[j] += f0[j-1] 

#     print(f0[-1])

#4153
# while True:
#     a, b, c = list(map(int, input().split()))
#     if a == 0 and b == 0 and c == 0:
#         break
#     nums = [a, b, c]
#     nums.sort() 
#     if nums[0] ** 2 + nums[1] ** 2 == nums[2] ** 2:
#         print("right")
#     else:
#         print("wrong")

#1874
n = int(input())
stack = []
result = []
count = 1
temp = 0
for i in range(n):
    nums = int(input())
    while count <= nums:
        stack.append(count)
        result.append("+")
        count += 1
    if stack[-1] == nums:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        temp = 1
        break

if temp == 0:
    for i in result:
        print(i)
        
