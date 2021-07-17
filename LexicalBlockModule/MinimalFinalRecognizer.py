from TransliterationModule.StringCharTypes import StringCharClasses
from LexicalBlockModule.FinalRecoginzerStates import FinalRecognizerStates
from LexicalBlockModule.InputLanguageCharClass import InputLanguageCharClass

def FinalRecognizer(symbols, classes, lexeme, states):
    if lexeme[1] == StringCharClasses.letter:
        if (states.GetCurrentState() == FinalRecognizerStates.begin or states.GetCurrentState() == FinalRecognizerStates.keyWordWhile
        or states.GetCurrentState() == FinalRecognizerStates.keyWordDo or states.GetCurrentState() == FinalRecognizerStates.keyWordIf
        or states.GetCurrentState() == FinalRecognizerStates.keyWordThen or states.GetCurrentState() == FinalRecognizerStates.keyWordSubroutineCall
        or states.GetCurrentState() == FinalRecognizerStates.name):

            symbols.append(lexeme[0])
            classes.append(InputLanguageCharClass.identifer)


    elif lexeme[1] == StringCharClasses.space:

    elif lexeme[1] == StringCharClasses.digital:

    elif lexeme[1] == StringCharClasses.semicolon:

    elif lexeme[1] == StringCharClasses.openBracket:

    elif lexeme[1] == StringCharClasses.closeBracket:

    elif lexeme[1] == StringCharClasses.more:

    elif lexeme[1] == StringCharClasses.less:

    elif lexeme[1] == StringCharClasses.hexadecimal:

    elif lexeme[1] == StringCharClasses.comma:

    else:

    states.SwitchToNextState()


