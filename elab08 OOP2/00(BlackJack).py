import random, time
import turtle
txt = '->'
class myCards:
    def __init__(self):
        self.carrycar = []
    def inpcard(self,a):
        self.carrycar.append(a)
def score(x,time=2):
    score = 0
    check = False
    for i in range(len(x)):
        if x[i][0] == "A":
            score += 1
            check = True
        elif x[i][0] == "2":
            score += 2
        elif x[i][0] == "3":
            score += 3
        elif x[i][0] == "4":
            score += 4
        elif x[i][0] == "5":
            score += 5
        elif x[i][0] == "6":
            score += 6
        elif x[i][0] == "7":
            score += 7
        elif x[i][0] == "8":
            score += 8
        elif x[i][0] == "9":
            score += 9
        elif x[i][0] == "T" or x[i][0] == "J" or x[i][0] == "Q" or x[i][0] == "K" and x[i][0] != "O":
            score += 10
        elif x[i][0] == "O":
            score += 0
    if check:
        a = score+10
        if a <=21:
            score = a
        elif a > 21:
            pass
        
            
    
    return score
        
    
        
class Card():
    ''' Card(): create a card object. To create a deck, try \Card.test_Card()\! '''
    symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
    def get_name(self):
        return self.name
    def get_suit(self):
        return self.suit
    def __repr__(self):
        return f"{self.name}{Card.symbols[self.suit]}"
    def test_Card():
        Names = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
        Suits = ['D','C','H','S']
        deck = [Card(str(n), s) for s in Suits for n in Names]
        random.shuffle(deck)
        res = [str(card) for card in deck]
        return ' '.join(res)
    #---------------------------------------------------------------------
    def render(self, x, y, color='blue', RENDER=False):
        ''' วาดไพ่ด้วยเต่า '''
        if not RENDER:
            return None
        # Draw border
        pen.penup()
        pen.color(color)
        pen.goto(x+50, y+75)
        xy = ((x+50, y+75), (x+50, y-75), (x-50, y-75), (x-50, y+75))
        pen.begin_fill()
        pen.pendown()
        for pos in xy:
            pen.goto(pos)
        pen.end_fill()
        pen.penup()
        # Draw card info
        if self.name not in ['','O']:
            # Draw suit in the middle
            pen.color('white')
            pen.goto(x-18, y-30)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))
            # Draw top left
            pen.goto(x-40, y+45)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x-40, y+25)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
            # Draw bottom right
            pen.goto(x+30, y-60)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x+30, y-80)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
        pen.penup()
    #---------------------------------------------------------------------

class Deck:
    ''' Deck(): สร้างสำรับไพ่ '''
    Names = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
    Suits = ['D','C','H','S']
    def __init__(self):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
    def shuffle(self):
        random.shuffle(self.cards)
    def get_card(self):
        return self.cards.pop()
    def set_cards(self, cards):
        self.cards = cards
    def reset(self, n=1):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
        for i in range(n):
            self.shuffle()
    def __repr__(self):
        res = [str(x) for x in self.cards]
        return ' '.join(res)

def preamble(RENDER=False):
    ''' จัดการ environment ในการวาดเต่า '''
    if not RENDER:
        return None
    #--------------------------------------------------------------------------------------
    global wn, pen
    wn, pen = turtle.Screen(), turtle.Turtle()
    wn.bgcolor('black')
    wn.setup(800, 600)
    wn.title('Deck of Cards Simulator by @TokyoEdtech, rebrewed by KunTotoNaMikeLabDotNet')
    pen.speed(0)
    pen.hideturtle()
    #--------------------------------------------------------------------------------------

def test_turtle_deck(RENDER=False):
    ''' ไว้ตรวจสอบเต่าวาดไพ่ ฟังชัน Card.render() '''
    preamble(RENDER)
    # create a deck f card
    deck = Deck()
    # shuffle deck
    deck.reset()
    print(deck)
    # render n cards (back) in a row
    nbOfCards = 5
    start_x = -250
    for x in range(nbOfCards):
        card = Card('', '')
        card.render(start_x + x*125, 175, 'orange', RENDER=True)
    time.sleep(1)
    # re-render n cards in a row
    start_x = -250
    for x in range(nbOfCards):
        card = deck.get_card()
        card.render(start_x + x*125, 175, RENDER=True)
    print('Done..')

def createVirtualDeck(s='K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠'):
    dd = s.split()
    res = []
    suit = {'♦':'D','♣':'C','♥':'H','♠':'S'}
    for d in dd:
        card = Card(d[0], suit[d[1]])
        res.append(card)
    deck = Deck()
    deck.set_cards(res)
    return deck

