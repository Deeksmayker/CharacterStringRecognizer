from LexicalBlockModule.InputLanguageCharClass import InputLanguageCharClass
from KeywordIdentificationBlockModule.KeyWords import KeyWords
from LexicalBlockModule.InputLanguageCharClass import InputLanguageCharClass
from SyntaxBlockModule.AnalysisResults import AnalysisResults

def KeywordIdentification(tokenChain):
    resultWordTypes = []

    logicalConstans = ["true", "false"]

    for token in tokenChain:
        if token[1] == InputLanguageCharClass.logical and not(token[0].lower() in logicalConstans):
            AnalysisResults.PrintOnWrongLine()

        if token[1] != InputLanguageCharClass.identifer:
            resultWordTypes.append(token[1])
            continue

        if token[0] == "while": resultWordTypes.append(KeyWords.keyWhile)
        elif token[0] == "do": resultWordTypes.append(KeyWords.keyDo)
        elif token[0] == "if": resultWordTypes.append(KeyWords.keyIf)
        elif token[0] == "then": resultWordTypes.append(KeyWords.keyThen)
        elif resultWordTypes[-1] == KeyWords.keyThen: resultWordTypes.append(KeyWords.keySubroutineCall)
        elif resultWordTypes[-1] == InputLanguageCharClass.openBracket or resultWordTypes[-1] == InputLanguageCharClass.comma: resultWordTypes.append(KeyWords.keyParam)
        else: resultWordTypes.append(token[1])

    return resultWordTypes

 