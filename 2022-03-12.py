import sys

start = [2,8,3,1,6,4,7,0,5] #시작상태
goal = [8,3,0,2,6,4,1,7,5] #목표상태

#    X       index
# |2 8 3|   |0 1 2|
# |1 6 4|   |3 4 5|
# |7 0 5|   |6 7 8|

#공백을 올려주는 함수
#down, left, right의 경우도 같다.
def up(X):
    index=0
    for i in range(len(X)): #X의 0의 위치 찾기 
        if X[i]==0:
            index = i
    
    if index ==0 or index ==1 or index == 2: #index = 0,1,2 는 위에 공간이 없기 때문에 다시 X리턴 
        return X
    else:#위로 up하였기 떄문에 값이 교환
        X[index]=X[index-3]
        X[index-3]=0
        return X

#공백을 바로 아래로 내려주는 함수
def down(X):

    index=0
    for i in range(len(X)):
        if X[i]==0:
            index = i
    
    if index ==6 or index ==7 or index == 8:
        return X
    else:
        X[index]=X[index+3]
        X[index+3]=0
        return X

#현재 공백 바로 오른쪽으로 옮겨주는 함수
def right(X):
    
    index=0
    for i in range(len(X)):
        if X[i]==0:
            index = i
    
    if index ==2 or index ==5 or index == 8:
        return X
    else:
        X[index]=X[index+1]
        X[index+1]=0
        return X
    
#현재 공백 바로 왼쪽으로 옮겨주는 함수
def left(X):
    index=0
    for i in range(len(X)):
        if X[i]==0:
            index = i
    
    if index ==0 or index ==3 or index == 6:
        return X
    else:
        X[index]=X[index-1]
        X[index-1]=0
        return X


def depth_first_search(): #깊이우선함수

    print(" 깊이 우선 탐색 ")
    open = [start] #시작노드
    closed=[]
  
    print("시작노드:",open)
    count = 1 #깊이레벨
    while open != []: #open 리스트가 빈 상태거나 탐색이 성공할 때 까지 반복 
        X = open[0] #현재상태
        #2차원 배열리스트로 출력
        print("현재노드:",count,": ")
        print("현재 open LIST ",open)
        print("-------------")
        print("|",X[0],"|",X[1],"|",X[2],"|")
        print("-------------")
        print("|",X[3],"|",X[4],"|",X[5],"|")
        print("-------------")
        print("|",X[6],"|",X[7],"|",X[8],"|")
        print("-------------\n")

        count=count+1 #깊이레벨 + 1
        
        if X==goal: #현재상태가 목표상태와 같을 경우, while문 종료
            print("Success")
            return True
        else : #아닐경우 현재상태 X의 자식노드를 생성한다.
                child=[]
                tmp=(tuple(X)) #현재상태와 자식노드가 같아지는것을 방지하기위해 튜플사용

                child.append(down(list(tmp)))
                   
                child.append(right(list(tmp))) #여백이 오른쪽으로 이동한거
                
                child.append(up(list(tmp))) #여백이 가운데로 이동한거
                
                child.append(left(list(tmp))) #여백이 왼쪽으로 이동한거
                
            

        closed.append(X) #closed(이미끝난 상태) 리스트에 현재상태 X 추가
        open.remove(X) #open 리스트에 현재상태 X 제거 => 이미탐색이 끝났기 때문
        
        #중복된 리스트 제거
        for i in range(len(child)):
            if child[i] not in open and child[i] not in closed:
                open.insert(0,child[i])

         
    print("Fail")
    return False #while문 종료


depth_first_search() #깊이우선 함수호출
