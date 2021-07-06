import re

class StringCharClasses:
    letter = "буква"
    space = "пробел"
    equal = "равно"
    digital = "цифра"
    semicolon = "тчкзпт"
    symbol = "знак"
    error = "ошибка"

    #Этот метод определяет какой именно класс у символа, используем мы его в функции транслитерации
    def RecognizeCharacter(self, char):
    
        if re.search(r'[а-яА-ЯёЁ]', char): return StringCharClasses.error

        if char == ' ': return StringCharClasses.space
        if char == ';': return StringCharClasses.semicolon
        if char == '=': return StringCharClasses.equal
        if char.isalpha(): return StringCharClasses.letter
        if char.isnumeric(): return StringCharClasses.digital
        if char == '+' or char == '-': return StringCharClasses.symbol
        
        return StringCharClasses.error