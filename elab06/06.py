size = input("City Size: ")
size = size.split()
map = []
for i in range(len(size)):
    size[i] = int(size[i])

for i in range (size[0]):
    x = input("")
    x = x.split()
    map.append(x)
# size = [4,5]
result_dir = []
# map = [['2', '3', '5', '6', '2'], ['1', '3', '4', '7', '1'], ['6', '5', '4', '1', '3'], ['2', '3', '7', '9', '6']]
for i in range(len(map)):
    for j in range(len(map[i])):
        map[i][j] = int(map[i][j])
def find_dir(map):
    global news_list,north,south,east,west
    news_list = []
    north = size[1]
    south = size[1]
    east = size[0]
    west = size[0]
    for i in range(size[1]): ######north
        sta = map[0][i]
        for j in range(size[0]):
            try:
                if sta > map[j+1][i]:
                    pass
                elif sta < map[j+1][i]:
                    north += 1
                    sta = map[j+1][i]
            except:
                pass
    for i in range(size[1]-1,-1,-1): ######south
        sta = map[-1][i]
        for j in range(size[0]-1,-1,-1):
            try:
                if sta > map[j-1][i]:
                    pass
                elif sta < map[j-1][i]:
                    south += 1
                    sta = map[j-1][i]
            except:
                pass
    for i in range(size[0]): ######WEST
        sta = map[i][0]
        for j in range(size[1]):
            try:
                if sta > map[i][j+1]:
                    pass
                elif sta < map[i][j+1]:
                    west += 1
                    sta = map[i][j+1]
            except:
                pass
    for i in range(size[0]-1,-1,-1): ######EAST
        sta = map[i][-1]
        for j in range(size[1]-1,-1,-1):
            try:
                if sta > map[i][j-1]:
                    pass
                elif sta < map[i][j-1]:
                    east += 1
                    sta = map[i][j-1]
            except:
                pass
    news_list = [('N',north),('S',south),('E',east),('W',west)]
    return news_list

find_dir(map)
news_list.sort(key=lambda x: x[1], reverse=True)
max_num = news_list[0][1]
for i in news_list:
    if i[1] == max_num:
        print(i[0],end=' ')
