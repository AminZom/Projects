/*
  Created by: Fei Song
  File Name: Main.java
  To Build: 
  After the scanner, tiny.flex, and the parser, tiny.cup, have been created.
    javac Main.java
  
  To Run: 
    java -classpath /usr/share/java/cup.jar:. Main fac.tiny

  where fac.tiny is an test input file for the tiny language.
*/
   
import java.io.*;
import absyn.*;
import java.util.*;
   
class Main {
  
  public static boolean SHOW_TREE = false;
  public static boolean SHOW_TABLE = false;
  static public void main(String argv[]) {    
    /* Start the parser */
    for (String element : argv) {
        if ( element.equals("-a"))
            SHOW_TREE = true;
        else if ( element.equals("-s"))
            SHOW_TABLE = true;
    }
    try {
      parser p = new parser(new Lexer(new FileReader(argv[0])));
      Absyn result = (Absyn)(p.parse().value);      
      if (SHOW_TREE && result != null) {
         System.out.println("The abstract syntax tree is:");
         ShowTreeVisitor visitor = new ShowTreeVisitor();
         result.accept(visitor, 0); 
      }
      if (result != null) {
         if(SHOW_TABLE)
         {
             System.out.println("Here is the symbol table:");
             System.out.println("Entering the global scope:");
         }
         SemanticVisitor visitor = new SemanticVisitor(SHOW_TABLE);
         result.accept(visitor, 0); 
         
         String keyRemoval = "";
         boolean checkRemove = false;
    
         for(String key: visitor.symbolTable.keySet())
         {
            visitor.declarations = visitor.symbolTable.get(key);
            if(visitor.declarations.get(0).level == 0)
            {
              visitor.indent(1);
              if(SHOW_TABLE)
                  System.out.println(visitor.declarations.get(0).name + ": " + visitor.declarations.get(0).type);
              
              if(visitor.declarations.size() <= 1)
              {
                 keyRemoval += key + ",";
                 checkRemove = true;
              }
              else if(visitor.declarations.size() > 1)
              {
                 visitor.declarations.remove(0);
                 visitor.symbolTable.put(key, visitor.declarations);
              }
            }
         }
         if(checkRemove == true)
         {
            keyRemoval = keyRemoval.substring(0, keyRemoval.length() - 1);
            String[] keyRemovalTokenizer = keyRemoval.split(",");
            for(int i = 0; i < keyRemovalTokenizer.length; i++)
               visitor.symbolTable.remove(keyRemovalTokenizer[i]);
         }
         if(SHOW_TABLE)
             System.out.println("Leaving the global scope.");
      }
    } catch (Exception e) {
      /* do cleanup here -- possibly rethrow e */
      e.printStackTrace();
    }
  }
}


