class AnalysisResults:
    correct = "ACCEPT"
    uncorrect = "REJECT"

    def PrintOnCorrectLine():
        print("Результат анализа - ", AnalysisResults.correct)
        exit(0)

    def PrintOnWrongLine():
        print("Результат анализа - ", AnalysisResults.uncorrect)
        exit(0)