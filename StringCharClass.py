class StringCharClass:
    letter = "буква"
    space = "пробел"
    equal = "равно"
    digital = "цифра"
    semicolon = "тчкзпт"

    def RecognizeCharacter(self, char):
        stringChar = StringCharClass()
        return {
            char == ' ': stringChar.space,
            char == ';': stringChar.semicolon,
            char == '=': stringChar.equal,
            char.isalpha(): stringChar.letter,
            char.isnumeric(): stringChar.digital
        }