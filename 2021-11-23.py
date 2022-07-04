while True:
    num = input()
    palindrom = num[::-1]
    if num == '0':
        break
    if num == palindrom:
        print("yes")
    else:
        print("no")