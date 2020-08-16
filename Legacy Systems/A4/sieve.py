#!/usr/bin/env/python3
    
if __name__=='__main__':
	N = input("Enter upper limit: ")	#acquiring the upper limit
	outputFile = open("pythonOutput.txt", "w")
	array = []
	for i in range(N+1):
		array.append(i)		#initializing the prime numbers array
		i += 1
	i = 2
	while (i * i <= N):		#loop iterates from 2 to the square root of the upper limit
		if (array[i] != 0):
			for j in range(i * 2, N+1, i):		#loop sets indeces of array that have numbers which are not prime to 0
				array[j] = 0
		i += 1
		
	for i in range(2, N):
		if (array[i] != 0):
			outputFile.write(str(array[i]) + "\n")		#printing the prime numbers to the file
            
	outputFile.close()
