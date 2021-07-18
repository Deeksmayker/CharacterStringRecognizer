from LexicalBlockModule.FinalRecoginzerStates import FinalRecognizerStates
from TransliterationModule.StringCharTypes import StringCharClasses
from LexicalBlockModule.MinimalFinalRecognizer import FinalRecognizer
from LexicalBlockModule.MinimalFinalRecognizer import StateSwitcher

def LexicalBlock2(lexemes):
    states = FinalRecognizerStates
    symbols = []
    classes = []
    previousLexemClass = lexemes[0][1]

    for lexeme in lexemes:
        FinalRecognizer(symbols, classes, lexeme, states)
        StateSwitcher(lexeme[1], previousLexemClass, states)
        previousLexemClass = lexeme[1]

    resultTokenChain = [("", "")]

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

    del resultTokenChain[0]

    return resultTokenChain