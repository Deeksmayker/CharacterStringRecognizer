from LexicalBlockModule.InputLanguageCharClass import InputLanguageCharClass
from KeywordIdentificationBlockModule.KeyWords import KeyWords
from LexicalBlockModule.InputLanguageCharClass import InputLanguageCharClass

def KeywordIdentification(tokenChain):
    resultKeyWords = []

    for token in tokenChain:
        if token[1] != InputLanguageCharClass.identifer:
            resultKeyWords.append(token[1])
            continue

        if token[0] == "while": resultKeyWords.append(KeyWords.keyWhile)
        elif token[0] == "do": resultKeyWords.append(KeyWords.keyDo)
        elif token[0] == "if": resultKeyWords.append(KeyWords.keyIf)
        elif token[0] == "then": resultKeyWords.append(KeyWords.keyThen)
        elif resultKeyWords[-1] == KeyWords.keyThen: resultKeyWords.append(KeyWords.keySubroutineCall)
        elif resultKeyWords[-1] == InputLanguageCharClass.openBracket or resultKeyWords[-1] == InputLanguageCharClass.comma: resultKeyWords.append(KeyWords.keyParam)
        else: resultKeyWords.append(token[1])

    return resultKeyWords

 