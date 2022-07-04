S = input()
if(S == "1 2 3 4 5 6 7 8"):
    print("ascending")
elif(S == "8 7 6 5 4 3 2 1"):
    print("descending")
else:
    print("mixed")

#11720번
n = int(input())
sum = 0
S = list(map(int, input()))
for i in range(n):
    sum = sum + S[i]

print(sum)

#1157번
word = input().upper()
word_list = list(set(word))
count_list = []
for i in range(len(word_list)):
    cnt = word.count(word_list[i])
    count_list.append(cnt)
    
if count_list.count(max(count_list)) >= 2:
    print("?")
else:
    print(word_list[(count_list.index(max(count_list)))])

#1546번
n = int(input())
num_list = list(map(int, input().split()))
avg_list = []
for i in range(n):
    avg_list.append(num_list[i] / max(num_list) * 100) 

avg = sum(avg_list) / n
print(avg)



