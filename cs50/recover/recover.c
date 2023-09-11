#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BLOCK_SIZE 512
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{

	if (argc != 2)
	{
		printf("Usage: ./recover image\n");
		return 1;
	}
	else
	{
		FILE *file = fopen(argv[1], "r");

		if (file == NULL)
		{
			printf("Error: cannot open %s\n", argv[1]);
			return 2;
		}

		BYTE buffer[BLOCK_SIZE];
		FILE *img = NULL;
		char filename[8];
		int fileCount = 0;

		while (fread(buffer, BLOCK_SIZE, 1, file) == 1)
		{
			if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
			{
				if (!(fileCount == 0))
				{
					fclose(img);
				}
				sprintf(filename, "%03i.jpg", fileCount);
				img = fopen(filename, "w");
				fileCount++;
			}

			if (!(fileCount == 0)) {
				fwrite(buffer, BLOCK_SIZE, 1, img);
			}
		}

		fclose(img);
		fclose(file);
	}

	return 0;
}