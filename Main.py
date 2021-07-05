import re

#В этом классе хранятся все возможные классы отдельных символов, то есть если в блоке транслитерации мы видим букву то присваиваем ему letter и так далее.
class StringCharClass:
    letter = "буква"
    space = "пробел"
    equal = "равно"
    digital = "цифра"
    semicolon = "тчкзпт"
    symbol = "знак"
    error = "ошибка"

    #Этот метод определяет какой именно класс у символа, используем мы его в функции транслитерации
    def RecognizeCharacter(self, char):
        stringChar = StringCharClass()

        if re.search(r'[а-яА-ЯёЁ]', char): return stringChar.error

        if char == ' ': return stringChar.space
        if char == ';': return stringChar.semicolon
        if char == '=': return stringChar.equal
        if char.isalpha(): return stringChar.letter
        if char.isnumeric(): return stringChar.digital
        if char == '+' or char == '-': return stringChar.symbol
        
        return stringChar.error

#Блок транслитерации, первый в списке
def TransliterationBlock(str):
    #Создаем массив, в который будем складывать все символы с их классами и на 24 строке создаем экземпляр класса в котором находятся виды символов
    tokenChain = []
    stringCharacters = StringCharClass()
    #Тут проходимся по символам переданой строки, в charClass пихаем класс текущего символа, на 28 в массив засовываем сам символ и его класс на одну позицию(это называется если че кортеж)
    for char in str:
        charClass = stringCharacters.RecognizeCharacter(char)
        tokenChain.append((char, charClass))
    return tokenChain

def LexicalBlock(tokenChain):
    stringCharacters = StringCharClass()
    resultTokenChain = [""]  
    previousCharClass = tokenChain[0][1]

    for char in tokenChain: 
        if char[1] == previousCharClass:
            resultTokenChain[len(resultTokenChain) - 1] += char[0]
        
        elif char[1] != stringCharacters.space:
             resultTokenChain.append(char[0])

        previousCharClass = char[1]        
        
    return resultTokenChain


print(TransliterationBlock(input()))
