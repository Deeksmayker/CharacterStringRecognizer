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
    comparison = "ОПЕРАТОР СРАВНЕНИЯ"
    bracket = "СКОБКА"
    hexadecimalConstant = "ШЕСНАДЦАТИРИЧНАЯ КОНСТАНТА"
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
        return (charClass == previousCharClass
        or (tokenArrayLength >= 1 and resultTokenChain[tokenArrayLength - 1][0] == "if" and currentToken[0].isalpha() and charClass == StringCharClasses.digital)
        or ((previousCharClass == StringCharClasses.more or previousCharClass == StringCharClasses.less) and charClass == StringCharClasses.equal)
        or (previousCharClass == StringCharClasses.less and charClass == StringCharClasses.more)
        or (StringCharClasses.RecognizeCharacter(currentToken[0]) == StringCharClasses.hexadecimal
        and charClass != StringCharClasses.space and previousCharClass != StringCharClasses.space)
        or (currentToken[0].isalpha() and charClass == StringCharClasses.digital and charClass != StringCharClasses.space and previousCharClass != StringCharClasses.space))

    def RecognizeLexicalTokenClass(tokenName):
        if StringCharClasses.RecognizeCharacter(tokenName) == StringCharClasses.semicolon: return InputLanguageCharClass.semicolon
        if tokenName == StringCharClasses.equal: return InputLanguageCharClass.equal
        if tokenName == StringCharClasses.sign: return InputLanguageCharClass.sign
        if tokenName.isnumeric(): return InputLanguageCharClass.integer
        if tokenName[0] == '<' or tokenName[0] == '>': return InputLanguageCharClass.comparison
        if tokenName.lower() == "true" or tokenName.lower() == "false": return InputLanguageCharClass.logical
        if tokenName == ')' or tokenName == '(':return InputLanguageCharClass.bracket
        if tokenName[0].isalpha(): return InputLanguageCharClass.identifer
        if StringCharClasses.RecognizeCharacter(tokenName[0]) == StringCharClasses.hexadecimal: return InputLanguageCharClass.hexadecimalConstant


        return InputLanguageCharClass.error

        