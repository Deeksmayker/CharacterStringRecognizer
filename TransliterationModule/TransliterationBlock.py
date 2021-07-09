from TransliterationModule.StringCharTypes import StringCharClasses

#Блок транслитерации, первый в списке
def TransliterationBlock(str):
    #Создаем массив, в который будем складывать все символы с их классами
    tokenChain = []
    #Тут проходимся по символам переданой строки, в charClass пихаем класс текущего символа, на 28 в массив засовываем сам символ и его класс на одну позицию(это называется если че кортеж)
    for char in str:
        charClass = StringCharClasses.RecognizeCharacter(char)
        tokenChain.append((char, charClass))
    return tokenChain