def play(player1='Computer', player2='Player', d=None, RENDER=False):
    print('Welcome to MikeLab BlackJack Casino.')
    preamble(RENDER)
    # create a deck of cards
    if d==None:
        deck = Deck()
        deck.reset()
    else:
        deck = createVirtualDeck(d)
    txt = '->'
    p1 = myCards()
    p2 = myCards()
    deck.cards = deck.cards[::-1]
    

    for i in range(2):
        p1.inpcard(deck.cards[0])
        deck.cards.pop(0)

        p2.inpcard(deck.cards[0])
        deck.cards.pop(0)
    
    time = 1
    resa = [str(x) for x in p1.carrycar]
    resb = [str(x) for x in p2.carrycar]
    a = ' '.join([f"O{resa[0][1]}",resa[1]])
    b = ' '.join(resb)
    scorea = score(["O♠",resa[1]],time)
    scoreb = score(resb,time)
    print(f"{player1:>9}: {a:<5} {txt:>12} {scorea}")
    print(f"{player2:>9}: {b:<5} {txt:>12} {scoreb}")
    scorea = score(resa,time)
    bjb = False
    bja = False
    bj = True
    lima = False
    limb = False
    space = 0
    spacea = 0
    fst = True
    if scoreb == 21:
        bjb = True
        limb = True
    if scorea == 21:
        bja = True
        lima = True
    while not limb:
        if not bjb and not limb:
            yn = input("Draw another card (y/n): ")
            try:
                if yn == 'y' or yn == 'Y':
                    p2.inpcard(deck.cards[0])
                    deck.cards.pop(0)
                    resb = [str(x) for x in p2.carrycar]
                    b = ' '.join(resb)
                    scoreb = score(resb)
                    print(f"{player2:>9}: {b:<5} {txt:>{9-space}} {scoreb}")
                    space += 3
                elif yn == 'n' or yn == 'N':
                    limb = True
                if scoreb > 21 or len(p2.carrycar) == 5:
                    limb = True
                    if len(p2.carrycar) == 5 and scoreb <= 21:
                        bjb = True
                if scoreb == 21:
                    limb = True
                
            except:
                pass
            
    while not lima:
        if not bja and not lima:
            if scorea <= 16 or fst:
                p1.inpcard(deck.cards[0])
                deck.cards.pop(0)
                resa = [str(x) for x in p1.carrycar]
                a = ' '.join(resa)
                scorea = score(resa)
                spacea += 3
                fst = False
            else:
                lima = True
        if scorea > 21 or len(p1.carrycar) == 5:
            lima = True
            if len(p1.carrycar) == 5 and scorea <= 21:
                bja = True
        if scorea == 21:
            lima = True
    if bjb:
        while True:
            if not bja and len(p1.carrycar) != 5 and scorea < 21:
                scorea = score(resa)
                if (scorea <= 21) or fst:
                    p1.inpcard(deck.cards[0])
                    deck.cards.pop(0)
                    resa = [str(x) for x in p1.carrycar]
                    a = ' '.join(resa)
                    scorea = score(resa)
                    spacea += 3
            else:
                break
            if len(p1.carrycar) == 5 and scorea <= 21:
                bja = True
                break
            elif len(p1.carrycar) == 5 and scorea > 21:
                break
                
    a = ' '.join(resa)    
    print("+++++++++++++++++++++++++++++++++")
    print(f"{player1:>9}: {a:<5} {txt:>{12-spacea}} {scorea}")
    print(f"{player2:>9}: {b:<5} {txt:>{12-space}} {scoreb}")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    if bja and bjb:
        print("Draw!")
    elif bja and not bjb:
        print(f"{player1} wins.")
    elif bjb and not bja:
        print(f"{player2} wins.")
    else:
        bj = False
    if scorea <= 21 and scoreb <= 21 and scorea < scoreb and not bj:
        print(f"{player2} wins.")
    elif scorea <= 21 and scoreb <= 21 and scoreb < scorea and not bj:
        print(f"{player1} wins.")
    elif scorea <= 21 and scoreb <= 21 and scoreb == scorea and not bj:
        print(f"Draw!")
    elif scorea > 21 and scoreb > 21 and not bj:
        print("Draw!")
    elif scorea > 21 and scoreb <= 21 and not bj:
        print(f"{player2} wins.")
    elif scoreb > 21 and scorea <= 21 and not bj:
        print(f"{player1} wins.")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

    
    
        
    
    
        

# a = Card("A","D")
# preamble(RENDER = True)
# a.render(0,0,RENDER=True)
def testcase01():
    random.seed(2)
    play()
def testcase02():
    random.seed(16)
    play()
def testcase03():
    random.seed(30)
    play()
def testcase04():
    s = 'K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠'
    play('Toto', 'Tutu', d=s)

def testcase05():
    s = 'A♣ 3♥ 2♠ T♥ 8♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase06():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase07():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ T♠'
    play(d=s)
def testcase08():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ Q♥ 3♠'
    play(d=s)
def testcase09():
    s = '5♠ A♥ A♣ 8♥ J♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
#------------------------------------------
q = int(input())
if q==1:
    testcase01()
elif q==2:
    testcase02()
elif q==3:
    testcase03()
elif q==4:
    testcase04()
elif q==5:
    testcase05()
elif q==6:
    testcase06()
elif q==7:
    testcase07()
elif q==8:
    testcase08()
elif q==9:
    testcase09()