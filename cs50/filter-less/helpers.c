#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width; j++)
		{
			int avg = round(((float)image[i][j].rgbtRed + (float)image[i][j].rgbtBlue + (float)image[i][j].rgbtGreen) / 3.0);
			image[i][j].rgbtRed = image[i][j].rgbtBlue = image[i][j].rgbtGreen = avg;
		}
	}
	return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width; j++)
		{
			int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
			int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
			int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

			image[i][j].rgbtRed = (sepiaRed > 255) ? 255 : sepiaRed;
			image[i][j].rgbtGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;
			image[i][j].rgbtBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;
		}
	}
	return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < (width / 2); j++)
		{
			RGBTRIPLE temp = image[i][j];

            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = temp;
		}
	}
	return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
	RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float sumBlue = 0;
            float sumGreen = 0;
            float sumRed = 0;
            float counter = 0;

            for (int r = -1; r < 2; r++)
            {
                for (int c = -1; c < 2; c++)
                {
                    if (i + r < 0 || i + r > height - 1)
                    {
                        continue;
                    }

                    if (j + c < 0 || j + c > width - 1)
                    {
                        continue;
                    }

                    sumBlue += image[i + r][j + c].rgbtBlue;
                    sumGreen += image[i + r][j + c].rgbtGreen;
                    sumRed += image[i + r][j + c].rgbtRed;
                    counter++;
                }
            }

            copy[i][j].rgbtBlue = round(sumBlue / counter);
            copy[i][j].rgbtGreen = round(sumGreen / counter);
            copy[i][j].rgbtRed = round(sumRed / counter);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtBlue = copy[i][j].rgbtBlue;
            image[i][j].rgbtGreen = copy[i][j].rgbtGreen;
            image[i][j].rgbtRed = copy[i][j].rgbtRed;
        }

    }
	return;
}
