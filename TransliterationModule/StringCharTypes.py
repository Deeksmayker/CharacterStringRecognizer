import re

class StringCharClasses:
    letter = "буква"
    space = "пробел"
    digital = "цифра"
    semicolon = "тчкзпт"
    equal = "равно"
    error = "ошибка"
    openBracket = "открывающая скобка"
    closeBracket = "закрывающая скобка"
    more = "больше"
    less = "меньше"
    hexadecimal = "шестнадцатиричный знак"
    comma = "запятая"

    #Этот метод определяет какой именно класс у символа, используем мы его в функции транслитерации
    def RecognizeCharacter(char):
        if char == ' ': return StringCharClasses.space
        if char == ';': return StringCharClasses.semicolon
        if char.isalpha() and re.search(r'[a-zA-Z]', char): return StringCharClasses.letter
        if char.isnumeric(): return StringCharClasses.digital
        if char == '(': return StringCharClasses.openBracket
        if char == ')': return StringCharClasses.closeBracket
        if char == '>': return StringCharClasses.more
        if char == '<': return StringCharClasses.less
        if char == '$': return StringCharClasses.hexadecimal
        if char == ',': return StringCharClasses.comma
        if char == '=': return StringCharClasses.equal
        
        return StringCharClasses.error

    def IsLetterHexadecimal(char):
        return re.search(r'[a-fA-F]', char)
