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
    def RecognizeCharacter(char):
    
        if re.search(r'[а-яА-ЯёЁ]', char): return StringCharClasses.error

        if char == ' ': return StringCharClasses.space
        if char == ';': return StringCharClasses.semicolon
        if char == '=': return StringCharClasses.equal
        if char.isalpha(): return StringCharClasses.letter
        if char.isnumeric(): return StringCharClasses.digital
        if char == '+' or char == '-': return StringCharClasses.symbol
        
        return StringCharClasses.error


#Блок транслитерации, первый в списке
def TransliterationBlock(str):
    #Создаем массив, в который будем складывать все символы с их классами
    tokenChain = []
    #Тут проходимся по символам переданой строки, в charClass пихаем класс текущего символа, на 28 в массив засовываем сам символ и его класс на одну позицию(это называется если че кортеж)
    for char in str:
        charClass = StringCharClasses.RecognizeCharacter(char)
        tokenChain.append((char, charClass))
    return tokenChain