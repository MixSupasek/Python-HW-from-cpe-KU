def checkmine(i,j):
    mine = 0
    try:
        if j - 1 >= 0 and matrix[i][j-1] == 'X':
            mine += 1

        if j + 1 < len(matrix[0]) and matrix[i][j+1] == 'X':
            mine += 1

        if i - 1 >= 0 and j - 1 >= 0 and matrix[i-1][j-1] == 'X':
            mine += 1

        if i - 1 >= 0 and j + 1 < len(matrix[0]) and matrix[i-1][j+1] == 'X':
            mine += 1

        if i - 1 >= 0 and matrix[i-1][j] == 'X':
            mine += 1

        if i + 1 < len(matrix) and j - 1 >= 0 and matrix[i+1][j-1] == 'X':
            mine += 1

        if i + 1 < len(matrix) and j + 1 < len(matrix[0]) and matrix[i+1][j+1] == 'X':
            mine += 1

        if i + 1 < len(matrix) and matrix[i+1][j] == 'X':
            mine += 1

    except Exception as e:
        pass
    return mine

size = list(map(int,input("Grid Size: ").split()))
size.reverse()
num_mine = int(input("Number of mine(s): "))
matrix = [] #####size[0]*size[1]
bom_pos = []
for i in range(num_mine):
    x = list(map(int,input(f"Mine#{i+1}: ").split()))
    x.reverse()
    bom_pos.append(x)
for i in range(size[0]):
    matrix.append([])
for i in range(size[0]):
    for j in range(size[1]):
        if [i,j] in bom_pos:
            matrix[i].append('X')
        else:
            matrix[i].append('y')
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'y':
            x = checkmine(i,j)
            matrix[i].insert(j,x)
            matrix[i].pop(j+1)
            
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end =' ')
    print('')
