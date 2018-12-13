#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/* constants */
#define MAX_SIZE 65536
#define THRESHOLD 0.9


/* Analyze and determine how human-language the msg is */
double readability(char *buf, int size)
{
	/* define confidence */
	double confidence;

	/* THIS IS FOR TESTING PURPOSES ONLY */
	char* test = "cryptography";
	if (strstr(buf, test) != NULL)
	{
		//printf("This is it!\n");
		confidence = 1;
	}
	else
	{
		//printf("%c", buf[1]);
		confidence = 0;
	}

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
	while ( fgets(buf, MAX_SIZE, stdin) != NULL )
	{
		strcat(encrMsg, buf);

	}

	//printf("The string: %s\n", encrMsg); // for debug

	// get size of the STDIN
	size = strlen(encrMsg);

	/*  BRUTE FORCE LOOP */
	for (key = 1; key < 256; key++)
	{
		//printf("Checking key: %d\n", key); // for debug

		/* loop through the characters in the encrypted msg */
		for (i = 0; i < size; i++)
		{
			buf[i] = encrMsg[i]^key;
		}

		/* Check whether the key is correct or not */
		confidence = readability(buf, size);

		if (confidence > THRESHOLD)
		{
			printf("Found key: %d\n", key);
			break;
		}
	}
	//printf("DECRPTED MESSAGE (key: %d):\n\n%s\n", key, buf);

	/* clean after myself */
	free(buf);
	free(encrMsg);

	return 0;
}
