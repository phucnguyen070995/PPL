class Rational:

    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return Rational.gcd(b, a % b)

    def __init__(self, numer = 0, denom = 1):
        try:
            assert denom != 0, "denom must # 0"
            assert isinstance(numer, int), "numer must be Int"
            assert isinstance(denom, int), "denom must be Int"
            __g = Rational.gcd(numer, denom)
            self.numer = numer // __g
            self.denom = denom // __g
        except AssertionError as msg:
            print('Error: ' + str(msg))
            self.__init__(0, 1)


    def __int__(self):
        self.__init__(self, 0, 1)

    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)

    def __add__(self, other):
        if (isinstance(other, int)):
            return Rational(self.numer + other * self.denom, self.denom)
        else:
            raise Exception("Sorry, number must be integer!")

if __name__ == '__main__':
    x = Rational(6, 5.3)
    y = Rational()
    # z = Rational(12, 8)
    print(x)
    print(y)
    # print(z)
    print(x + 1)