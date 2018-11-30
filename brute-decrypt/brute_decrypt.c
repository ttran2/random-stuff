#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/* constants */
#define CLEAR(x) memset(x,'\0',1000)
#define MAX_SIZE 65536
#define THRESHOLD 0.9


/* Analyze and determine how human-language the msg is */
int readability(char *buf)
{
	/* define confidence */
	int confidence;

	/* THIS IS FOR TESTING PURPOSES ONLY */
	char* test = "cryptography";
	if (strstr(buf, test) != NULL)
	{
		printf("This is it!");
		confidence = 1;
	}
	else
	{
		printf("%c", buf[1]);
		confidence = 0;
	}

	return confidence;
}


/* Main function */
int main(void)
{
	/* define and declare stuff */
	char *buf = malloc(MAX_SIZE * sizeof(char) + 1); // buffer
	char *encrMsg = malloc(MAX_SIZE * sizeof(char) + 1); // encrypted msg
	char *charBuf = malloc(sizeof(char) + 1); // buffer for single character
	int i, key, confidence;

	/* charBuf will contain be like: [a character],[\0] */
	charBuf[1] = '\0';

	/* check if buffer was allocated successfully */
	if (buf == NULL)
	{
		fprintf(stderr, "FATAL: Not enough memory.\n");
		return 1;
	}

	/* store STDIN into "encMsg" through a buffer */
	while ( fgets(buf, MAX_SIZE, stdin) != NULL )
	{
		strcat(encrMsg, buf);

	}

	/* clean after myself */
	CLEAR(buf);
	//free(buf);

	//printf("The string: %s\n", encrMsg); // for debug

	/*  BRUTE FORCE LOOP */
	for (key = 1; key < 256; key++)
	{
		//printf("Checking key: %d\n", key); // for debug

		/* loop through the characters in the encrypted msg */
		for (i = 0; i < strlen(encrMsg); i++)
		{
			charBuf[0] = encrMsg[i]^key;
			strcat(buf, charBuf);
		}

		/* Check whether the key is correct or not */
		confidence = readability(buf);
		
		if (confidence > THRESHOLD)
		{
			printf("Found key: %d\n", key);
			break;
		}
	}
	//printf("DECRPTED MESSAGE (key: %d):\n\n%s\n", key, buf);

	/* clean after myself */
	//free(buf);
	//free(encrMsg);
	//free(charBuf);
}