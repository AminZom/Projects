JAVAC=javac
JFLEX=jflex
#JFLEX=/home/fsong/jflex/bin/jflex

all: Token.class Lexer.class Scanner.class

%.class: %.java
	$(JAVAC) $^

Lexer.java: SGML.flex
	$(JFLEX) SGML.flex

clean:
	rm -f Lexer.java *.class *~
