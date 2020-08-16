all: saw zip

saw: saw.c
	gcc saw.c -o saw
	
clean: saw
	rm saw

zip: saw.c README.txt report.pdf Makefile
	zip cis3210_ass2_msheikht.zip saw.c README.txt report.pdf Makefile
