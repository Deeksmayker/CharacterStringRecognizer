from TransliterationModule.StringCharTypes import StringCharClasses
from LexicalBlockModule.FinalRecoginzerStates import FinalRecognizerStates
from LexicalBlockModule.InputLanguageCharClass import InputLanguageCharClass
from SyntaxBlockModule.AnalysisResults import AnalysisResults

def FinalRecognizer(symbols, classes, lexeme, states):
    currentState = states.GetCurrentState()
    if lexeme[1] != StringCharClasses.space:
        symbols.append(lexeme[0])

    if lexeme[1] == StringCharClasses.letter:
        if (currentState == FinalRecognizerStates.begin or currentState == FinalRecognizerStates.keyWordWhile
        or currentState == FinalRecognizerStates.space2 or currentState == FinalRecognizerStates.keyWordDo
        or currentState == FinalRecognizerStates.space3 or currentState == FinalRecognizerStates.keyWordIf
        or currentState == FinalRecognizerStates.space4 or currentState == FinalRecognizerStates.name
        or currentState == FinalRecognizerStates.space7 or currentState == FinalRecognizerStates.keyWordThen
        or currentState == FinalRecognizerStates.space8 or currentState == FinalRecognizerStates.keyWordSubroutineCall
        or currentState == FinalRecognizerStates.space10 or currentState == FinalRecognizerStates.param):
            classes.append(InputLanguageCharClass.identifer)

        elif currentState == FinalRecognizerStates.space1 or currentState == FinalRecognizerStates.logicalConst:
            classes.append(InputLanguageCharClass.logical)

        elif currentState == FinalRecognizerStates.hexadecimal and StringCharClasses.IsLetterHexadecimal(lexeme[0]):
            classes.append(InputLanguageCharClass.hexadecimalConstant)

        else:
            AnalysisResults.PrintOnWrongLine()
            


    elif lexeme[1] == StringCharClasses.space:
        if currentState == FinalRecognizerStates.error:
            AnalysisResults.PrintOnWrongLine()

    elif lexeme[1] == StringCharClasses.digital:
        if (currentState == FinalRecognizerStates.name or currentState == FinalRecognizerStates.keyWordSubroutineCall
        or currentState == FinalRecognizerStates.param):
            classes.append(InputLanguageCharClass.identifer)

        elif currentState == FinalRecognizerStates.hexadecimal:
            classes.append(InputLanguageCharClass.hexadecimalConstant)

        else:
            AnalysisResults.PrintOnWrongLine()

    elif lexeme[1] == StringCharClasses.semicolon:
        if currentState == FinalRecognizerStates.closeBracket or currentState == FinalRecognizerStates.space14:
            classes.append(InputLanguageCharClass.semicolon)

        else:
            AnalysisResults.PrintOnWrongLine()

    elif lexeme[1] == StringCharClasses.equal:
        if currentState == FinalRecognizerStates.comparison:
            classes.append(InputLanguageCharClass.comparison)

    elif lexeme[1] == StringCharClasses.openBracket:
        if currentState == FinalRecognizerStates.keyWordSubroutineCall or FinalRecognizerStates.space9:
            classes.append(InputLanguageCharClass.openBracket)

        else:
            AnalysisResults.PrintOnWrongLine()

    elif lexeme[1] == StringCharClasses.closeBracket:
        if currentState == FinalRecognizerStates.param or currentState == FinalRecognizerStates.space13:
            classes.append(InputLanguageCharClass.closeBracket)
        
        else:
            AnalysisResults.PrintOnWrongLine()

    elif lexeme[1] == StringCharClasses.more:
        if currentState == FinalRecognizerStates.space5 or currentState == FinalRecognizerStates.comparison:
            classes.append(InputLanguageCharClass.comparison)

        else:
            AnalysisResults.PrintOnWrongLine()

    elif lexeme[1] == StringCharClasses.less:
        if currentState == FinalRecognizerStates.space5:
            classes.append(InputLanguageCharClass.comparison)

        else:
            AnalysisResults.PrintOnWrongLine()

    elif lexeme[1] == StringCharClasses.hexadecimal:
        if currentState == FinalRecognizerStates.space6:
            classes.append(InputLanguageCharClass.hexadecimalConstant)
        
        else:
            AnalysisResults.PrintOnWrongLine()

    elif lexeme[1] == StringCharClasses.comma:
        if currentState == FinalRecognizerStates.param or currentState == FinalRecognizerStates.space11:
            classes.append(InputLanguageCharClass.comma)

        else:
            AnalysisResults.PrintOnWrongLine()

    else:
        AnalysisResults.PrintOnWrongLine()

    


