class Fraction:
    
    def __init__(self, numerator, denominator):
        """Method constructor."""

        self.num = numerator
        self.den = denominator

    def __str__(self):
        """Printing method."""

        return self.num, '/', self.den


if __name__ == '__main__':
    pass
