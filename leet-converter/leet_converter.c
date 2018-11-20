#include <stdio.h>
#include <malloc.h>
#include <string.h>

//g++ leet_converter.c -o leet_converter.exe

// declare functions
void leet(char *s);

// function to convert string to leet (1337)
void leet(char *s)
{
	int i;
	for(i = 0; i < strlen(s); i++) // loop through character
	{
		//printf("[%c]", s[i]); // print each character
		switch(s[i])
		{
			case 'a':
			case 'A':
				s[i] = '4';
				//s[i] = "4"; /// WRONG !!! nonsense!!
				break;
			case 'l':
			case 'L':
				s[i] = '1';
				break;
			case 'e':
			case 'E':
				s[i] = '3';
				break;
			case 't':
			case 'T':
				s[i] = '7';
				break;
		}
	}
}

// main function
int main(int argc, char *argv[])
{
	char *s; // will be the original AND later converted string
	int i; // argument index

	if (argc == 1)
	{
		printf("Missing argument! Gimme at least one argument (a string).\n");
		return 1;
	}

	for(i = 1; i < argc; i++) // i=1 cause i=0 is program name
	{
		s = malloc( strlen(argv[i]) * sizeof(char) ); // allocate for first word
		strcpy(s, argv[i]);

		leet(s); // convert the word
		printf("%s", s); // or just puts(s); // print out leeted
		free(s); // free the allocated space

		if (i == argc-1) // if it's the last word
		{
			printf("\n");
		}
		else
		{
			printf(" ");
		}

	}

	return 0;
}
