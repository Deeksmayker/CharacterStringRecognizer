from TransliterationModule.StringCharTypes import StringCharClasses

class InputLanguageCharClass:
    identifer = "ИДЕНТИФИКАТОР"
    begin = "НАЧ"
    keyWord = "КЛСЛОВО"
    equal = "РАВНО"
    sign = "ЗНАК"
    integer = "ЦЕЛОЕ"
    logical = "ЛОГКОНСТ"
    semicolon = "ТЧКЗПТ"
    comparison = "ОПЕРАТОР СРАВНЕНИЯ"
    openBracket = "ОТКРЫВАЮЩАЯ СКОБКА"
    closeBracket = "ЗАКРЫВАЮЩАЯ СКОБКА"
    hexadecimalConstant = "ШЕСНАДЦАТИРИЧНАЯ КОНСТАНТА"
    operator = "ОПЕРАТОР"
    comma = "ЗАПЯТАЯ"
    error = "Е"

    #Ну тут проверяется много каких случаев, писал под пивом в 3 ночи, не судите строго
    def IsPossibleTokenName(charClass, previousCharClass, resultTokenChain, currentToken):
        tokenArrayLength = len(resultTokenChain)
        return (charClass == previousCharClass
        or (tokenArrayLength >= 1 and resultTokenChain[tokenArrayLength - 1][0] == "if" and currentToken[0].isalpha() and charClass == StringCharClasses.digital)
        or ((previousCharClass == StringCharClasses.more or previousCharClass == StringCharClasses.less) and charClass == StringCharClasses.equal)
        or (previousCharClass == StringCharClasses.less and charClass == StringCharClasses.more)
        or (StringCharClasses.RecognizeCharacter(currentToken[0]) == StringCharClasses.hexadecimal
        and charClass != StringCharClasses.space and previousCharClass != StringCharClasses.space)
        or (currentToken[0].isalpha() and charClass == StringCharClasses.digital and charClass != StringCharClasses.space and previousCharClass != StringCharClasses.space))
        

    #Ну тут всё просто, по большей части проверяем одиночные символы чтобы вывалить им классы. С помощью isnureric можем понять является ли это числом.
    #В конце если первый символ это буква(isalpha проверяет буква ли это) то ставим возвращем идентификатор, который потом уже будем превращать в ключевое слово
    #Если ничего не подходит то вываливаем ошибку
    def RecognizeLexicalTokenClass(tokenName):
        if StringCharClasses.RecognizeCharacter(tokenName) == StringCharClasses.semicolon: return InputLanguageCharClass.semicolon
        if tokenName == StringCharClasses.equal: return InputLanguageCharClass.equal
        if tokenName == StringCharClasses.sign: return InputLanguageCharClass.sign
        if tokenName.isnumeric(): return InputLanguageCharClass.integer
        if tokenName[0] == '<' or tokenName[0] == '>': return InputLanguageCharClass.comparison
        if tokenName.lower() == "true" or tokenName.lower() == "false": return InputLanguageCharClass.logical
        if tokenName == '(': return InputLanguageCharClass.openBracket
        if tokenName == ')': return InputLanguageCharClass.closeBracket
        if StringCharClasses.RecognizeCharacter(tokenName[0]) == StringCharClasses.hexadecimal: return InputLanguageCharClass.hexadecimalConstant
        if tokenName == ',': return InputLanguageCharClass.comma
        if tokenName[0].isalpha(): return InputLanguageCharClass.identifer

        return InputLanguageCharClass.error

        