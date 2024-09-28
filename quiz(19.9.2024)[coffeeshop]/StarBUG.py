def readMenu(fn='CoffeeMenu01.txt'): # นำฟังชันนี้ไปใช้อ่านเมนูกาแฟ โดยไม่ต้องส่งซ้ำ
    with open(fn) as fd:
        return fd.read()

# นิยามคลาสทั้งสองให้สมบูรณ์ตามข้อกำหนดด้านบน นิสิตสามารถเพิ่มเติมเมธอด setter / getter และอื่นๆ จากที่กำหนดด้านบนได้ตามความเหมาะสม
class CupOfCoffee:
    def __init__(self, coffee_type='', drinking_type='', price=0):
        self.coffee_type = coffee_type
        self.drinking_type = drinking_type
        self.price = price
        self.add_on = []
        self.addonprice = []
    def set_add_on(self, one_add_on, one_add_on_price):
        self.add_on.append(one_add_on)
        self.addonprice.append(one_add_on_price)
        self.price += one_add_on_price
    def __repr__(self):
        if len(self.add_on) == 0:
            return f" This cup is {self.drinking_type.lower()} {self.coffee_type} with no add on, {self.price} baht."
        elif len(self.add_on) == 1:
            return f" This cup is {self.drinking_type.lower()} {self.coffee_type} with {self.add_on[0]}, {self.price} baht."
        elif len(self.add_on) == 2:
            return f" This cup is {self.drinking_type.lower()} {self.coffee_type} with {self.add_on[0]} and {self.add_on[1]}, {self.price} baht."
        elif len(self.add_on) == 3:
            return f" This cup is {self.drinking_type.lower()} {self.coffee_type} with {self.add_on[0]}, {self.add_on[1]} and {self.add_on[2]}, {self.price} baht."
            
class CustomerBill:
    def __init__(self,name=''):
        self.name = name
        self.price = 0
        self.res = ''
        width = 32
        txt = f"Kun {self.name}'s Receipt"
        xy = int((32-len(txt))/2)
        self.res += "++++++++++++++++++++++++++++++++\n"
#         self.res += f"      CPE38 **StarBUG Cafe\n"
#         self.res += f"{txt.center(width)}"
        self.res += f"{'CPE38 **StarBUG Cafe'.center(width)}\n"
        self.res += f"{txt:>{xy+len(txt)}}"
        self.res += f"\n{'++++++++++++++++++++++++++++++++':<0}\n"
        self.res += "Description                Price\n"
    def add_ordered_coffee(self, aCupOfCoffeeObject):
        b = aCupOfCoffeeObject
        self.price += b.price
        spaceres = 30
        spaceres -= len(b.drinking_type)
        spaceres -= len(b.coffee_type)
        self.res += f"{b.drinking_type} {b.coffee_type} {b.price:>{spaceres}}\n"
        if len(b.add_on) > 0:
            for j in range(len(b.add_on)):
                self.res += f" + {b.add_on[j]}\n"
            self.res += "\n"
        else:
            self.res += "\n"
    def receipt(self):
        self.res += f"Total {self.price:>26,}\n"
        self.res += "++++++++++++++++++++++++++++++++\n"
        self.res += " Thank you, please come back :)\n"
        self.res += "++++++++++++++++++++++++++++++++\n"
        return self.res
        
def readMenuNew(fn='CoffeeMenu01.txt'):
    m = []
    with open(fn) as fd:
        for line in fd:
            m.append(line.strip().split(','))
        return m

