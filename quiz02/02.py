def Unicodesort(x:list):
    for i in range(len(x)):
        for j in range(len(x)):
            z = j+1
            if ord(x[j]) > ord[x[z]]:
                x[j] = x[z]
                x[z] = x[j]
    return x

a_list = list(map(str,input("Enter list a: ").split()))
b_list = list(map(str,input("Enter list b: ").split()))
ab_list = a_list.extend(b_list)
print(Unicodesort(ab_list))