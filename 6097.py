w, h = map(int, input().split())
n = int(input())

arr = [[0] * h for _ in range(w)]


for i in range(n) :
    l, d, x, y = map(int, input().split())
    x -= 1
    y -= 1
    
    if d == 0 :
        for j in range(l):
            arr[x][y+j] = 1
    else :
        for j in range(l):
            arr[x+j][y] = 1
            
for i in range(w) :
    for j in range(h) :
        print(arr[i][j], end = ' ')
    print()