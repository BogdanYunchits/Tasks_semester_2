def calculate_text_statistics(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    word_count = len(words)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    average_word_length = sum(len(word) for word in words) / word_count if word_count != 0 else 0

    print(f"Word Count: {word_count}")
    print(f"Sentence Count: {sentence_count}")
    print(f"Average Word Length: {average_word_length:.2f}")

calculate_text_statistics("large_text.txt")
