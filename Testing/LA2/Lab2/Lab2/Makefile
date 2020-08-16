all: Lab2 runLab

Lab2: include/Calculator.h include/TestCalculator.h src/Calculator.c src/TestCalculator.c src/main.c
	gcc -Wall -std=c99 -Iinclude src/Calculator.c src/TestCalculator.c src/main.c -o bin/lab2

runLab: bin/lab2
	./bin/lab2
