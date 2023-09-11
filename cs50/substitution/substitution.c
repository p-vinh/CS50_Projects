#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

char CIPHER[26];

void convertToCipher();

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        // Checks key for correct length
        if (strlen(argv[1]) == 26)
        {
            for (int i = 0; i < strlen(argv[1]); i++)
            {
                // Checks if key does not contain number or illegal characters
                if (!isalpha(argv[1][i]))  // if contain non-alphabet
                {
                    printf("Key must contain only alphabetic characters\n");
                    return 1;
                }
                // Checks for another instance of a character
                for (int j = i + 1; j < strlen(argv[1]); j++)
                {
                    // this might mess up code
                    if (toupper(argv[1][j]) == toupper(argv[1][i]))
                    {
                        printf("Key contains a letter more than once\n");
                        return 1;
                    }
                }
            }

        }
        else
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
    }
    else
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Copies to cipher array from argv
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        CIPHER[i] = argv[1][i];
    }

    convertToCipher();

    return 0;
}

void convertToCipher()
{
    string input = get_string("plaintext: ");

    printf("ciphertext: ");

    for (int i = 0; i < strlen(input); i++)
    {
        // Checks if input is a character, else will just output(, ! ? any other char)
        if (isalpha(input[i]))
        {
            // if input is uppercase converts the key to upper
            if (isupper(input[i]))
            {
                printf("%c", toupper(CIPHER[input[i] - 'A']));
            }
            // if input is lowercase converts the key to lower
            else
            {
                printf("%c", tolower(CIPHER[input[i] - 'a']));
            }
        }
        else
        {
            printf("%c", input[i]);
        }
    }
    printf("\n");
}
