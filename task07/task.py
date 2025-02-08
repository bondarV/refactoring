class RomanNumerals:
    value_map_list = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    value_map_dict = {symbol: value for value, symbol in value_map_list}


class DecimalToRoman:
    def __init__(self):
        self.roman_numeral = ''
        self.num = 0

    def convert(self, num):
        self.num = num
        self.roman_numeral = ''
        self.implementation_roman()
        return self.roman_numeral

    def implementation_roman(self):
        for value, symbol in RomanNumerals.value_map_list:
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
        self.decimal = 0
        self.i = 0

    def convert(self, roman_number):
        self.decimal = 0
        self.i = 0
        while self.check_length(roman_number):
            if self.check_on_pair(roman_number):
                self.found_combo_of_literals(roman_number)
            else:
                self.found_solo_literal(roman_number)
        return self.decimal

    def check_length(self, roman_number):
        return self.i < len(roman_number)

    def check_on_pair(self, roman_number):
        return self.i + 1 < len(roman_number) and roman_number[self.i:self.i + 2] in RomanNumerals.value_map_dict

    def found_solo_literal(self, roman_number):
        self.decimal += RomanNumerals.value_map_dict[roman_number[self.i]]
        self.i += 1

    def found_combo_of_literals(self, roman_number):
        self.decimal += RomanNumerals.value_map_dict[roman_number[self.i:self.i + 2]]
        self.i += 2


if __name__ == '__main__':
    decimal_to_roman_converter = DecimalToRoman()
    print(decimal_to_roman_converter.convert(1987))

    roman_to_decimal_converter = RomanToDecimal()
    print(roman_to_decimal_converter.convert('MCMLXXXVII'))
