#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    // Calculates Grade with formula. Uses the functions to get letters, words, and sentences
    int grade = round(0.0588 * (((float)count_letters(text) / (float)count_words(text)) * 100.0) - 0.296 * (((float)count_sentences(
                          text) / (float)count_words(text)) * 100.0) - 15.8);

    // Checks the grade
    if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }

    return 0;
}

int count_letters(string text)
{
    int letters = 0;

    // Counts the number of letters
    for (int i = 0; i < strlen(text); i++)
    {
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            letters++;
        }
    }

    return letters;
}

int count_words(string text)
{
    // Assumpation: will contain at least one word
    // will not start or end with a space
    // will not have multiple spaces in a row
    int words = 1;

    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == ' ')
        {
            words++;
        }
    }

    return words;
}

int count_sentences(string text)
{
    int sentences = 0;

    // Counts the number of sentences
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }

    return sentences;
}