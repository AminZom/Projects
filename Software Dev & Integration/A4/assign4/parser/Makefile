UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S), Darwin)
	LIB := dynamicLib.dylib
else ifeq ($(UNAME_S), Linux)
	LIB := dynamicLib.so
endif
all: dynamicLib.o $(LIB)

$(LIB): dynamicLib.o
	gcc -shared -o ../$(LIB) GEDCOMparser.o GEDCOMutilities.o LinkedListAPI.o

dynamicLib.o: src/GEDCOMparser.c src/LinkedListAPI.c src/GEDCOMutilities.c
	gcc -Wall -std=c11 -Iinclude -c -fpic src/GEDCOMparser.c src/GEDCOMutilities.c src/LinkedListAPI.c -g

clean:
	rm ../$(LIB) *.o
