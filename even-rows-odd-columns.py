rows, columns = [int(x) for x in input().split()]

matrix = []

for i in range(rows):
    temp = list(map(int, input().split()))[:columns]
    matrix.append(temp)
    
for i in range(rows):
    if (i+1)%2 == 0:
        matrix[i].reverse()

start_ = rows - 1
end_ = 0 
for i in range(rows):
    for j in range(columns):
        if (j+1) % 2 != 0:
            print(matrix[start_][end_],end=" ")
            end_ += 2
        else:
            print(matrix[i][j],end=" ")
    start_ -= 1
    end_ = 0
    print()
    
