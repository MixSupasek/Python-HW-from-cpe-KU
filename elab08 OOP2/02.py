class Fraction:
    def __init__(self,numerator = 0,denominator = 1):
        self.numerator = numerator
        self.denominator = denominator
        list = []
        if self.numerator >= self.denominator:
            for i in range(1,int(self.numerator)):
                if self.numerator%i == 0 and self.denominator%i == 0:
                    list.append(i)
        else:
            for i in range(1,int(self.denominator)):
                if self.numerator%i == 0 and self.denominator%i == 0:
                    list.append(i)
        if len(list) == 0:
            list.append(1)
            self.numerator = self.numerator/max(list)
            self.denominator = self.denominator/max(list)
        else:
            self.numerator = self.numerator/max(list)
            self.denominator = self.denominator/max(list)
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
    def __str__(self):
        if self.numerator == 0:
            return "0 / 1"
        if self.denominator == 0:
            return "1 / 0"
        return f"{int(self.numerator)} / {int(self.denominator)}"