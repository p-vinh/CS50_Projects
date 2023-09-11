#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

void checkSum(long credit, int length);
int getNumber(long credit, int index, int offset);
int getLength(long credit);

int main(void)
{
    long credit;

    // Gets input from the user
    do
    {
        credit = get_long("Number: ");
    }
    while (credit < 0);

    // Gets length of the input
    int length = getLength(credit);

    if (length != 13 && length != 15 && length != 16)
    {
        printf("INVALID\n");
        return 0;
    }

    // Checks if the inputted credit is valid
    checkSum(credit, length);

    // Gets the first digit of the card number
    int firstDigits = getNumber(credit, length, 2);

    if (firstDigits / 10 == 4)
    {
        printf("VISA\n");
    }
    else if (firstDigits >= 51 && firstDigits <= 55)
    {
        printf("MASTERCARD\n");
    }
    else if (firstDigits == 34 || firstDigits == 37)
    {
        printf("AMEX\n");
    }
    else
    {
        printf("INVALID\n");
    }

    return 0;
}

int getLength(long credit)
{
    int length = 0;

    // Counting Length
    while (credit > 0)
    {
        credit = credit / 10;
        length++;
    }

    return length;
}

int getNumber(long credit, int index, int offset)
{
    // Retrieves number at the index
    long firstNum = pow(10, index);
    long secondNum = pow(10, index - offset);
    return (credit % firstNum) / secondNum;
}

void checkSum(long credit, int length)
{
    int sum = 0;

    for (int i = 1; i <= length; i++)
    {
        // Second to last number
        if (i % 2 == 0)
        {
            int number = 2 * getNumber(credit, i, 1);
            sum += number < 10 ? number : 1 + (number % 10);
        }
        // Last number
        else
        {
            sum += getNumber(credit, i, 1);
        }
    }

    if (sum % 10 != 0)
    {
        printf("INVALID\n");
        exit(0);
    }
}
