#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Gets name input from user
    string name = get_string("What's your name? ");

    // Prints the name
    printf("hello, %s\n", name);
}