from KeywordIdentificationBlockModule.KeyWords import KeyWords
from LexicalBlockModule.InputLanguageCharClass import InputLanguageCharClass
from SyntaxBlockModule.AnalysisResults import AnalysisResults

def SyntaxBlock(lineKeyWords):
    if lineKeyWords[-1] != InputLanguageCharClass.semicolon: return AnalysisResults.uncorrect

    previousKeyWord = ""
    for keyWord in lineKeyWords:
        if keyWord == InputLanguageCharClass.error: return AnalysisResults.uncorrect
        if keyWord == InputLanguageCharClass.logical and previousKeyWord != KeyWords.keyWhile: return AnalysisResults.uncorrect
        if keyWord == KeyWords.keyDo and previousKeyWord != InputLanguageCharClass.logical: return AnalysisResults.uncorrect
        if keyWord == KeyWords.keyIf and previousKeyWord != KeyWords.keyDo: return AnalysisResults.uncorrect
        if keyWord == InputLanguageCharClass.identifer and previousKeyWord != KeyWords.keyIf: return AnalysisResults.uncorrect
        if keyWord == InputLanguageCharClass.comparison and previousKeyWord != InputLanguageCharClass.identifer: return AnalysisResults.uncorrect
        if keyWord == InputLanguageCharClass.hexadecimalConstant and previousKeyWord != InputLanguageCharClass.comparison: return AnalysisResults.uncorrect
        if keyWord == KeyWords.keyThen and previousKeyWord != InputLanguageCharClass.hexadecimalConstant: return AnalysisResults.uncorrect
        if keyWord == KeyWords.keySubroutineCall and previousKeyWord != KeyWords.keyThen: return AnalysisResults.uncorrect
        if keyWord == InputLanguageCharClass.openBracket and previousKeyWord != KeyWords.keySubroutineCall: return AnalysisResults.uncorrect
        if keyWord == KeyWords.keyParam and previousKeyWord != InputLanguageCharClass.openBracket and previousKeyWord != InputLanguageCharClass.comma:
            return AnalysisResults.uncorrect
        if keyWord == InputLanguageCharClass.closeBracket and previousKeyWord != KeyWords.keyParam: return AnalysisResults.uncorrect

        previousKeyWord = keyWord

    return AnalysisResults.correct