from LexicalBlockModule.FinalRecoginzerStates import FinalRecognizerStates
from TransliterationModule.StringCharTypes import StringCharClasses
from LexicalBlockModule.MinimalFinalRecognizer import FinalRecognizer

def LexicalBlock2(lexemes):
    states = FinalRecognizerStates
    symbols = []
    classes = []

    for lexeme in lexemes:
        FinalRecognizer(symbols, classes, lexeme, states)