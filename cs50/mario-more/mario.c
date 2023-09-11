#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get height from user
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);


    for (int i = 1; i <= height; i++)
    {
        // Indent for left pyramid
        for (int space = 1; space <= height - i; space++)
        {
            printf(" ");
        }
        // Left Half of Pyramid
        for (int j = 1; j <= i; j++)
        {
            printf("#");
        }

        // Space in the middle
        printf("  ");

        // Right Half of Pyramid
        for (int right = 1; right <= i; right++)
        {
            printf("#");
        }
        printf("\n");
    }

}
