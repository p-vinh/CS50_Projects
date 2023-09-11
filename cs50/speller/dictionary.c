// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
	char word[LENGTH + 1];
	struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 100;

// Hash table
node *table[N];
int sizeOfDict = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
	int hashCode = hash(word);

	node *n = table[hashCode];

	while (n != NULL)
	{
		if (strcasecmp(word, n->word) == 0)
		{
			return true;
		}
		n = n->next;
	}

	return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
	unsigned long hash = 5381;
	int c;

	while ((c = tolower(*word++)))
	{
		hash = ((hash << 5) + hash) + c;
	}
	return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
	FILE *dict = fopen(dictionary, "r");

	if (dict == NULL)
	{
		printf("Dictionary File: %s could not be opened", dictionary);
		return false;
	}

	char nextWord[LENGTH + 1];

	while (fscanf(dict, "%s", nextWord) != EOF)
	{
		node *n = malloc(sizeof(node));

		if (n == NULL)
		{
			return false;
		}

		strcpy(n->word, nextWord);

		unsigned int hash_value = hash(nextWord);

		n->next = table[hash_value];
		table[hash_value] = n;
		sizeOfDict++;
	}

	fclose(dict);

	return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
	return sizeOfDict;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
	for (int i = 0; i < N; i++)
	{
		node *n = table[i];

		while (n != NULL)
		{
			node *temp = n;
			n = n->next;
			free(temp);
		}

		if (n == NULL || i == N - 1)
		{
			return true;
		}
	}
	return false;
}
