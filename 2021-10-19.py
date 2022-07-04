#순차검색 알고리즘
# def Seq_Search(a, x):
#     n = len(a)
#     for i in range(0, n):
#         if x == a[i]:
#             return i
#     return 0

# v = [2,1,5,3,5]
# print(Seq_Search(v, 5))

#이진검색 알고리즘(재귀)
# def Bin_Search(a, x):
#     a.sort()
#     n = len(a)
#     low = 0
#     high = n - 1
#     while(low <= high):
#         mid = (low + high) // 2
#         if(x == a[mid]):
#             return mid
#         elif(x < a[mid]):
#             high = mid - 1
#         elif(x > a[mid]):
#             low = mid + 1
#     return -1

# S = [1,2,3,4,5,6,7]
# print(Bin_Search(S, 7))

#피보나찌 수(재귀)
# def fibonacci(n):
#     if(n <= 1):
#         return 1
#     else:
#         return (fibonacci(n-1) + fibonacci(n-2))

#피노나찌 수(반복)
# def fibonacci(n):
#     S = [0 for i in range(n+1)]
#     if( n > 0):
#         S[1] = 1
#         for i in range(2, n+1):
#             S[i] = S[i-1] + S[i-2]
#         return S[i]
#     return -1
# n = int(input())
# print(fibonacci(n))

#배열 덧셈 알고리즘
# def sumdef(n=0, S =[]):
#     sum = 0
#     for i in range(0, n):
#         sum = sum +  S[i]
#     print(sum)
#     return sum

# n = 5
# S = [1,2,3,4,5]
# sumdef(n, S)

#교환정렬 알고리즘
# def exchange_sort(S = []):
#     n = len(S)
#     for i in range(0, n-1):
#         for j in range(i+1, n):
#             if (S[j] < S[i]):
#                 S[i],S[j] = S[j],S[i]
#     return S

# S = [0,23,45,67,26,12,6]
# print("원 리스트 : ",S)
# exchange_sort(S)
# print("정렬된 리스트 ", S)

#----------------------------분할정복----------------------------#
#이진검색: 재귀 알고리즘
