# 最大公因数
def GCD(x, y):
    if y > x:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x


# 最小公倍数
def LCM(x, y):
    return x * y // (GCD(x, y))


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            common_denominator = LCM(self.denominator, other.denominator)
            common_numerator = (common_denominator // self.denominator) * self.numerator + (
                    common_denominator // other.denominator) * other.numerator
            common_factor = GCD(common_numerator, common_denominator)
            result_numerator = common_numerator // common_factor
            result_denominator = common_denominator // common_factor
            return Fraction(result_numerator, result_denominator)


if __name__ == '__main__':
    m, n, x, y = map(int, input().split())
    a = Fraction(m, n)
    b = Fraction(x, y)
    print(f"{(a + b).numerator}/{(a + b).denominator}")
