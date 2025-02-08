class DecimalToRoman:
    def __init__(self,num):
        self.roman_numeral = ''
        self.num = num

        self.value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]

    def convert(self, num):
        self.implementation_roman()
        return self.roman_numeral

    def implementation_roman(self):
        for value, symbol in self.value_map:
            self.add_symbols(value, symbol)

    def add_symbols(self, value, symbol):
        while self.is_value_greater_equal(value):
            self.add_symbol(symbol)
            self.decrease_num(value)

    def is_value_greater_equal(self, value):
        return self.num >= value

    def add_symbol(self, symbol):
        self.roman_numeral += symbol

    def decrease_num(self, value):
        self.num -= value


class RomanToDecimal:
    def __init__(self):
        self.value_map = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
            'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
            'X': 10, 'IX': 9, 'V': 5, 'IV': 4,
            'I': 1
        }
        self.decimal = 0
        self.i = 0

    def convert(self, roman_number):
        while self.check_length(roman_number):
            if self.check_on_pair(roman_number):
                self.found_combo_of_literals(roman_number)
            else:
                self.found_solo_literal(roman_number)
        return self.decimal

    def check_length(self, roman_number):
        return self.i < len(roman_number)

    def check_on_pair(self, roman_number):
        return self.check_length(roman_number) and roman_number[self.i:self.i + 2] in self.value_map

    def found_solo_literal(self, roman_number):
        self.decimal += self.value_map[roman_number[self.i]]
        self.i += 1

    def found_combo_of_literals(self, roman_number):
        self.decimal += self.value_map[roman_number[self.i:self.i + 2]]
        self.i += 2


if __name__ == '__main__':
    decimal_to_roman_converter = DecimalToRoman()
    print(decimal_to_roman_converter.convert(1987))  # MCMLXXXVII

    roman_to_decimal_converter = RomanToDecimal()
    print(roman_to_decimal_converter.convert('MCMLXXXVII'))  # 1987
