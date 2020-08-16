/*
  File Name: SGML.flex
  JFlex specification for the SGML language
*/
   
import java.util.ArrayList;

%%
   
%class Lexer
%type Token
%line
%column
    
%eofval{
  if(tagStack.size() != 0)  //If the stack is not empty, display it to stderr
  {
     System.err.print("Global stack contents: ");
     System.err.println(tagStack);
  }
  return null;
%eofval};

%{
  private static ArrayList<String> tagStack = new ArrayList<String>();  //Global stack
  private static int getTagName(String name, int checkState)  //Function to retrieve the tag
  {
     if(checkState == 0)
     { 
         if(name.toLowerCase().equals("doc"))
            return Token.OPEN_DOC;
         else if(name.toLowerCase().equals("text"))
            return Token.OPEN_TEXT;
         else if(name.toLowerCase().equals("date"))
            return Token.OPEN_DATE;
         else if(name.toLowerCase().equals("docno"))
            return Token.OPEN_DOCNO;
         else if(name.toLowerCase().equals("headline"))
            return Token.OPEN_HEADLINE;
         else if(name.toLowerCase().equals("length"))
            return Token.OPEN_LENGTH;
         else
            return Token.OPEN_TAG;
     }
     else
     {
         if(name.toLowerCase().equals("doc"))
            return Token.CLOSE_DOC;
         else if(name.toLowerCase().equals("text"))
            return Token.CLOSE_TEXT;
         else if(name.toLowerCase().equals("date"))
            return Token.CLOSE_DATE;
         else if(name.toLowerCase().equals("docno"))
            return Token.CLOSE_DOCNO;
         else if(name.toLowerCase().equals("headline"))
            return Token.CLOSE_HEADLINE;
         else if(name.toLowerCase().equals("length"))
            return Token.CLOSE_LENGTH;
         else
            return Token.CLOSE_TAG;
     }
  }
  private static boolean checkRelevancy(String name)  //Function checks if an inputted string is relevant, and returns a boolean value accordingly.
  {
      if(name.toLowerCase().equals("relp") || name.toLowerCase().equals("doc") || name.toLowerCase().equals("text") || name.toLowerCase().equals("date") || name.toLowerCase().equals("docno") || name.toLowerCase().equals("headline") || name.toLowerCase().equals("length"))
      {
          return true;
      }
      else
          return false;
  }

%};

//Regular expression variable for line terminators
LineTerminator = \r|\n|\r\n

//Regular expression variable for white space characters
WhiteSpace     = {LineTerminator} | [ \t\f]

//Regular expression variable for integers and real numbers, with the possibility of - or +
number = ("-"?|"+"?)[0-9]+("."?[0-9]+)?

//Regular expression variable for words
word = ([0-9]*[a-zA-Z]+[0-9]*)+

//Regular expression variable for hyphenated words
hyphenated = ([a-zA-Z0-9])+("-"([a-zA-Z0-9])+)+

//Regular expression variable for apostrophized words with the possibility of hyphens
apostrophized = ([a-zA-Z])+(("-"([a-zA-Z])+)*"'"([a-zA-Z])+("-"([a-zA-Z])+)*)+
   
%%
   
/*
   This section contains regular expressions and actions, i.e. Java
   code, that will be executed when the scanner matches the associated
   regular expression. */

