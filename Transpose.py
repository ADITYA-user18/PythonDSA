arr = [[5,9,1],[2,3,7],[1,4,8]]

rows = len(arr)
cols = len(arr[0])

rev = [[0]*rows for _ in range(cols)]

for i in range(0,rows):
    for j in range(0,cols):
        rev[i][j] = arr[j][i]

print(rev)





