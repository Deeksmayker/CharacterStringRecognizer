import re

class StringCharClasses:
    letter = "буква"
    space = "пробел"
    equal = "равно"
    digital = "цифра"
    semicolon = "тчкзпт"
    symbol = "знак"
    error = "ошибка"
    bracket = "скобка"
    squareBracket = "квадратная скобка"

    #Этот метод определяет какой именно класс у символа, используем мы его в функции транслитерации
    def RecognizeCharacter(char):
        if char == ' ': return StringCharClasses.space
        if char == ';': return StringCharClasses.semicolon
        if char == '=': return StringCharClasses.equal
        if char.isalpha() and re.search(r'[a-zA-Z]', char): return StringCharClasses.letter
        if char.isnumeric(): return StringCharClasses.digital
        if char == '+' or char == '-': return StringCharClasses.symbol
        if char == '(' or char == ')': return StringCharClasses.bracket
        if char == '[' or char == ']': return StringCharClasses.squareBracket
        
        return StringCharClasses.error

class InputLanguageCharClass:
    identifer = "ИДЕНТЕФИКАТОР"
    equal = "РАВНО"
    integer = "ЦЕЛОЕ"
    semicolon = "тчкзпт"

    def IsPossibleIdentifierName(charClass, previousCharClass, resultTokenChain):
        tokenArrayLength = len(resultTokenChain)
        return charClass == previousCharClass or (tokenArrayLength >= 2 and resultTokenChain[tokenArrayLength - 2][0] == "const"
        and previousCharClass == StringCharClasses.letter and charClass == StringCharClasses.digital)


#Блок транслитерации, первый в списке
def TransliterationBlock(str):
    #Создаем массив, в который будем складывать все символы с их классами
    tokenChain = []
    #Тут проходимся по символам переданой строки, в charClass пихаем класс текущего символа, на 28 в массив засовываем сам символ и его класс на одну позицию(это называется если че кортеж)
    for char in str:
        charClass = StringCharClasses.RecognizeCharacter(char)
        tokenChain.append((char, charClass))
    return tokenChain

def LexicalBlock(tokenChain):
    resultTokenChain = [("", "")]  
    previousCharClass = tokenChain[0][1]

    for char in tokenChain: 
        if InputLanguageCharClass.IsPossibleIdentifierName(char[1], previousCharClass, resultTokenChain):
            resultTokenChain[len(resultTokenChain) - 1][0] += char[0]
        
        elif char[1] != StringCharClasses.space:
             resultTokenChain.append((char[0], ""))

        previousCharClass = char[1]        
        
    return resultTokenChain


print(TransliterationBlock(input()))
