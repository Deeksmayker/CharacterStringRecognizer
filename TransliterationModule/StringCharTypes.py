import re

class StringCharClasses:
    letter = "буква"
    space = "пробел"
    equal = "равно"
    digital = "цифра"
    semicolon = "тчкзпт"
    sign = "знак"
    error = "ошибка"
    bracket = "скобка"
    squareBracket = "квадратная скобка"
    more = "больше"
    less = "меньше"
    hexadecimal = "шестнадцатиричный знак"

    #Этот метод определяет какой именно класс у символа, используем мы его в функции транслитерации
    def RecognizeCharacter(char):
        if char == ' ': return StringCharClasses.space
        if char == ';': return StringCharClasses.semicolon
        if char == '=': return StringCharClasses.equal
        if char.isalpha() and re.search(r'[a-zA-Z]', char): return StringCharClasses.letter
        if char.isnumeric(): return StringCharClasses.digital
        if char == '+' or char == '-': return StringCharClasses.sign
        if char == '(' or char == ')': return StringCharClasses.bracket
        if char == '[' or char == ']': return StringCharClasses.squareBracket
        if char == '>': return StringCharClasses.more
        if char == '<': return StringCharClasses.less
        if char == '$': return StringCharClasses.hexadecimal
        
        return StringCharClasses.error