//Regular expression for all open tags
"<"[^>/]*">"       { String name = yytext();                         //
                     name = name.substring(1);                       //
                     name = name.substring(0, name.length() - 1);    // The yytext() is filtered so that only the name of the open tag is stored
                     name = name.trim();                             // For example: (<   TEXT align="left"   >) becomes TEXT
                     String[] names = name.split(" ");               //
                     name = names[0];                                //
                     if(name.toLowerCase().equals("p"))   //If the open tag is a P tag (<P>)
                     {
                         boolean isTagRelevant = false;
                         for(int i = 0; i < tagStack.size(); i++)   //Checks the stack for any irrelevant tags
                         {
                             isTagRelevant = checkRelevancy(tagStack.get(i));
                             if(isTagRelevant == false)
                                 break;
                         }
                         if(isTagRelevant == true)   //If the stack only consists of relevant tags
                         {
                             tagStack.add("relp");   //Adding "relp" to the stack to distinguish relevant P tags from irrelevant P tags
                             return new Token(Token.OPEN_P, name, yyline, yycolumn);
                         }
                         else
                             tagStack.add("p");   //Adding the irrelevant "p" to the stack if the stack consisted of one or more irrelevant tags
                     }
                     else
                     {
                         tagStack.add(name.toLowerCase());   //If the tag is not a P tag, simply add it to the stack
                         if(checkRelevancy(name))
                             return new Token(getTagName(name, 0), name, yyline, yycolumn); }   //If the tag is relevant, create a token for it
                     }
                     
//Regular expression for all close tags
"</"[^>/]*">"      { String name = yytext();
                     name = name.substring(2);
                     name = name.substring(0, name.length() - 1);    // The yytext() is filtered so that only the name of the close tag is stored
                     name = name.trim();                             // For example: (</   TEXT    >) becomes TEXT
                     if(tagStack.size() == 0)
                         return new Token(Token.ERROR, yytext(), yyline, yycolumn);   //If the close tag is read before an open tag, send an error
                     String top = tagStack.remove(tagStack.size() - 1);
                     if(name.toLowerCase().equals("p"))
                     {
                         if(top.equals("relp"))
                             return new Token(Token.CLOSE_P, name, yyline, yycolumn);
                     }
                     else
                     {
                         if(top.equals(name.toLowerCase()))
                         {
                             if(checkRelevancy(name))
                                 return new Token(getTagName(name, 1), name, yyline, yycolumn);
                         }
                         else
                         {
                             tagStack.add(top);
                             return new Token(Token.ERROR, yytext(), yyline, yycolumn);
                         }
                     }}
//Regular expression for apostrophized words with the possibility of hyphens
{apostrophized}    { if(tagStack.size() == 0)
                         return new Token(Token.ERROR, yytext(), yyline, yycolumn);
                     else if(checkRelevancy(tagStack.get(tagStack.size() - 1)) == true)
                     {
                         return new Token(Token.APOSTROPHIZED, yytext(), yyline, yycolumn);
                     }}
//Regular expression for hyphenated words
{hyphenated}       { if(tagStack.size() == 0)
                         return new Token(Token.ERROR, yytext(), yyline, yycolumn);
                     else if(checkRelevancy(tagStack.get(tagStack.size() - 1)) == true)
                     {
                         return new Token(Token.HYPHENATED, yytext(), yyline, yycolumn);
                     }}
//Regular expression for integers and real numbers, with the possibility of - or +
{number}           { if(tagStack.size() == 0)
                         return new Token(Token.ERROR, yytext(), yyline, yycolumn);
                     else if(checkRelevancy(tagStack.get(tagStack.size() - 1)) == true)
                     {
                         return new Token(Token.NUMBER, yytext(), yyline, yycolumn);
                     }}
//Regular expression for words
{word}             { if(tagStack.size() == 0)
                         return new Token(Token.ERROR, yytext(), yyline, yycolumn);
                     else if(checkRelevancy(tagStack.get(tagStack.size() - 1)) == true)
                     {
                         return new Token(Token.WORD, yytext(), yyline, yycolumn);
                     }}
{WhiteSpace}+      { /* skip whitespace */ }   
"{"[^\}]*"}"       { /* skip comments */ }
.                  { if(tagStack.size() == 0)
                         return new Token(Token.ERROR, yytext(), yyline, yycolumn);
                     else if(checkRelevancy(tagStack.get(tagStack.size() - 1)) == true)
                     {
                         return new Token(Token.PUNCTUATION, yytext(), yyline, yycolumn);
                     }}

