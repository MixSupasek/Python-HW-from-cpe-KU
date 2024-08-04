row = int(input("Enter Rook's row position: "))
column = int(input("Enter Rook's column position: "))
if row >= 0 and row <= 7 and column >= 0 and column <= 7:
    print("-----------------")
    for i in range(8):
        print('|',end='')
        for j in range(8):
            if i != row:
                if j != column:
                    print(' |',end='')
                if j == column:
                    print('x|',end='')
            if i == row:
                if j!= column:
                    print('x|',end='')
                elif j == column:
                    print('R|',end='')
        print('')
        print("-----------------")
            
    

