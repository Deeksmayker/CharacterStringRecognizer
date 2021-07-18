from TransliterationModule.TransliterationBlock import TransliterationBlock
from LexicalBlockModule.LexicalBlock2 import LexicalBlock2
from KeywordIdentificationBlockModule.KeywordIdentificationBlock import KeywordIdentification
from SyntaxBlockModule.SyntaxBlock import SyntaxBlock
from SyntaxBlockModule.AnalysisResults import AnalysisResults

input = open("INPUT.txt", 'r').read()
output = open("OUTPUT.txt", 'w')

transliteration = TransliterationBlock(input)
lexical = LexicalBlock2(transliteration)
keyWords = KeywordIdentification(lexical)
result = SyntaxBlock(keyWords)

output.write(result)

print("Блок транслитерации - ", transliteration, "\n ")
print("Лексический блок - ", lexical, "\n")
print("Идентефикация ключевых слов - ", keyWords, "\n")
AnalysisResults.PrintOnCorrectLine()