from spelling_corrector import SpellingCorrector

corrector = SpellingCorrector()

while True:
    user_input = input("\nEnter text (or 'end' to quit): ")
    if user_input.lower() == 'end':
        print("Goodbye!")
        break
    corrected = corrector.correct_text(user_input)
    print(f"Corrected: {corrected}")