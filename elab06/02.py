text = input("Input sentence: ")
row = int(input("Input row: "))
def zigzag(text,row):
    list = []
    result = []
    current = 0
    n_row = 0
    flag = True
    if row == 1:
        for i in text:
            list.append(i)
            result = [list]
    if row > 1:
        for i in range(row):
            result.append([])
        while current != len(text):
            try:
                result[n_row].append(text[current])
                current += 1
                if n_row == (row-1):
                    flag = False
                    
                elif n_row == 0:
                    flag = True
                    
                if flag == True:
                    n_row += 1
                elif flag == False:
                    n_row -= 1
            except IndexError:
                print("curent: ",current)
                break
            
    return result
            
for i in zigzag(text,row):
    for j in i:
        print(j,end='')
