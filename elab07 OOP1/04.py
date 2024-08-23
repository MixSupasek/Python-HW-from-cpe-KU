class Coin:
    def __init__(self,value = 1):
        self.value = value
    def __str__(self):
        return f"{self.value} Baht Coin"
class BankNote:
    def __init__(self,value = 20):
        self.value = value
    def __str__(self):
        return f"{self.value} Baht Banknote"
amount = int(input("Input amount : "))
if amount >= 1000:
    a = int(amount/1000)
    ths = BankNote(1000)
    print(f"You get {a} of {ths}")
    amount -= 1000*a
if amount >= 500:
    a = int(amount/500)
    fhun = BankNote(500)
    print(f"You get {a} of {fhun}")
    amount -= 500*a
if amount >= 100:
    a = int(amount/100)
    hun = BankNote(100)
    print(f"You get {a} of {hun}")
    amount -= 100*a
if amount >= 50:
    a = int(amount/50)
    fif = BankNote(50)
    print(f"You get {a} of {fif}")
    amount -= 50*a
if amount >= 20:
    a = int(amount/20)
    twe = BankNote(20)
    print(f"You get {a} of {twe}")
    amount -= 20*a
if amount >= 10:
    a = int(amount/10)
    ten = Coin(10)
    print(f"You get {a} of {ten}")
    amount -= 10*a
if amount >= 5:
    a = int(amount/5)
    fiv = Coin(5)
    print(f"You get {a} of {fiv}")
    amount -= 5*a
if amount >= 2:
    a = int(amount/2)
    two = Coin(2)
    print(f"You get {a} of {two}")
    amount -= 2*a
if amount >= 1:
    a = int(amount/1)
    one = Coin(1)
    print(f"You get {a} of {one}")
    amount -= a
    
            
            
        
