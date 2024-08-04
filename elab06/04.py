import string
alpha_list = []
alpha_list = list(string.ascii_uppercase)
txt_list = []
txt = input("Text: ")
txt_list = txt.split()
# txt_list = ['HEAD' ,'HEAP' ,'LEAP' ,'TEAR', 'REAR' ,'BAER' ,'BAET' ,'BEEP', 'JEEP' ,'JOIP', 'JEIP' ,'AEIO']
# print(txt_list)
streak = 1
streak_list = []
flag = True
for x in txt_list:
    for z in x:
        if z in alpha_list:
            pass
        else:
            flag = False
if flag == True:
    for i in range(len(txt_list)):
        cur_mis = 0
        for j in range(len(txt_list[i])):
            try:
                if txt_list[i][j] != txt_list[i+1][j]:
                    cur_mis += 1
                else:
                    pass
       
            except IndexError:
                streak_list.append(streak)
                break
            
        if cur_mis > 2:
            streak_list.append(streak)
            streak = 1
        elif cur_mis <= 2:
            streak += 1
    streak_list.sort(reverse=True)
    print(f"{len(streak_list)} Chain(s). Maximum length is {streak_list[0]} word(s).")

