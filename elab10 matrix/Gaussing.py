# Function to read the matrix from a file and convert to Fraction
def readMat(fn='gauss01.txt'):
    m = []
    with open(fn) as fp:
        for line in fp:
            m.append(line.strip().split(' '))
    return m

def printMat(m):
    for row in m:
        print(' '.join([str(x) for x in row]))
    print()

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    def evaluate(self):
        return self.numerator/self.denominator
    def add(self,n=0):
        s = n*self.denominator
        a = self.numerator + s
        return Fraction(a,self.denominator)
    def multiply(self,n=0):
        a = self.numerator * n
        return Fraction(a,self.denominator)
    def __add__(self,x):
        a = self.numerator*x.denominator
        b = self.denominator*x.denominator
        c = x.numerator*self.denominator
        return Fraction(a+c,b)
    def __mul__(self,x):
        a = self.numerator*x.numerator
        b = self.denominator*x.denominator
        return Fraction(a,b)
    def __sub__(self,x):
        a = self.numerator*x.denominator
        b = self.denominator*x.denominator
        c = x.numerator*self.denominator
        return Fraction(a-c,b)
    def simplify(self):
        common = gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common
        if self.denominator < 0:  # ทำให้ตัวส่วนเป็นบวกเสมอ
            self.numerator *= -1
            self.denominator *= -1
    def __str__(self):
        if self.denominator == 1:
            return f"{int(self.numerator)}"
        if self.numerator == 0:
            return "0 / 1"
        if self.denominator == 0:
            return "1 / 0"
        return f"{int(self.numerator)}/{int(self.denominator)}"
    
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def row_operation(mat):
    ans = []
    check = 1
    mnum = 1
    nnum = len(mat) + 1
    now_i = 0
    now_j = 0
    phase = 0
    time = 0
    for i in range(1,len(mat)+1):
        time += i
    while check != (time+1):
        if now_i == len(mat):
            now_i = phase
            now_j += 1
        if check == 1 or check == mnum + nnum:
            mnum = check
            nnum -= 1
            phase += 1
            if mat[now_i][now_j].denominator == 1:
                print(f"R{phase} => R{phase}/({int(mat[now_i][now_j].numerator)})")
            else:
                print(f"R{phase} => R{phase}/({int(mat[now_i][now_j].numerator)}/{int(mat[now_i][now_j].denominator)})")
            a = mat[now_i][now_j]
            for j in range(len(mat[now_i])):
                if a.denominator == 1:
                    mat[now_i][j] = mat[now_i][j] * Fraction(1, a.numerator)
                else:
                    mat[now_i][j] = mat[now_i][j] * Fraction(a.denominator, a.numerator)
            for row in mat:
                for value in row:
                    if value.denominator == 1 or value.numerator == 0 or value.numerator%value.denominator == 0:
                        if value.numerator%value.denominator == 0 and value.denominator != 0:
                            res = value.numerator/value.denominator
                            print(f"{int(res):>8}",end="")
                        else:
                            print(f"{int(value.numerator):>8}", end="")
                    else:
                        a = f"{int(value.numerator)}/{int(value.denominator)}"
                        print(f"{a:>8}", end="")
                print()
            print()

            now_i += 1
        else:
            if mat[now_i][now_j].numerator != 0:
                Rtmp = [mat[phase - 1][j] * mat[now_i][now_j] for j in range(len(m[now_i]))]
                if mat[now_i][now_j].denominator == 1:
                    print(f"R{phase}'->({int(mat[now_i][now_j].numerator)})*R{phase}",end = ' ')
                else:
                    print(f"R{phase}'->({int(mat[now_i][now_j].numerator)}/{int(mat[now_i][now_j].denominator)})*R{phase}",end = ' ')
                print('[',end='')
                cnt = 0
                for i in Rtmp:
                    if i.denominator == 1:
                        print(int(i.numerator),end='')
                    else:
                        print(i,end='')
                    cnt += 1
                    if cnt != len(mat)+1:
                        print(',',end=' ')
                print(']')  
                print(f"R{now_i + 1} ==> R{now_i + 1}-R{phase}'")

                for j in range(len(mat[now_i])):
                    mat[now_i][j] = mat[now_i][j] -Rtmp[j]  

                for row in mat:
                    for value in row:
                        if value.denominator == 1:
                            print(f"{int(value.numerator):>8}", end="")
                        else:
                            a = f"{int(value.numerator)}/{int(value.denominator)}"
                            print(f"{a:>8}", end="")
                    print()
                print()

            now_i += 1
        check += 1
    print("Result from Gaussian Elimination: ")
    for row in mat:
        for value in row:
            if value.denominator == 1 or value.numerator == 0 or value.numerator%value.denominator == 0:
                if value.numerator%value.denominator == 0 and value.denominator != 0:
                    res = value.numerator/value.denominator
                    print(f"{int(res):>8}",end="")
                else:
                    print(f"{int(value.numerator):>8}", end="")
            else:
                a = f"{int(value.numerator)}/{int(value.denominator)}"
                print(f"{a:>8}", end="")
        print()
    print()
    for i in range(len(m)):
        if i == (len(m)-1):
            if mat[i][len(m)].denominator == 1:
                ans.append(int(mat[i][len(m)].numerator))
            else:
                ans.append(mat[i][len(m)])
        else:
            ans.append('x')
    while True:
        for i in range(len(ans)-2,-1,-1):
            res = mat[i][len(m)]
            for j in range(len(ans)-1,i,-1):
                res -= mat[i][j]*ans[j]
            ans[i] = res
        break
    print("After Back-Substitution:")
    for i in range(len(ans)):
        if ans[i].denominator == 1:
            print(f'{alphabet[i]} =',int(ans[i].numerator))
        else:
            print(f'{alphabet[i]} = {int(ans[i].numerator)}/{int(ans[i].denominator)}')
        
filename = input("Enter filename: ")
print("Augmented Matrix:")
m = readMat(filename)
mat = [[Fraction(int(num), 1) for num in row] for row in m]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for row in mat:
    for value in row:
        if value.denominator == 1 or value.numerator == 0 or value.numerator%value.denominator == 0:
            if value.numerator%value.denominator == 0 and value.denominator != 0:
                res = value.numerator/value.denominator
                print(f"{int(res):>8}",end="")
            else:
                print(f"{int(value.numerator):>8}", end="")
        else:
            a = f"{int(value.numerator)}/{int(value.denominator)}"
            print(f"{a:>8}", end=" ")
    print()
print()

row_operation(mat)



