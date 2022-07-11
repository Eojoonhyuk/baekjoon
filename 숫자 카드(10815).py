import sys
n = int(sys.stdin.readline())
my_list = list(map(int, input().split()))
m = int(sys.stdin.readline())
card_list = list(map(int, input().split()))

my_list.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in card_list:
    if binary_search(my_list, i, 0, n -1) is not None:
        print("1", end = ' ')
    else:
        print("0", end = ' ')





