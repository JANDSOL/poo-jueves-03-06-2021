class Fraction:
    
    def __init__(self, numerator=0, denominator=0):
        """Method constructor."""

        self.num = numerator
        self.den = denominator

    def __str__(self):
        """Printing method."""

        return '{}/{}'.format(self.num, self.den)


if __name__ == '__main__':
    pass
