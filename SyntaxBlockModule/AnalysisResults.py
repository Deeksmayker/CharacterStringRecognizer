#Ну тут находятся все возможные результаты анализа. Их может быть и больше чем два, так что по правилу хорошего кода лучше писать отдельные классы и для этого
class AnalysisResults:
    correct = "ACCEPT"
    uncorrect = "REJECT"

    def PrintOnCorrectLine():
        print("Результат анализа - ", AnalysisResults.correct)
        exit(0)

    def PrintOnWrongLine():
        print("Результат анализа - ", AnalysisResults.uncorrect)
        exit(0)