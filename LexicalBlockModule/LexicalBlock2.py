from LexicalBlockModule.FinalRecoginzerStates import FinalRecognizerStates
from TransliterationModule.StringCharTypes import StringCharClasses
from LexicalBlockModule.MinimalFinalRecognizer import FinalRecognizer
from LexicalBlockModule.MinimalFinalRecognizer import StateSwitcher

def LexicalBlock2(lexemes):
    #Создаем экземпляр класса, в котором хранятся все состояния конечного распознавателя. Также массив с символами, классами слов и запоминаем предыдущий класс лексемы
    states = FinalRecognizerStates
    symbols = []
    classes = []
    previousLexemClass = lexemes[0][1]

    for lexeme in lexemes:
        #Каждую итерацию цикла вызываем конечный распознаватель и проверяем состояния. Также запоминаем предыдущий класс лексемы
        FinalRecognizer(symbols, classes, lexeme, states)
        StateSwitcher(lexeme[1], previousLexemClass, states)
        previousLexemClass = lexeme[1]


    resultTokenChain = [("", "")]

    #Тут мы собираем все символы с одинаковыми классами и двигаем их вперед, пока не встретим символ другого класса.
    #Во втором цикле отсекаем ненужные и добавляем нужные в итоговую цепь токенов
    for i in range(len(symbols) - 1):
        if classes[i] == StringCharClasses.space:
            symbols[i] = None
            classes[i] = None
            continue
        if classes[i] == classes[i + 1]:
            symbols[i + 1] = symbols[i] + symbols[i + 1]
            symbols[i] = None
            classes[i] = None

    for i in range(len(symbols)):
        if symbols[i] != None:
            resultTokenChain.append((symbols[i], classes[i]))

    #Тут удаляем нулевой элемент, так как чтобы создать кортежный массив было необходимо нулевой элемент сделать кортежным(возможно)
    del resultTokenChain[0]

    return resultTokenChain