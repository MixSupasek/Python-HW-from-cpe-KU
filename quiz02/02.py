def getInput():
    a = eval(input('Enter list a: '))
    b = eval(input('Enter list b: '))
    return a,b
def merge(a: list,b: list):
    global u
    ab_list = []
    for i in range(len(a)):
        ab_list.append(a[i])
    for j in range(len(b)):
        ab_list.append(b[j])
    x = ab_list
    u = type(x[0])
    if u == int: 
        for i in range(len(x)):
            for j in range(0, len(x) - i - 1):
                z = j + 1
                if int(x[j]) > int(x[z]):
                    x[j], x[z] = x[z], x[j]
        return x
    
    elif u == str: 
        for i in range(len(x)):
            for j in range(0, len(x) - i - 1):
                z = j + 1
                if ord(x[j][0]) > ord(x[z][0]):
                    x[j], x[z] = x[z], x[j]
        return x




a,b = getInput()
res = merge(a,b)
print(res)
