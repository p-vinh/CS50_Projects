from cs50 import get_string


def main():

    text = get_string("Text: ")

    L = count_letters(text) / count_words(text) * 100
    S = count_sentences(text) / count_words(text) * 100

    grade = round(0.0588 * L - 0.29 * S - 15.8)

    if (grade >= 16):
        print("Grade 16+")

    elif (grade < 1):
        print("Before Grade 1")

    else:
        print("Grade", grade)

def count_letters(text):
    letters = 0

    for i in range(len(text)):
        if (text[i].isalpha()):
            letters += 1
    return letters

def count_words(text):
    words = 1

    for i in range(len(text)):
        if (text[i].isspace()):
            words += 1

    return words

def count_sentences(text):
    sentences = 0

    for i in range(len(text)):
        if (text[i] == '.' or text[i] == '?' or text[i] == '!'):
            sentences += 1

    return sentences

if __name__ == "__main__":
    main()