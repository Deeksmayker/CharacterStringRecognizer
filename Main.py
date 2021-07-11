from os import read
from TransliterationModule.TransliterationBlock import TransliterationBlock
from LexicalBlockModule.LexicalBlock import LexicalBlock
from KeywordIdentificationBlockModule.KeywordIdentificationBlock import KeywordIdentification

input = open("INPUT.txt", 'r').read()
output = open("OUTPUT.txt", 'w')

transliteration = TransliterationBlock(input)
lexical = LexicalBlock(transliteration)
keyWords = KeywordIdentification(lexical)

print("Блок транслитерации - ", transliteration, "\n")
print("Лексический блок - ", lexical, "\n")
print("Идентефикация ключевых слов - ", keyWords, "\n")
