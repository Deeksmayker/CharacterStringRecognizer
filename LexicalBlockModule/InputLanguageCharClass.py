from ..TransliterationModule.StringCharTypes import StringCharClasses

class InputLanguageCharClass:
    identifer = "ИДЕНТЕФИКАТОР"
    equal = "РАВНО"
    integer = "ЦЕЛОЕ"
    semicolon = "тчкзпт"

    def IsPossibleIdentifierName(charClass, previousCharClass, resultTokenChain):
        tokenArrayLength = len(resultTokenChain)
        return charClass == previousCharClass or (tokenArrayLength >= 2 and resultTokenChain[tokenArrayLength - 2][0] == "const"
        and previousCharClass == StringCharClasses.letter and charClass == StringCharClasses.digital)
