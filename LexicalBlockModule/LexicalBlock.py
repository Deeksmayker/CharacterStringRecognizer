#Тут также импортируем именно классы
from LexicalBlockModule.InputLanguageCharClass import InputLanguageCharClass
from TransliterationModule.StringCharTypes import StringCharClasses

def LexicalBlock(tokenChain):
    #Создаем массив в который будем складывать результат. Предыдущий класс символа нужен и сначала присваиваем ему класс первого символа из переданого нам токенЧейна.
    #В куррентТокен будем складывать текущее собранное слово
    resultTokenChain = []
    previousCharClass = tokenChain[0][1]
    currentToken = ""

    for char in tokenChain: 
        #Проверяем можно ли добавить еще один символ к слову
        if InputLanguageCharClass.IsPossibleTokenName(char[1], previousCharClass, resultTokenChain, currentToken):
            currentToken += char[0]
        
        #Если нельзя и текущий символ не пробел то в итоговый массив добавляем текущий токен и его класс (определяем с помощью той самой функции)
        elif char[1] != StringCharClasses.space:
            resultTokenChain.append((currentToken, InputLanguageCharClass.RecognizeLexicalTokenClass(currentToken)))
            #Ну и готовим уже новый куррент токен, ставим в него текущий символ на котором сейчас стоим
            currentToken = char[0]

        #тут обновляем предыдущий класс символа
        previousCharClass = char[1]        
        
    #После цикла тоже надо разок добавить токен и его класс в массив. Такое уродство возможно и можно было обойти, но писал под пивом 
    resultTokenChain.append((currentToken, InputLanguageCharClass.RecognizeLexicalTokenClass(currentToken)))

    return resultTokenChain