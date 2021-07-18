#Также импортируем классы
from LexicalBlockModule.InputLanguageCharClass import InputLanguageCharClass
from KeywordIdentificationBlockModule.KeyWords import KeyWords
from LexicalBlockModule.InputLanguageCharClass import InputLanguageCharClass
from SyntaxBlockModule.AnalysisResults import AnalysisResults

def KeywordIdentification(tokenChain):
    resultWordsClasses = []

    #тут нас интересуют только идентефикаторы, из них мы хотим получить полноценные ключевые слова, поэтому в начале каждой итерации проверяем является ли токен
    #идентификатором, если нет то просто добавляем его в итоговый массив и идем на следующую итерацию
    logicalConstans = ["true", "false"]

    for token in tokenChain:
        if token[1] == InputLanguageCharClass.logical and not(token[0].lower() in logicalConstans):
            AnalysisResults.PrintOnWrongLine()

        if token[1] != InputLanguageCharClass.identifer:
            resultWordsClasses.append(token[1])
            continue

        #Ну тут всё понятно по конкретным ключевым словам, просто проверяем идентификаторы и добавляем в массив соответствующие ключевые слова
        if token[0] == "while": resultWordsClasses.append(KeyWords.keyWhile)
        elif token[0] == "do": resultWordsClasses.append(KeyWords.keyDo)
        elif token[0] == "if": resultWordsClasses.append(KeyWords.keyIf)
        elif token[0] == "then": resultWordsClasses.append(KeyWords.keyThen)
        #Тут мы уже проверяем последний на данный момент элемент массива, чтобы понять что мы находимся на вызове подпрограммы или параметре
        elif resultWordsClasses[-1] == KeyWords.keyThen: resultWordsClasses.append(KeyWords.keySubroutineCall)
        elif resultWordsClasses[-1] == InputLanguageCharClass.openBracket or resultWordsClasses[-1] == InputLanguageCharClass.comma: resultWordsClasses.append(KeyWords.keyParam)
        else: resultWordsClasses.append(token[1])

    return resultWordsClasses

 