#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

void sieveAlgorithm(int N);

int main()
{
	char input[200] = "";
	int N = 0;	//the inputted upper limit
	while(N == 0)
	{
		printf("Enter upper limit: ");
		scanf("%s", input);
		N = atoi(input);
		if(N == 0)
			printf("Incorrect number! Try again.\n");
	}
	sieveAlgorithm(N);
	return 0;
}

void sieveAlgorithm(int N)
{
	FILE* outputFile = fopen("cOutput.txt.txt", "w");	//the output file for the prime numbers
	int array[N + 1];
	for(int i = 0; i < N; i++)
		array[i] = i;
	
	for(int i = 2; i * i <= N; i++)	//iterating from 2 to the square root of the upper limit
	{
		if(array[i] != 0)
		{
			for(int j = i * 2; j <= N; j += i)	//loop iterates and sets the non-primes to 0
			{
				array[j] = 0;
			}
		}
	}
	for(int i = 2; i < N; i++)	//loop prints the primes to the file
	{
		if(array[i] != 0)
			fprintf(outputFile, "%d\n", array[i]);
	}
	fclose(outputFile);
}
