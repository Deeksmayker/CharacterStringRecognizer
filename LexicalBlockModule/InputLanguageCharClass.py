from TransliterationModule.StringCharTypes import StringCharClasses

class InputLanguageCharClass:
    identifer = "ИДЕНТЕФИКАТОР"
    begin = "НАЧ"
    keyWord = "КЛСЛОВО"
    space1 = "ПРОБЕЛ1"
    name = "ИМЯ"
    space2 = "ПРОБЕЛ2"
    equal = "РАВНО"
    space3 = "ПРОБЕЛ3"
    sign = "ЗНАК"
    space4 = "ПРОБЕЛ4"
    integer = "ЦЕЛОЕ"
    space51 = "ПРОБЕЛ51"
    logical = "ЛОГКОНСТ"
    space52 = "ПРОБЛЕ52"
    semicolon = "ТЧКЗПТ"
    space6 = "ПРОБЕЛ6"
    error = "Е"

    def IsPossibleTokenName(charClass, previousCharClass, resultTokenChain, currentToken):
        tokenArrayLength = len(resultTokenChain)
        return charClass == previousCharClass or (tokenArrayLength >= 1 and resultTokenChain[tokenArrayLength - 1][0] == "const"
        and currentToken[0].isalpha() and charClass == StringCharClasses.digital)

    def RecognizeLexicalTokenClass(tokenName):
        a =3