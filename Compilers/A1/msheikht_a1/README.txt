**********************************************
Mohammadamin Sheikhtaheri         Jan 30, 2020
0930853

CIS*4650 - Assignment 1
README.txt
**********************************************

**********************
What This Program Does
**********************

This program reads from stdin until EOF is read, and it tokenizes
the input based on pre-determined regular expressions for the SGML
language. These tokens are then sent to stdout, and any errors are
sent to stderr. A global stack is used to organize tags in order to
filter the output properly. In case the stack is not empty by the end
of input, then it is also displayed to stderr.

*************************
Assumptions & Limitations
*************************

  - All text such as "This is a text" must reside within a tag
  - Irrelevant tags such as <BYLINE> cannot have relevant tags such as <TEXT> 
    within them (if they do, the imbedded text within the relevant tags are still
    tokenized.)
  - The "relp" keyword is used to distinguish relevant P tags from irrelevant
    P tags on the stack
  - All errors are outputted to stderr, and all tokens are outputted to stdout
  - Only the first instance of a word in a tag is considered, for example:
  
        <   DOC   TEXT    >
        
    The above will only look at DOC, and consider this a valid open tag for <DOC>
  - Closing tags cannot have attributes (ex. </TEXT align="text">
  - Spaces in the closing tag can be between </ and the tag name, and between the
    tag name and > (ex. </    TEXT     >) NOT <   /   TEXT       >
  - Empty tags cannot exist (ex. <  >)

********************
Building The Program
********************

To build the program, first enter:

    make clean
    
This is to clean up any Lexer.java and .class files that may be present in the directory.
Then enter:

    make
    
This will build the project, creating the specific files required to run.

*******************
Testing The Program
*******************

To test this program, it is highly recommended that a file be used to give input
to the scanner, like below:

    java Scanner < testfile.txt
    
If you wish to have the token output of this program also be to a file, enter:

    java Scanner < testfile.txt > outputfile.txt

Personally, I had many different test files checking how this program handles the
many different conditions such as:

  - Embedded text within irrelevant tags
  - <P> tags in relevant and irrelevant tags
  - Mismatched open and close tags
  - Different types of hyphenated words (ex. father-in-law)
  - Different types of apostrophized words (ex. O'Reily's)
  - Different types of a combination of apostrophized and hyphenated words (father-in-law's)
  - Integers and real numbers with + and - (ex. -24.556)
  
*********************
Possible Improvements
*********************

  - Improve the handling of edge cases such as relevant tags being included in irrelevant tags










