#В этом классе хранятся все возможные классы отдельных символов, то есть если в блоке транслитерации мы видим букву то присваиваем ему letter и так далее.
class StringCharClass:
    letter = "буква"
    space = "пробел"
    equal = "равно"
    digital = "цифра"
    semicolon = "тчкзпт"

    #Этот метод определяет какой именно класс у символа, используем мы его в функции транслитерации
    def RecognizeCharacter(self, char):
        stringChar = StringCharClass()
        return {
            char == ' ': stringChar.space,
            char == ';': stringChar.semicolon,
            char == '=': stringChar.equal,
            char.isalpha(): stringChar.letter,
            char.isnumeric(): stringChar.digital
        }[True]

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


print(LexicalBlock(TransliterationBlock(input())))
#Some checkout
print(5)
