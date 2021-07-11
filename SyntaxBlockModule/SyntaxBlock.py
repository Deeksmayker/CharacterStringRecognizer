from KeywordIdentificationBlockModule.KeyWords import KeyWords
from LexicalBlockModule.InputLanguageCharClass import InputLanguageCharClass
from SyntaxBlockModule.AnalysisResults import AnalysisResults

def SyntaxBlock(wordsClasses):
    #Ну в начале сразу проверяем есть ли в конце точка с запятой, если нет то вываливаем ошибку
    if wordsClasses[-1] != InputLanguageCharClass.semicolon: return AnalysisResults.uncorrect

    #Ну тут всё работает по простому принципу. Мы всегда смотрим на предыдущий символ, если его класс не соответствует тому что должно то вываливаем ошибку, 
    #если же все классы слов прошли через эти ифы без ошибки то возвращем коррект на последней строке
    previousWordClass = ""
    for class in wordsClasses:
        if class == InputLanguageCharClass.error: return AnalysisResults.uncorrect
        if class == InputLanguageCharClass.logical and previousWordClass != KeyWords.keyWhile: return AnalysisResults.uncorrect
        if class == KeyWords.keyDo and previousWordClass != InputLanguageCharClass.logical: return AnalysisResults.uncorrect
        if class == KeyWords.keyIf and previousWordClass != KeyWords.keyDo: return AnalysisResults.uncorrect
        if class == InputLanguageCharClass.identifer and previousWordClass != KeyWords.keyIf: return AnalysisResults.uncorrect
        if class == InputLanguageCharClass.comparison and previousWordClass != InputLanguageCharClass.identifer: return AnalysisResults.uncorrect
        if class == InputLanguageCharClass.hexadecimalConstant and previousWordClass != InputLanguageCharClass.comparison: return AnalysisResults.uncorrect
        if class == KeyWords.keyThen and previousWordClass != InputLanguageCharClass.hexadecimalConstant: return AnalysisResults.uncorrect
        if class == KeyWords.keySubroutineCall and previousWordClass != KeyWords.keyThen: return AnalysisResults.uncorrect
        if class == InputLanguageCharClass.openBracket and previousWordClass != KeyWords.keySubroutineCall: return AnalysisResults.uncorrect
        if class == KeyWords.keyParam and previousWordClass != InputLanguageCharClass.openBracket and previousWordClass != InputLanguageCharClass.comma:
            return AnalysisResults.uncorrect
        if class == InputLanguageCharClass.closeBracket and previousWordClass != KeyWords.keyParam: return AnalysisResults.uncorrect

        previousWordClass = class

    return AnalysisResults.correct