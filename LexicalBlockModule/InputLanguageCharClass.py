from TransliterationModule.StringCharTypes import StringCharClasses

class InputLanguageCharClass:
    identifer = "ИДЕНТИФИКАТОР"
    begin = "НАЧ"
    logical = "ЛОГКОНСТ"
    semicolon = "ТЧКЗПТ"
    comparison = "ОПЕРАТОР СРАВНЕНИЯ"
    openBracket = "ОТКРЫВАЮЩАЯ СКОБКА"
    closeBracket = "ЗАКРЫВАЮЩАЯ СКОБКА"
    hexadecimalConstant = "ШЕСНАДЦАТИРИЧНАЯ КОНСТАНТА"
    comma = "ЗАПЯТАЯ"
    error = "Е"

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
        if tokenName[0] == '<' or tokenName[0] == '>': return InputLanguageCharClass.comparison
        if tokenName.lower() == "true" or tokenName.lower() == "false": return InputLanguageCharClass.logical
        if tokenName == '(': return InputLanguageCharClass.openBracket
        if tokenName == ')': return InputLanguageCharClass.closeBracket
        if StringCharClasses.RecognizeCharacter(tokenName[0]) == StringCharClasses.hexadecimal: return InputLanguageCharClass.hexadecimalConstant
        if tokenName == ',': return InputLanguageCharClass.comma
        if tokenName[0].isalpha(): return InputLanguageCharClass.identifer

        return InputLanguageCharClass.error

        