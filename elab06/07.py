flip = input("Direction to flip square (V/H): ")
size = int(input("Input size of square: "))
matrix = []
for i in range(size):
    x = input("")
    x = x.split()
    matrix.append(x)

def flip_tool(flip,matrix):
    result = []
    if flip == 'V':
        for i in range(-1,(-1*size)-1,-1):
            result.append(matrix[i])
    
    elif flip == 'H':
        for i in range(size):
            result.append(matrix[i][::-1])
            
    return result

print("After flip:")
for i in flip_tool(flip,matrix):
    print(*i)
    
