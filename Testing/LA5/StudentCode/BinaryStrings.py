import os
import sys


class BinaryString:
    # an array of binary strings
    # will be used to hold all the binary strings if length 'n'
    binaryStrings = []

    # a particular binary string of length 'n'
    binaryString = []

    # function to generate all binary strings  of lnegth 'n' and print the ones with
    # 'k' 1s in it.
    def genAllBinStrings(self, n: int, k: int, count: int):

        # if the count equals
        # 'n' then append binaryString to binaryStrings
        # and print binaryString if it has 'k' 1's in it
		if(count == n):
			self.binaryStrings.append(self.binaryString.copy())
			numOnes = 0
			for i in range(0, count):
				if(self.binaryString[i] == '1'):
					numOnes++
			print(numOnes)
			if(numOnes == k):
				print(self.binaryString.copy())
            self.binaryString.clear()
            return

        # else add '0' to the binaryString
        self.binaryString.append('0')

        # incremenet count by '1'
        count += 1

        # recursive call with 
        self.genAllBinStrings(n, k, count)

    # function to genearte all substrings of parameter sting
    # function will call genAllBinStrings with 'n' being the length of string.
    # The function should print only substrings of length 'k' where 'k' is a parameter
    #passed into the function
    def genAllSubStrings(self, k: int, string: str):

        # genearte all binaryStrings of length = len(string)
        self.genAllBinStrings(len(string), k, 0)

        # for each binary string in the list binaryStrings
        for i in range(0, len(self.binaryStrings)):

            ##Get the current binary string in binaryStrings
            binString = self.binaryStrings[i]

            ##the current substring to be generated from binString
            substring = ""

            ##for the len of binString which equals the len of
            ##the parameter string, append to substring string[j]
            for j in range(0, len(binString)):
                substring += string[j]

            
            print(substring)


    ##count the number of ones in binString
    def countOnes(self, binString:list):
        
        count = 0
        ##for the length of binString
        for i in range(0, len(binString)):
            ##if binString[i] is a '1'
            ##then count++
            if binString[i] == '1':
                count += 1
        #return count
        return count
