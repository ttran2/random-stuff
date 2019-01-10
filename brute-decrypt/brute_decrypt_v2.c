#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h> // for tolower() and toupper()

/* constants */
#define MAX_SIZE 65536


/* declare a structure (basically downgraded object) */
typedef struct { // 'struct' is the KEYWORD (not custom)
	int key;
	int validChar;
} best_t;

/* Returns number of 'valid' characters (a-z and space) */
int validChar(char *buf, int size)
{
	/* declare stuff */
	int i, counter;

	/* count integer */
	counter = 0;
	for (i = 0; i < size; i++)
	{
		if ( tolower(buf[i]) >= 'a' &&  tolower(buf[i]) <= 'z')
		{
			counter++;
		}
		if ( buf[i] == ' ')
		{
			counter++;
		}
	}

	#ifdef DEBUG
	fprintf(stderr, "The counter: %i\n", counter);
	#endif

	return counter;
}

/* Main function */
int main(void)
{
	/* declare stuff */
	int i, key, size;

	/* allocate memory for a buffer 'buf' */
	char *buf = malloc((MAX_SIZE + 1) * sizeof(char)); // buffer

	/* check if buffer was allocated successfully */
	if (buf == NULL)
	{
		fprintf(stderr, "FATAL: Failed to allocate memory for 'encrMsg' :(\n");
		return 1;
	}

	/* allocate memory for 'encrMsg' */
	char *encrMsg = malloc((MAX_SIZE + 1) * sizeof(char));

	/* check encrMsg allocation */
	if (encrMsg == NULL)
	{
		fprintf(stderr, "FATAL: Failed to allocate memory for 'encrMsg' :(\n");
		free(buf);
		return 1;
	}

	/* store STDIN into "encMsg" through a buffer */
	size = fread(encrMsg, 1, MAX_SIZE, stdin);
	#ifdef DEBUG
	fprintf(stderr, "Read: %i bytes\n", size);
	#endif
	//encrMsg[++size] = 0; // add 0 (aka '\0') at the end of the string

	/* declare stuff for the brute force loop */
	best_t best;
	int numOfChar;

	/* nullify 'best' */
	best.key = 0;
	best.validChar = 0;

	/*  BRUTE FORCE LOOP */
	for (key = 1; key < 256; key++)
	{
		#ifdef DEBUG
		fprintf(stderr, "Checking key: %d | ", key);
		#endif

		/* loop through the characters in the encrypted msg */
		for (i = 0; i < size; i++)
		{
			buf[i] = encrMsg[i]^key;
		}

		/* get the number of 'valid' characters */
		numOfChar = validChar(buf, size);

		if (best.validChar < numOfChar)
		{
			best.validChar = numOfChar;
			best.key = key;
		}
	}

	/* print out the results */
	fprintf(stderr, "Best key: %d (%d 'valid' characters)\n", best.key, best.validChar);

	/* print out decrypted msg*/
	for (i = 0; i < size; i++)
	{
		putchar(encrMsg[i]^best.key);
	}

	/* clean after myself */
	free(buf);
	free(encrMsg);

	return 0;
}
