from os import read
from TransliterationModule.TransliterationBlock import TransliterationBlock
from LexicalBlockModule.LexicalBlock import LexicalBlock

input = open("INPUT.txt", 'r').read()
output = open("OUTPUT.txt", 'w')

transliteration = TransliterationBlock(input)
lexical = LexicalBlock(transliteration)

print("Блок транслитерации - ", transliteration, "\n")
print("Лексический блок - ", lexical)
