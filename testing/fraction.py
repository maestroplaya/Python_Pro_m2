import math


class Fraction:

    def __init__(self, num, den):
        self.num, self.den = self.get_reduced_fraction(num, den)

    @staticmethod
    def get_reduced_fraction(num, den):
        gcd = math.gcd(num, den)
        return num // gcd, den // gcd

    @staticmethod
    def get_common_denominator(den1, den2):
        common_den = den1 * den2 // math.gcd(den1, den2)
        return common_den

    def __str__(self):
        return f'Дробь {self.num}/{self.den}'

    def __add__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        num = common_den // self.den * self.num + common_den // other.den * other.num
        num, den = self.get_reduced_fraction(num, common_den)
        return num, den

    def __iadd__(self, other):
        self.num, self.den = self + other
        return self

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __ne__(self, other):
        return self.num != other.num or self.den != other.den

    def __gt__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num > common_den // other.den * other.num

    def __ge__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num >= common_den // other.den * other.num

    def __lt__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num < common_den // other.den * other.num

    def __le__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num <= common_den // other.den * other.num


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 9)

print(fraction1)
print(fraction2)
print(fraction1 + fraction2)

fraction1 += fraction2
print(fraction1)

print(fraction2 < fraction1)

