class Fraction:
    
    def __init__(self, numerator=0, denominator=0):
        """Method constructor."""

        self.num = numerator
        self.den = denominator

    def __str__(self):
        """Printing method."""

        return '{}/{}'.format(self.num, self.den)


if __name__ == '__main__':
    test1, test2 = Fraction(3, 4), Fraction(4, 5)
    list_test = (test1, test2)
    
    print('*' * 39)
    for num, test in enumerate(list_test, 1):
        print('  Prueba {} de la clase Fraction: {}'.format(num, test))
    print('*' * 39)
