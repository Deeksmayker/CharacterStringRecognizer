#Из папок(это модули) вызывается файл (это блок), оттуда уже импортируются функции
from TransliterationModule.TransliterationBlock import TransliterationBlock
from LexicalBlockModule.LexicalBlock import LexicalBlock
from KeywordIdentificationBlockModule.KeywordIdentificationBlock import KeywordIdentification
from SyntaxBlockModule.SyntaxBlock import SyntaxBlock

#Читаем инпут и создаем оутпут
input = open("INPUT.txt", 'r').read()
output = open("OUTPUT.txt", 'w')

transliteration = TransliterationBlock(input)
lexical = LexicalBlock(transliteration)
keyWords = KeywordIdentification(lexical)
result = SyntaxBlock(keyWords)

#Тут записыавем результат в файл оутпут
output.write(result)

#А это нужно было для дебага
print("Блок транслитерации - ", transliteration, "\n")
print("Лексический блок - ", lexical, "\n")
print("Идентефикация ключевых слов - ", keyWords, "\n")
print("Результат анализа - ", result)
