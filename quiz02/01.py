rat = '__QQ\n()">'.split('\n')
hunter = ' O \n/|\\\n/ \\'.split('\n')
lion = ' /\_/\ \n( o.o )\n > ^ < '.split('\n')
pic = (rat, hunter, lion)
name_1 = input("Player1 name: ")
name_2 = input("Player2 name: ")
print("")
score_1 = 0
score_2 = 0
round = 1

def score(choice_1,choice_2):

    if choice_1 == 1 and choice_2 == 1:
        pass
    elif choice_1 == 1 and choice_2 == 2:
        score_1 += 1
    elif choice_1 == 1 and choice_2 == 3:
        score_2 += 1
        
    elif choice_1 == 2 and choice_2 == 1:
        score_2 += 1
    elif choice_1 == 2 and choice_2 == 2:
        pass
    elif choice_1 == 2 and choice_2 == 3:
        score_1 += 1
    
    elif choice_1 == 3 and choice_2 == 1:
        score_1 += 1
    elif choice_1 == 3 and choice_2 == 2:
        score_2 += 1
    elif choice_1 == 3 and choice_2 == 3:
        pass
    
while True:
    if score_1 != 3 and score_2 !=3 and round != 6:
        print(f"Round {round}!")
        print(f"{name_1} {score_1} / {name_2} {score_2}")
        choice_1 = int(input(f"{name_1}'s choice (1/rat, 2/hunter and 3/lion): "))
        choice_2 = int(input(f"{name_2}'s choice (1/rat, 2/hunter and 3/lion): "))
        if (choice_1 == 1 or choice_1 == 2 or choice_1 == 3) and (choice_2 == 1 or choice_2 == 2 or choice_2 == 3):
            if choice_1 == 1 and choice_2 == 1:
                pass
            elif choice_1 == 1 and choice_2 == 2:
                score_1 += 1
            elif choice_1 == 1 and choice_2 == 3:
                score_2 += 1
                
            elif choice_1 == 2 and choice_2 == 1:
                score_2 += 1
            elif choice_1 == 2 and choice_2 == 2:
                pass
            elif choice_1 == 2 and choice_2 == 3:
                score_1 += 1
            
            elif choice_1 == 3 and choice_2 == 1:
                score_1 += 1
            elif choice_1 == 3 and choice_2 == 2:
                score_2 += 1
            elif choice_1 == 3 and choice_2 == 3:
                pass
            round += 1
            pic = (rat, hunter, lion)
            if choice_1 == 1 and choice_2 == 1:
                pic = (rat, hunter, lion)
                i = rat
                print(i[0],'    ',i[0])
                print(i[1],' VS ',i[1])
            if choice_1 == 1 and choice_2 == 2:
                pic = (rat, hunter, lion)
                i = rat
                j = hunter
                print(i[0],'    ',j[0])
                print(i[1],' VS ',j[1])
                print('         ',j[2])
            if choice_1 == 1 and choice_2 == 3:
                pic = (rat, hunter, lion)
                i = rat
                j = lion
                print(i[0],'    ',j[0])
                print(i[1],' VS ',j[1])
                print('         ',j[2])
                
            if choice_1 == 2 and choice_2 == 1:
                pic = (rat, hunter, lion)
                i = hunter
                j = rat
                print(i[0],'    ',j[0])
                print(i[1],' VS ',j[1])
                print(i[2])

            if choice_1 == 2 and choice_2 == 2:
                pic = (rat, hunter, lion)
                i = hunter
                j = hunter
                print(i[0],'    ',j[0])
                print(i[1],' VS ',j[1])
                print(i[2],'    ',j[2])
            if choice_1 == 2 and choice_2 == 3:
                pic = (rat, hunter, lion)
                i = hunter
                j = lion
                print(i[0],'    ',j[0])
                print(i[1],' VS ',j[1])
                print(i[2],'    ',j[2])
            if choice_1 == 3 and choice_2 == 1:
                pic = (rat, hunter, lion)
                i = lion
                j = rat
                print(i[0],'    ',j[0])
                print(i[1],' VS ',j[1])
                print(i[2])

            if choice_1 == 3 and choice_2 == 2:
                pic = (rat, hunter, lion)
                i = lion
                j = hunter
                print(i[0],'    ',j[0])
                print(i[1],' VS ',j[1])
                print(i[2],'    ',j[2])
            if choice_1 == 3 and choice_2 == 3:
                pic = (rat, hunter, lion)
                i = lion
                j = lion
                print(i[0],'    ',j[0])
                print(i[1],' VS ',j[1])
                print(i[2],'    ',j[2])
            print('')
    elif score_1 == 3:
        print(f"{name_1} {score_1} / {name_2} {score_2}")
        print(f"{name_1} win!")
        break
    elif score_2 == 3:
        print(f"{name_1} {score_1} / {name_2} {score_2}")
        print(f"{name_2} win!")
        break
    elif round == 6 and score_1 == score_2:
        print(f"{name_1} {score_1} / {name_2} {score_2}")
        print("Draw!")
        break
    elif round == 6 and score_1 > score_2:
        print(f"{name_1} {score_1} / {name_2} {score_2}")
        print(f"{name_1} win!")
        break
    elif round == 6 and score_1 < score_2:
        print(f"{name_1} {score_1} / {name_2} {score_2}")
        print(f"{name_2} win!")
        break