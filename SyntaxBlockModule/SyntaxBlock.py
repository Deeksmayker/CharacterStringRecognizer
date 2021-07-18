from KeywordIdentificationBlockModule.KeyWords import KeyWords
from LexicalBlockModule.InputLanguageCharClass import InputLanguageCharClass
from SyntaxBlockModule.AnalysisResults import AnalysisResults

def SyntaxBlock(wordsClasses):
    #Ну в начале сразу проверяем есть ли в конце точка с запятой, если нет то вываливаем ошибку
    if wordsClasses[-1] != InputLanguageCharClass.semicolon: return AnalysisResults.uncorrect

    #Ну тут всё работает по простому принципу. Мы всегда смотрим на предыдущий символ, если его класс не соответствует тому что должно то вываливаем ошибку, 
    #если же все классы слов прошли через эти ифы без ошибки то возвращем коррект на последней строке
    previousWordClass = ""
    for wordClass in wordsClasses:
        if wordClass == InputLanguageCharClass.error: return AnalysisResults.uncorrect
        if wordClass == InputLanguageCharClass.logical and previousWordClass != KeyWords.keyWhile: return AnalysisResults.uncorrect
        if wordClass == KeyWords.keyDo and previousWordClass != InputLanguageCharClass.logical: return AnalysisResults.uncorrect
        if wordClass == KeyWords.keyIf and previousWordClass != KeyWords.keyDo: return AnalysisResults.uncorrect
        if wordClass == InputLanguageCharClass.identifer and previousWordClass != KeyWords.keyIf: return AnalysisResults.uncorrect
        if wordClass == InputLanguageCharClass.comparison and previousWordClass != InputLanguageCharClass.identifer: return AnalysisResults.uncorrect
        if wordClass == InputLanguageCharClass.hexadecimalConstant and previousWordClass != InputLanguageCharClass.comparison: return AnalysisResults.uncorrect
        if wordClass == KeyWords.keyThen and previousWordClass != InputLanguageCharClass.hexadecimalConstant: return AnalysisResults.uncorrect
        if wordClass == KeyWords.keySubroutineCall and previousWordClass != KeyWords.keyThen: return AnalysisResults.uncorrect
        if wordClass == InputLanguageCharClass.openBracket and previousWordClass != KeyWords.keySubroutineCall: return AnalysisResults.uncorrect
        if wordClass == KeyWords.keyParam and previousWordClass != InputLanguageCharClass.openBracket and previousWordClass != InputLanguageCharClass.comma:
            return AnalysisResults.uncorrect
        if wordClass == InputLanguageCharClass.closeBracket and previousWordClass != KeyWords.keyParam: return AnalysisResults.uncorrect

        previousWordClass = wordClass

    return AnalysisResults.correct