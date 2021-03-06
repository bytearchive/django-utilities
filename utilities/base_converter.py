class BaseConverter(object):
    decimal_digits = "0123456789"
    hexadecimal_digits = "0123456789abcdef"
    
    def __init__(self, digits):
        self.digits = digits
    
    def from_decimal(self, i):
        return self.convert(i, self.decimal_digits, self.digits)
    
    def to_decimal(self, s):
        return int(self.convert(s, self.digits, self.decimal_digits))
    
    def from_hexadecimal(self, i):
        return self.convert(i, self.hexadecimal_digits, self.digits)
    
    def to_hexadecimal(self, s):
        return int(self.convert(s, self.digits, self.hexadecimal_digits))
    
    def convert(number, fromdigits, todigits):
        # Based on http://code.activestate.com/recipes/111286/
        if str(number)[0] == '-':
            number = str(number)[1:]
            neg = 1
        else:
            neg = 0

        # make an integer out of the number
        x = 0
        for digit in str(number):
           x = x * len(fromdigits) + fromdigits.index(digit)
    
        # create the result in base 'len(todigits)'
        if x == 0:
            res = todigits[0]
        else:
            res = ""
            while x > 0:
                digit = x % len(todigits)
                res = todigits[digit] + res
                x = int(x / len(todigits))
            if neg:
                res = '-' + res
        return res
    convert = staticmethod(convert)

bin = BaseConverter('01')
hexconv = BaseConverter('0123456789ABCDEF')
base62 = BaseConverter(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
)

if __name__ == '__main__':
    nums = [-10 ** 10, 10 ** 10] + range(-100, 100)
    for convertor in [bin, hexconv, base62]:
        for i in nums:
            assert i == bin.to_decimal(bin.from_decimal(i)), '%s failed' % i
