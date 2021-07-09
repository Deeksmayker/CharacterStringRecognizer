from TransliterationModule.StringCharTypes import StringCharClasses

class InputLanguageCharClass:
    identifer = "ИДЕНТЕФИКАТОР"
    begin = "НАЧ"
    keyWord = "КЛСЛОВО"
    name = "ИМЯ"
    equal = "РАВНО"
    sign = "ЗНАК"
    integer = "ЦЕЛОЕ"
    logical = "ЛОГКОНСТ"
    semicolon = "ТЧКЗПТ"
    error = "Е"
    space1 = "ПРОБЕЛ1"
    space2 = "ПРОБЕЛ2"
    space3 = "ПРОБЕЛ3"
    space4 = "ПРОБЕЛ4"
    space51 = "ПРОБЕЛ51"
    space52 = "ПРОБЛЕ52"
    space6 = "ПРОБЕЛ6"

    def IsPossibleTokenName(charClass, previousCharClass, resultTokenChain, currentToken):
        tokenArrayLength = len(resultTokenChain)
        return charClass == previousCharClass or (tokenArrayLength >= 1 and resultTokenChain[tokenArrayLength - 1][0] == "const"
        and currentToken[0].isalpha() and charClass == StringCharClasses.digital)

    def RecognizeLexicalTokenClass(tokenName):
        if tokenName == StringCharClasses.semicolon: return InputLanguageCharClass.semicolon
        if tokenName == StringCharClasses.equal: return InputLanguageCharClass.equal
        if tokenName == StringCharClasses.sign: return InputLanguageCharClass.sign

        