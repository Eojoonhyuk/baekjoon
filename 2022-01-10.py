#2292
# n = int(input())
# cnt = 1
# cnt_six = 6
# count = 1
# while n > cnt:
#     count += 1
#     cnt += cnt_six
#     cnt_six += 6
# print(count)

#1085
# x, y, w, h = map(int, input().split())
# n = 0
# k = 0
# if x >= w - x:
#     n = w - x
# else:
#     n = x

# if y >= h - y:
#     k = h - y
# else:
#     k = y

# if(n > k):
#     print(k)
# else:
#     print(n)

#1920
# def binary(target):
#     left = 0
#     right = n - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if a[mid] == target:
#             return True
        
#         if target < a[mid]:
#             right = mid - 1
#         elif target > a[mid]:
#             left = mid + 1

# n = int(input())
# a = list(map(int, input().split()))
# a.sort()

# k = int(input())
# b = list(map(int, input().split()))

# for i in range(k):
#     if binary(b[i]):
#         print(1)
#     else:
#         print(0)


