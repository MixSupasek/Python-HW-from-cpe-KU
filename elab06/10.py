hori = int(input("Enter horizontal shift size: "))
vert = int(input("Enter vertical shift size: "))
image = []
result = []
flag = True
if hori >= 0 and vert >= 0:
    print("Enter image:")
    x = input("")
    lenght_line = len(x)
    image.append(x)
    while True:
        z = input("")
        if z != '-1' and len(z) == lenght_line:
            image.append(z)        
        elif z == '-1':
            break
        elif z != '-1' and len(z) != lenght_line:
            flag = False
    if flag == True:
        print("After shift:")
        lenght = len(image[0])
        for i in range(vert):
            result.append('0'*lenght)
        for i in range(len(image)-vert):
            result.append(('0'*hori)+image[i][:(lenght-hori)])
        for i in result:
            print(i)

