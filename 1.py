class Fraction(object):
    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        self.reduce()

    def __str__(self):
        return "%d/%d" % (self.__num, self.__den)

    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num /= g
        self.__den /= g

    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)

    def __neg__(self):  # перегрузка оператора отрицания
        return Fraction(self.__num*-1, self.__den)

    def __invert__(self): # перегрузка оператора инвертирования
        return Fraction(self.__den, self.__num)

    def __pow__(self, power, modulo=None):  # перегрузка оператора возведения в степень
        return Fraction(self.__num**power, self.__den**power)

    def __float__(self):
        return float(self.__num/self.__den)

    def __int__(self):
        return int(self.__num/self.__den)


frac = Fraction(7, 2)
print("example")
print(frac)
print(-frac)
print(~frac)
print(frac**2)
print(float(frac))
print(int(frac))
