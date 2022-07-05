import re

n = int(input())
guitar_list = []

for i in range(n):
    serial_num = input()
    guitar_list.append(serial_num)
    
for i in range(n-1):
    for j in range(i+1, n):
        if len(guitar_list[i]) > len(guitar_list[j]):
            guitar_list[i], guitar_list[j] = guitar_list[j], guitar_list[i]
        elif len(guitar_list[i]) == len(guitar_list[j]):
            # for a,b in zip(guitar_list[i], guitar_list[j]):
            a_sum = 0
            b_sum = 0
            # if a.isdigit():
            #     a_sum += int(a)
            # if b.isdigit():
            #     b_sum += int(b)
            a = re.sub(r'[^0-9]', '', guitar_list[i])
            b = re.sub(r'[^0-9]', '', guitar_list[j])
            for k in a:
                a_sum += int(k)
            for k in b:
                b_sum += int(k)
            if a_sum > b_sum:
                guitar_list[i], guitar_list[j] = guitar_list[j], guitar_list[i]
            elif a_sum == b_sum:
                for a,b in zip(guitar_list[i], guitar_list[j]):
                    if a > b:
                        guitar_list[i], guitar_list[j] = guitar_list[j], guitar_list[i]
                        break
                    elif a < b:
                        break

for i in guitar_list:
    print(i)

