CC = gcc

all: tcpserver tcpclient udpserver udpclient 

tcpserver: tcpserver.c
	$(CC) -o tcpserver tcpserver.c

tcpclient: tcpclient.c
	$(CC) -o tcpclient tcpclient.c

udpserver: udpserver.c
	$(CC) -o udpserver udpserver.c

udpclient: udpclient.c
	$(CC) -o udpclient udpclient.c

clean:
	rm -f *.o tcpserver udpserver tcpclient udpclient

