import math

class Fraction:
    def __init__(self, numerator, denominator):
        gcd = math.gcd(int(numerator),int(denominator))
        self._numerator = int(numerator/gcd)
        self._denominator = int(denominator/gcd)

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, value):
        if isinstance(value, int):
            self._numerator = value
        else:
            print('Please only enter integer numbers!')

    @property
    def denominator(self):
        if self._denominator == 0:
            raise ZeroDivisionError('You cannot divide by zero!')
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ZeroDivisionError('You cannot divide by zero!')
        elif isinstance(value, int):
            self._denominator = value
            print('hi')
        else:
            print('Please only enter integer numbers!')

    def __repr__(self):
        return 'Fraction({}, {})'.format(self.numerator,self.denominator)

    def __add__(self, other):
        z = (self.denominator*other.denominator)
        x, y = self.numerator*other.denominator, other.numerator*self.denominator
        return Fraction(x+y,z)

    def __sub__(self, other):
        z = (self.denominator*other.denominator)
        x, y = self.numerator*other.denominator, other.numerator*self.denominator
        return Fraction(x-y, z)

    def __mul__(self, other):
        x, y = self.numerator*other.numerator, self.denominator*other.denominator
        return Fraction(x,y)

    def __truediv__(self, other):
        x, y = self.numerator*other.denominator, self.denominator*other.numerator
        return Fraction(x,y)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)



x = Fraction(5, 10)
y = Fraction(6, 7)


print(x)
print(y)
print(-x)
print(-y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x+2)
