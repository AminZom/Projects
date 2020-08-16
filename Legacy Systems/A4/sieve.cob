identification division.
program-id. sieveAlgorithm.
environment division.
input-output section.
file-control.
    select outputFile assign to "cobolOutput.txt"
    organization is line sequential.
data division.
file section.
fd outputFile.
01  outputRecord.
    05 primeNum  pic x(100).
working-storage section.
01  N		         usage unsigned-int.
01  primeIndex       usage unsigned-int.
01  arrayRecord.
   05  num-table pic s9 value 1
		   occurs 1 to 10000000 times depending on N
		   indexed by indexNum.
	   88  checkPrime value 1 false 0.

procedure division.
   display "Enter upper limit: " with no advancing
   accept N
   set checkPrime (1) to false
   perform until N / 2 < primeIndex
	   add 1 to primeIndex
	   perform varying indexNum from primeIndex by 1
		   until checkPrime (indexNum)
	   end-perform
	   move indexNum to primeIndex
	   compute indexNum = primeIndex ** 2
	   perform until N < indexNum
		   set checkPrime (indexNum) to false
		   set indexNum up by primeIndex
	   end-perform
   end-perform
   open output outputFile
   perform varying indexNum from 1 by 1 until N < indexNum
	   if checkPrime (indexNum)
	       move indexNum to primeNum
		   write outputRecord
	   end-if
   end-perform.
   close outputFile.
