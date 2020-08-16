#!/bin/sh
## Question 1: Short Answer
##
## echo: Displays a line of text/variable to standard output or a file.
## grep: Searches for lines within the given files that match a given pattern list.
## cut: Cuts sections from each line of given files, and writes the result to standard output.
## -d: Specifies the delimiter for the cut command.
## -c: Specifies to the grep command to only display the number of lines the match was found in.
## -f: Checks if the given file name is of type file.
## -f2: Extracts the 2nd field from the line and displays it to standard output

	N_FILES_PROCESSED=0
	N_TOTAL_PASSES=0
	N_TOTAL_FAILS=0

	for filename in "$@"
	do
		N_PASSES_PROCESSED=0
		N_FAILS_PROCESSED=0
		
		if [ -f ${filename} ]
		then
			echo " "
			echo "Working on \033[1;34m${filename}\033[0;0m"
			if
				N_PASSES_PROCESSED=$(grep -w -c PASS ${filename} | cut -d: -f2)
				N_FAILS_PROCESSED=$(grep -w -c FAIL ${filename} | cut -d: -f2)
				N_TOTAL_PASSES=$((N_TOTAL_PASSES + N_PASSES_PROCESSED))
				N_TOTAL_FAILS=$((N_TOTAL_FAILS + N_FAILS_PROCESSED))
			then
				:
			else
				## print a warning to standard error
				echo "warning: search failed" >&2
			fi
			N_FILES_PROCESSED=$((N_FILES_PROCESSED + 1))
			echo "In total, ${N_PASSES_PROCESSED} passes were found."
			echo "In total, ${N_FAILS_PROCESSED} fails were found."
			if [ $((N_FAILS_PROCESSED)) \> 1 ]
			then
				echo "Below are the line numbers of the FAIL(s):"
				awk '$0 ~ /FAIL/{print NR}' ${filename}
			fi
			printf "The score for this file is: "
			echo "${N_PASSES_PROCESSED}*1.25-${N_FAILS_PROCESSED}*1.5" | bc
			if [ $(echo "${N_PASSES_PROCESSED}*1.25-${N_FAILS_PROCESSED}*1.5 >= 0" | bc) -eq 1 ]
			then
				printf "This test file has "
				echo "\033[0;32mPASSED\033[0;0m"
			else
				printf "This test file has "
				echo "\033[0;31mFAILED\033[0;0m"
			fi
		fi
	done

	echo "In total, ${N_FILES_PROCESSED} file(s) were processed"
	printf "The total score of all files is: "
	echo "${N_TOTAL_PASSES}*1.25-${N_TOTAL_FAILS}*1.5" | bc
	if [ $(echo "${N_TOTAL_PASSES}*1.25-${N_TOTAL_FAILS}*1.5 >= 0" | bc) -eq 1 ]
	then
		printf "Overall test has "
		echo "\033[0;32mPASSED\033[0;0m"
	else
		printf "Overall test has "
		echo "\033[0;31mFAILED\033[0;0m"
	fi
	
	
