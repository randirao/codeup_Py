arr = []

#입력받기
for i in range(10):
    row = list(map(int, input().split()))
    arr.append(row)

x, y = 1, 1

while True :
    if arr[x][y] == 2 :         #먹이가 있으면
        arr[x][y] = 9
        break                   #멈춰!
    arr[x][y] = 9               #arr[x][y]는 9로 초기화

    if y+1 < 10 and arr[x][y+1] != 1 :       #오른쪽이 막혔으면
        y += 1                  #밑으로 ㄱㄱ
    elif x+1 < 10 and arr[x+1][y] != 1:      #아니면
        x += 1                  #오른쪽으로 ㄱㄱ
    else :
        break
    

#출력하기
for i in range(10):
    for j in range(10):
        print(arr[i][j], end=' ')
    print("")