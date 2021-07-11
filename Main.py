from TransliterationModule.TransliterationBlock import TransliterationBlock
from LexicalBlockModule.LexicalBlock import LexicalBlock
from KeywordIdentificationBlockModule.KeywordIdentificationBlock import KeywordIdentification
from SyntaxBlockModule.SyntaxBlock import SyntaxBlock

input = open("INPUT.txt", 'r').read()
output = open("OUTPUT.txt", 'w')

transliteration = TransliterationBlock(input)
lexical = LexicalBlock(transliteration)
keyWords = KeywordIdentification(lexical)
result = SyntaxBlock(keyWords)

print("Блок транслитерации - ", transliteration, "\n")
print("Лексический блок - ", lexical, "\n")
print("Идентефикация ключевых слов - ", keyWords, "\n")
print("Результат анализа - ", result)
