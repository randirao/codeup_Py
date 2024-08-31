# arr = [[0 for col in range(10)] for row in range(10)]

arr = [list(map(int, input().split())) for _ in range(10)]

#입력받기   
# for i in range(10) :
#     for j in range(10) :
#         arr[i][j] = int(input())

x, y = 1, 1

while True :
    arr[x][y] = 9             #arr[x][y]는 9로 초기화
    if arr[x][y] == 2 :       #먹이가 있으면
        break                 #멈춰!
    elif arr[x][y+1] == 1 :   #오른쪽이 막혔으면
        x += 1                #밑으로 ㄱㄱ
    else :                    #아니면
        y += 1                #오른쪽으로 ㄱㄱ
    

#출력하기
for i in range(10):
    for j in range(10):
        print(arr[i][j], end=' ')
    print("")