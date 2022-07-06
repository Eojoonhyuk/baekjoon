import sys

t = int(sys.stdin.readline())
for _ in range(t):
    count = 1 #index 0번째는 서류가 1등이므로 합격
    applicant = []
    n = int(sys.stdin.readline())
    for i in range(n):
        papers, interview = map(int, sys.stdin.readline().split())
        applicant.append([papers, interview])
    
    applicant.sort()
    cut_line = applicant[0][1] #합격기준 설정

    for i in range(1,n):
        if cut_line > applicant[i][1]:
            cut_line = applicant[i][1]
            count += 1
            print(count)
    
    print(count)