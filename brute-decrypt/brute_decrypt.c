#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h> // for tolower() and toupper()

/* constants */
#define MAX_SIZE 65536
#define THRESHOLD 0.9


/* Analyze and determine how human-language the msg is */
double readability(char *buf, int size)
{
	/* declare stuff */
	double confidence;
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

	confidence = ((double) counter) / ((double) size);

	#ifdef DEBUG
	fprintf(stderr, "The counter: %i | The confidence: %f\n", counter, confidence);
	#endif

	return confidence;
}


/* Main function */
int main(void)
{
	/* declare stuff */
	int i, key, size;
	double confidence;

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
	fgets(encrMsg, MAX_SIZE, stdin);

	// get size of the STDIN
	size = strlen(encrMsg);

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

		/* Check whether the key is correct or not */
		confidence = readability(buf, size);

		if (confidence > THRESHOLD)
		{
			fprintf(stderr, "Found key: %d\n", key);
			puts(buf); // print buf
			break;
		}
	}

	/* clean after myself */
	free(buf);
	free(encrMsg);

	return 0;
}
