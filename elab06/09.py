row = int(input("Enter the number of rows or columns : "))

for i in range(1,row+1):
    for j in range(i,i+row):
        print('%2d'%j,end=' ')
    print('')
