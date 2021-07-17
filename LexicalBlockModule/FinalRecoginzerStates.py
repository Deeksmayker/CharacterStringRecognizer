class FinalRecognizerStates:
    currentIndex = 0

    begin = "НАЧ"
    keyWordWhile = "КЛСЛОВО_WHILE"
    space1 = "ПРОБЕЛ1" 
    logicalConst = "ЛОГКОНСТ"   
    space2 = "ПРОБЕЛ2"
    keyWordDo = "КЛСЛОВО_DO"
    space3 = "ПРОБЕЛ3"
    keyWordIf = "КЛСЛОВО_IF"
    space4 = "ПРОБЕЛ4"
    name = "ИМЯ"
    space5 = "ПРОБЕЛ5"
    comparison = "СРАВНЕНИЕ"
    space6 = "ПРОБЕЛ6"
    hexadecimal = "ШЕСНАДЦАТИРИЧНАЯ"
    space7 = "ПРОБЕЛ7"
    keyWordThen = "КЛСЛОВО_THEN"
    space8 = "ПРОБЕЛ8"
    keyWordSubroutineCall = "КЛСЛОВО_ВЫЗОВ_ПОДПРОГРАММЫ"
    space9 = "ПРОБЕЛ9"
    openBracket = "ОТКРЫВАЮЩАЯ СКОБКА"
    space10 = "ПРОБЕЛ10"
    param = "ПАРАМЕТР"
    space11 = "ПРОБЕЛ11"
    comma = "ЗАПЯТАЯ"
    space12 = "ПРОБЕЛ12"    
    space13 = "ПРОБЕЛ13"
    closeBracket = "ЗАКРЫВАЮЩАЯ СКОБКА"
    space14 = "ПРОБЕЛ14"
    semicolon = "ТЧКЗПТ"
    space15 = "ПРОБЕЛ15"
    error = "E"

    states =[begin ,
    keyWordWhile,
    space1 ,
    logicalConst ,
    space2 ,
    keyWordDo ,
    space3 ,
    keyWordIf ,
    space4 ,
    name ,
    space5 ,
    comparison ,
    space6 ,
    hexadecimal ,
    space7 ,
    keyWordThen ,
    space8 ,
    keyWordSubroutineCall,
    space9 ,
    openBracket ,
    space10 ,
    param ,
    space11 ,
    comma,
    space12 ,
    space13 ,
    closeBracket ,
    space14 ,
    semicolon ,
    space15 ,
    error]

    def GetCurrentState():
        return FinalRecognizerStates.states[FinalRecognizerStates.currentIndex]

    def SwitchToNextState():
        FinalRecognizerStates.currentIndex += 1