def runStarBUGcafe_main():
    global total
    global coffee_dict
    global ft
    coffee_menu_CSV = readMenuNew(coffee_menu_filename)
    add_on_menu_CSV = readMenuNew(addon_menu_filename)
    res = ''
    menu_C = 1
    addon_C = 1
    cup_C = 1
    Addon_list = []
    pop = False
    for i in coffee_menu_CSV:
        for j in range(len(i)):
            try:
                i[j] = int(i[j])
            except:
                pass
    for i in add_on_menu_CSV:
        for j in range(len(i)):
            try:
                i[j] = int(i[j])
            except:
                pass
    if [''] in coffee_menu_CSV:
        coffee_menu_CSV.remove([''])
    if [''] in add_on_menu_CSV:
        add_on_menu_CSV.remove([''])
    if ft:
        for i in coffee_menu_CSV:
            coffee_dict[f"{i[0]}"] = 0
    print("Welcome to CPE38 **StarBUG Cafe!")
    print("+++++++++++++ MENU +++++++++++++")
    print("Coffee         Hot  Cold  Frappe")
    for i in coffee_menu_CSV:
        space = len(i[0])
        space = 15-space
        print(f"{menu_C}.{i[0]} {i[1]:>{space}} {i[2]:>5} {i[3]:>5}")
        menu_C += 1
    print("++++++++++++ ADD-ON ++++++++++++")
    for i in add_on_menu_CSV:
        space = len(i[0])
        space = 21-space
        print(f"{addon_C}.{i[0]} {i[1]:>{space}}")
        addon_C += 1
    print("++++++++++++++++++++++++++++++++")
    print()
    name = input("Enter customer's name: ")
    if name != "Good Day":
        while True:
            try:
                numcup = int(input("How many cups of coffee to order? "))
            except ValueError:
                print(" ERROR: Invalid input!")
                continue
            if numcup <= 0:
                print(" ERROR: Invalid input!")
            else:
                break
        b = CustomerBill(name)
        for i in range(numcup):
            flag = False
            count = 0
            zero_C = 0
            
            Addon_list.append([])
            
            while True:
                try:
                    TypeOfCoffee = int(input(f"Cup #{cup_C}, please select type of coffee: "))
                except ValueError:
                    print(" ERROR: Invalid input!")
                    continue
                if TypeOfCoffee > len(coffee_menu_CSV) or TypeOfCoffee < 1:
                    print(" ERROR: Invalid input!")
                else:
                    break
            for j in range(4):
                if coffee_menu_CSV[TypeOfCoffee-1][j] == 0:
                    zero_C += 1
            while True:
                if zero_C == 0:
                    DrinkingType = input(f"Cup #{cup_C}, please select drinking type (H,C,F): ")
                    if DrinkingType == 'h' or DrinkingType == 'H':
                        DrinkingType = 1
                        break
                    elif DrinkingType == 'c' or DrinkingType == 'C':
                        DrinkingType = 2
                        break
                    elif DrinkingType == 'f' or DrinkingType == 'F':
                        DrinkingType = 3
                        break
                    else:
                        print(" ERROR: Invalid input!")
                elif zero_C == 1:
                    DrinkingType = input(f"Cup #{cup_C}, please select drinking type (H,C): ")
                    if DrinkingType == 'h' or DrinkingType == 'H':
                        DrinkingType = 1
                        break
                    elif DrinkingType == 'c' or DrinkingType == 'C':
                        DrinkingType = 2
                        break
                    else:
                        print(" ERROR: Invalid input!")
                elif zero_C == 2:
                    DrinkingType = 1
                    break
            if DrinkingType == 1:
                DrinkingTypeStr = 'Hot'
            elif DrinkingType == 2:
                DrinkingTypeStr = 'Cold'
            elif DrinkingType == 3:
                DrinkingTypeStr = 'Frappe'
            while count != len(add_on_menu_CSV):
                TypeOfAddon = input(f"Cup #{cup_C}, please select add on (enter for exit): ")
                if TypeOfAddon == '':
                    break
                else:
                    try:
                        if int(TypeOfAddon) > len(add_on_menu_CSV) or int(TypeOfAddon) < 1 or int(TypeOfAddon) in Addon_list[i]:
                            print(" ERROR: Invalid input!")
                        else:
                            TypeOfAddon = int(TypeOfAddon)
                            if TypeOfAddon not in Addon_list[i]:
                                count += 1
                                Addon_list[i].append(TypeOfAddon)
                                flag = True
                            else:
                                print(" ERROR: Invalid input!")
                                continue
                    except ValueError:
                        print(" ERROR: Invalid input!")
                        continue
            a = CupOfCoffee(coffee_type = coffee_menu_CSV[TypeOfCoffee-1][0],drinking_type = DrinkingTypeStr,price = coffee_menu_CSV[TypeOfCoffee-1][DrinkingType])
            coffee_dict[a.coffee_type] += 1
            if len(Addon_list[cup_C-1]) > 0 and flag:
                for j in Addon_list[cup_C-1]:
                    a.set_add_on(one_add_on = add_on_menu_CSV[j-1][0], one_add_on_price = add_on_menu_CSV[j-1][1])
                    
            total += a.price 
            b.add_ordered_coffee(a)
            spaceres = 30
            spaceres -= len(DrinkingTypeStr)
            spaceres -= len(a.coffee_type)
            print(a)
            res += f"{DrinkingTypeStr} {a.coffee_type} {a.price:>{spaceres}}\n"
            if len(Addon_list[cup_C-1]) > 0 and flag:
                for j in range(len(Addon_list[cup_C-1])):
                    res += f" + {a.add_on[j]}\n"
            cup_C += 1

        print(b.receipt())
        ft = False
        runStarBUGcafe_main()
    else:
        print("++++++++++++++++++++++++++++++++")
        print("      CPE38 **StarBUG Cafe")
        print("  Report for Coffee sold today")
        print("++++++++++++++++++++++++++++++++")
        for coffee in coffee_dict:
            space = 24
            space -= len(coffee)
    
            if coffee_dict[coffee] != 0:
                if coffee_dict[coffee] > 1:
                    print(f" {coffee} {coffee_dict[coffee]:>{space}} cups")
                elif coffee_dict[coffee] == 1:
                    print(f" {coffee} {coffee_dict[coffee]:>{space}} cup")
        print()
        print(f"Total sold amount {total:>9,} baht")
        print("++++++++++++++++++++++++++++++++")
        print("       What's a good day!")
        print("++++++++++++++++++++++++++++++++")
        
    
coffee_dict = dict()
total = 0
ft = True
coffee_menu_filename = input('Enter Coffee Menu available today (filename): ')
coffee_menu_CSV = readMenu(coffee_menu_filename)
addon_menu_filename = input('Enter AddOn Menu available today (filename): ')
add_on_menu_CSV = readMenu(addon_menu_filename)
runStarBUGcafe_main()

            
