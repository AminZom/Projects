JAVA=java
JAVAC=javac
JFLEX=jflex
CLASSPATH=-classpath /usr/share/java/cup.jar:.
#CUP=$(JAVA) $(CLASSPATH) java_cup.Main
CUP=cup

all: Main.class

Main.class: absyn/*.java parser.java sym.java Lexer.java ShowTreeVisitor.java SemanticVisitor.java Scanner.java Main.java

%.class: %.java
	$(JAVAC) $(CLASSPATH)  $^

Lexer.java: CM.flex
	$(JFLEX) CM.flex

parser.java: CM.cup
	#$(CUP) -dump -expect 3 tiny.cup
	$(CUP) CM.cup

clean:
	rm -f parser.java Lexer.java sym.java *.class absyn/*.class *~
