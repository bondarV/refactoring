class DecimalToRoman:
    def __init__(self):
        self.value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]

    def convert(self, num):
        roman_numeral = ''
        for value, symbol in self.value_map:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral


class RomanToDecimal:
    def __init__(self):
        self.value_map = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
            'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
            'X': 10, 'IX': 9, 'V': 5, 'IV': 4,
            'I': 1
        }

    def convert(self, roman):
        decimal = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i + 2] in self.value_map:
                decimal += self.value_map[roman[i:i + 2]]
                i += 2
            else:
                decimal += self.value_map[roman[i]]
                i += 1
        return decimal


if __name__ == '__main__':
    converter = RomanToDecimal()
    print(converter.convert('MCMLXXXVII'))

    converter = DecimalToRoman()
    print(converter.convert(1987))
