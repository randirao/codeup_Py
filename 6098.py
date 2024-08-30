arr = []

for i in range(10):
    arr.append([0] * 10)

#입력받기   
for i in range(10) :
    for j in range(10) :
        arr[i] = map(int, input().split())

# while True :
arr[1][1] = 9

#출력하기
for i in range(10):
    for j in range(10):
        print(arr[i][j], end=' ')
    print()