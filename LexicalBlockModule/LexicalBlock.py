from LexicalBlockModule.InputLanguageCharClass import InputLanguageCharClass
from TransliterationModule.StringCharTypes import StringCharClasses

def LexicalBlock(tokenChain):
    resultTokenChain = []  
    previousCharClass = tokenChain[0][1]
    currentToken = ""

    for char in tokenChain: 
        if InputLanguageCharClass.IsPossibleTokenName(char[1], previousCharClass, resultTokenChain, currentToken):
            currentToken += char[0]
        
        elif char[1] != StringCharClasses.space:
             resultTokenChain.append((currentToken, ""))
             currentToken = char[0]

        previousCharClass = char[1]        
        
    resultTokenChain.append((currentToken, ""))

    return resultTokenChain