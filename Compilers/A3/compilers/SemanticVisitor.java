import absyn.*;
import java.util.*;

public class SemanticVisitor implements AbsynVisitor {

  final static int SPACES = 4;
  public ArrayList<Entry> declarations = new ArrayList<Entry>();
  public HashMap <String, ArrayList<Entry>> symbolTable = new HashMap<>();
  public String lastFunc = null;
  public boolean showTable = false;
  
  public SemanticVisitor(boolean SHOW_TABLE)
  {
      this.showTable = SHOW_TABLE;
  }
  

  public String checkOp( OpExp exp )
  {
    String leftType = null;
    String rightType = null;
    
    if(exp.left instanceof OpExp)
        leftType = checkOp((OpExp) exp.left);
    else if(exp.left instanceof VarExp)
    {
        VarExp leftSide = (VarExp) exp.left;
        if(leftSide.variable instanceof SimpleVar)
        {
            SimpleVar expLeftVar = (SimpleVar) leftSide.variable;
            declarations = symbolTable.get(expLeftVar.name);
            if(declarations == null)
                return null;
            leftType = declarations.get(0).type;
        }
        else if(leftSide.variable instanceof IndexVar)
        {
            IndexVar expLeftVar = (IndexVar) leftSide.variable;
            declarations = symbolTable.get(expLeftVar.name);
            if(declarations == null)
                return null;
            leftType = declarations.get(0).type;
        }
    }
    else if(exp.left instanceof IntExp)
    {
        leftType = "int";
    }
    else if(exp.left instanceof CallExp)
    {
        CallExp expLeftVar = (CallExp) exp.left;
        if(symbolTable.get(expLeftVar.func) == null)
            return null;
        FunctionDec function = (FunctionDec) symbolTable.get(expLeftVar.func).get(0).dec;
        leftType = function.type;
    }

    if(exp.right instanceof OpExp)
        rightType = checkOp((OpExp) exp.right);
    else if(exp.right instanceof VarExp)
    {
        VarExp rightSide = (VarExp) exp.right;
        if(rightSide.variable instanceof SimpleVar)
        {
            SimpleVar expRightVar = (SimpleVar) rightSide.variable;
            declarations = symbolTable.get(expRightVar.name);
            if(declarations == null)
                return null;
            rightType = declarations.get(0).type;
        }
        else if(rightSide.variable instanceof IndexVar)
        {
            IndexVar expRightVar = (IndexVar) rightSide.variable;
            declarations = symbolTable.get(expRightVar.name);
            if(declarations == null)
                return null;
            rightType = declarations.get(0).type;
        }
    }
    else if(exp.right instanceof IntExp)
    {
        rightType = "int";
    }
    else if(exp.right instanceof CallExp)
    {
        CallExp expRightVar = (CallExp) exp.right;
        if(symbolTable.get(expRightVar.func) == null)
            return null;
        FunctionDec function = (FunctionDec) symbolTable.get(expRightVar.func).get(0).dec;
        rightType = function.type;
    }
    
    if(leftType.equals("MISMATCH") || rightType.equals("MISMATCH"))
        return leftType;
        
    if(!leftType.equals(rightType))
        return "MISMATCH";
    
    return rightType;
  }
  
  public void indent( int level ) {
    if(showTable)
        for( int i = 0; i < level * SPACES; i++ ) System.out.print( " " );
  }

  public void visit( ExpList expList, int level ) {
    while( expList != null ) {
      if (expList.head != null ) 
        expList.head.accept( this, level );
      expList = expList.tail;
    } 
  }
  
  public void visit( DecList expList, int level ) {
    while( expList != null ) {
      if (expList.head != null ) 
        expList.head.accept( this, level );
      expList = expList.tail;
    } 
  }
  
  public void visit( VarDecList expList, int level ) {
    while( expList != null ) {
      if (expList.head != null ) 
        expList.head.accept( this, level );
      expList = expList.tail;
    } 
  }

  public void visit( AssignExp exp, int level ) {
    exp.lhs.accept( this, level );
    exp.rhs.accept( this, level );
    
    String leftType = "";
    String rightType = "";
    
    if(exp.lhs instanceof SimpleVar)
    {
        SimpleVar leftSide = (SimpleVar) exp.lhs;
        if(symbolTable.get(leftSide.name) == null)
        {
            return;
        }
        leftType = symbolTable.get(leftSide.name).get(0).type;
    }
    else if(exp.lhs instanceof IndexVar)
    {
        IndexVar leftSide = (IndexVar) exp.lhs;
        if(symbolTable.get(leftSide.name) == null)
        {
            return;
        }
        leftType = symbolTable.get(leftSide.name).get(0).type;
    }
    
    if(exp.rhs instanceof OpExp)
    {
        OpExp rightSide = (OpExp) exp.rhs;
        rightType = checkOp(rightSide);
    }
    else if(exp.rhs instanceof VarExp)
    {
        VarExp rightSide = (VarExp) exp.rhs;
        if(rightSide.variable instanceof SimpleVar)
        {
            SimpleVar rightSideVar = (SimpleVar) rightSide.variable;
            if(symbolTable.get(rightSideVar.name) == null)
            {
                return;
            }
            rightType = symbolTable.get(rightSideVar.name).get(0).type;
        }
        else if(rightSide.variable instanceof IndexVar)
        {
            IndexVar rightSideVar = (IndexVar) rightSide.variable;
            if(symbolTable.get(rightSideVar.name) == null)
            {
                return;
            }
            rightType = symbolTable.get(rightSideVar.name).get(0).type;
        }
    }
    else if(exp.rhs instanceof IntExp)
    {
        rightType = "int";
    }
    else if(exp.rhs instanceof CallExp)
    {
        CallExp expExp = (CallExp) exp.rhs;
        if(symbolTable.get(expExp.func) == null)
            return;
        FunctionDec function = (FunctionDec) symbolTable.get(expExp.func).get(0).dec;
        rightType = function.type;
    }
    if(leftType != rightType)
    {
        System.err.println("\u001B[31mERROR\u001B[0m: Assignment type mismatch in line " + (exp.row + 1) + ", column " + exp.col + ".");
        return;
    }
  }

  public void visit( IfExp exp, int level ) {
    //level++;
    indent(level+1);
    if(showTable) 
        System.out.println("Entering a new IF block:");
    
    if(exp.test instanceof VarExp)
    {
        VarExp testVar = (VarExp) exp.test;
        if(testVar.variable instanceof SimpleVar)
        {
            SimpleVar test = (SimpleVar) testVar.variable;
            if(symbolTable.get(test.name) == null)
                return;
            else if(!symbolTable.get(test.name).get(0).type.equals("int"))
            {
                System.err.println("\u001B[31mERROR\u001B[0m: Test condition for if statement is not an int, in line " + (exp.row + 1) + ", column " + exp.col + ".");
            }
        }
        else if(testVar.variable instanceof IndexVar)
        {
            IndexVar test = (IndexVar) testVar.variable;
            if(symbolTable.get(test.name) == null)
                return;
            else if(!symbolTable.get(test.name).get(0).type.equals("int"))
            {
                System.err.println("\u001B[31mERROR\u001B[0m: Test condition for if statement is not an int, in line " + (exp.row + 1) + ", column " + exp.col + ".");
            }
        }
    }
    else if(exp.test instanceof OpExp)
    {
        OpExp test = (OpExp) exp.test;
        String expType = checkOp(test);
        if(expType != null && !expType.equals("int"))
        {
            System.err.println("\u001B[31mERROR\u001B[0m: Test condition for if statement is not an int, in line " + (exp.row + 1) + ", column " + exp.col + ".");
        }
    }
    else if(exp.test instanceof CallExp)
    {
        CallExp test = (CallExp) exp.test;
        if(symbolTable.get(test.func) == null)
            return;
        FunctionDec function = (FunctionDec) symbolTable.get(test.func).get(0).dec;
        if(!function.type.equals("int"))
        {
            System.err.println("\u001B[31mERROR\u001B[0m: Test condition for if statement is not an int, in line " + (exp.row + 1) + ", column " + exp.col + ".");
        }
    }
    
    exp.test.accept( this, level );
    exp.thenpart.accept( this, level );
    if (exp.elsepart != null )
       exp.elsepart.accept( this, level );
       
    String keyRemoval = "";
    boolean checkRemove = false;
    
    for(String key: symbolTable.keySet())
    {
       declarations = symbolTable.get(key);
       if(declarations.get(0).level == level+1)
       {
         indent(level+2);
         if(showTable) 
             System.out.println(declarations.get(0).name + ": " + declarations.get(0).type);
         
         if(declarations.size() <= 1)
         {
            keyRemoval += key + ",";
            checkRemove = true;
         }
         else if(declarations.size() > 1)
         {
            declarations.remove(0);
            symbolTable.put(key, declarations);
         }
       }
    }
    if(checkRemove == true)
    {
       keyRemoval = keyRemoval.substring(0, keyRemoval.length() - 1);
       String[] keyRemovalTokenizer = keyRemoval.split(",");
       for(int i = 0; i < keyRemovalTokenizer.length; i++)
          symbolTable.remove(keyRemovalTokenizer[i]);
    }
    indent(level+1);
    if(showTable) 
        System.out.println("Leaving the IF block.");
    level--;
  }

  public void visit( OpExp exp, int level ) {
    exp.left.accept( this, level );
    exp.right.accept( this, level );
    String expType = null;
    
    expType = checkOp(exp);
    if(expType != null && expType.equals("MISMATCH"))
        System.err.println("\u001B[31mERROR\u001B[0m: Operation type mismatch in line " + (exp.row + 1) + ", column " + exp.col + ".");
  }

  public void visit( VarExp exp, int level ) {
    if (exp.variable != null )
      exp.variable.accept( this, level );
    //IMPORTANT
  }
  
  public void visit( ReturnExp exp, int level ) {
    if (exp.exp != null )
      exp.exp.accept( this, level );
    
    if(exp.exp instanceof IntExp)
    {
        if(!lastFunc.equals("int"))
        {
            System.err.println("\u001B[31mERROR\u001B[0m: Function return type mismatch in line " + (exp.row + 1) + ", column " + exp.col + ".");
        }
    }
    else if(exp.exp == null)
    {
        if(!lastFunc.equals("void"))
        {
            System.err.println("\u001B[31mERROR\u001B[0m: Function return type mismatch in line " + (exp.row + 1) + ", column " + exp.col + ".");
        }
    }
    else if(exp.exp instanceof VarExp)
    {
        VarExp expExp = (VarExp) exp.exp;
        if(expExp.variable instanceof SimpleVar)
        {
            SimpleVar expVar = (SimpleVar) expExp.variable;
            if(symbolTable.get(expVar.name) == null)
                return;
            else if(!symbolTable.get(expVar.name).get(0).type.equals(lastFunc))
            {
                System.err.println("\u001B[31mERROR\u001B[0m: Function return type mismatch in line " + (exp.row + 1) + ", column " + exp.col + ".");
            }
        }
        else if(expExp.variable instanceof IndexVar)
        {
            IndexVar expVar = (IndexVar) expExp.variable;
            if(symbolTable.get(expVar.name) == null)
                return;
            else if(!symbolTable.get(expVar.name).get(0).type.equals(lastFunc))
            {
                System.err.println("\u001B[31mERROR\u001B[0m: Function return type mismatch in line " + (exp.row + 1) + ", column " + exp.col + ".");
            }
        }
    }
    else if(exp.exp instanceof CallExp)
    {
        CallExp expExp = (CallExp) exp.exp;
        if(symbolTable.get(expExp.func) == null)
            return;
        FunctionDec function = (FunctionDec) symbolTable.get(expExp.func).get(0).dec;
        if(!function.type.equals(lastFunc))
        {
            System.err.println("\u001B[31mERROR\u001B[0m: Function return type mismatch in line " + (exp.row + 1) + ", column " + exp.col + ".");
        }
    }
    else if(exp.exp instanceof OpExp)
    {
        OpExp expExp = (OpExp) exp.exp;
        String expType = checkOp(expExp);
        if(expType != null && !expType.equals(lastFunc))
            System.err.println("\u001B[31mERROR\u001B[0m: Function return type mismatch in line " + (exp.row + 1) + ", column " + exp.col + ".");
    }
  }
  
  public void visit( WhileExp exp, int level ) {
    //level++;
    indent(level+1);
    if(showTable) 
        System.out.println("Entering a new WHILE block:");
    
    if(exp.test instanceof VarExp)
    {
        VarExp testVar = (VarExp) exp.test;
        if(testVar.variable instanceof SimpleVar)
        {
            SimpleVar test = (SimpleVar) testVar.variable;
            if(symbolTable.get(test.name) == null)
                return;
            else if(!symbolTable.get(test.name).get(0).type.equals("int"))
            {
                System.err.println("\u001B[31mERROR\u001B[0m: Test condition for while statement is not an int, in line " + (exp.row + 1) + ", column " + exp.col + ".");
            }
        }
        else if(testVar.variable instanceof IndexVar)
        {
            IndexVar test = (IndexVar) testVar.variable;
            if(symbolTable.get(test.name) == null)
                return;
            else if(!symbolTable.get(test.name).get(0).type.equals("int"))
            {
                System.err.println("\u001B[31mERROR\u001B[0m: Test condition for while statement is not an int, in line " + (exp.row + 1) + ", column " + exp.col + ".");
            }
        }
    }
    else if(exp.test instanceof OpExp)
    {
        OpExp test = (OpExp) exp.test;
        String expType = checkOp(test);
        if(expType != null && !expType.equals("int"))
        {
            System.err.println("\u001B[31mERROR\u001B[0m: Test condition for while statement is not an int, in line " + (exp.row + 1) + ", column " + exp.col + ".");
        }
    }
    else if(exp.test instanceof CallExp)
    {
        CallExp test = (CallExp) exp.test;
        if(symbolTable.get(test.func) == null)
            return;
        FunctionDec function = (FunctionDec) symbolTable.get(test.func).get(0).dec;
        if(!function.type.equals("int"))
        {
            System.err.println("\u001B[31mERROR\u001B[0m: Test condition for while statement is not an int, in line " + (exp.row + 1) + ", column " + exp.col + ".");
        }
    }
    
    if (exp.body != null )
      exp.body.accept( this, level );
    if (exp.test != null )
      exp.test.accept( this, level );
      
    String keyRemoval = "";
    boolean checkRemove = false;
    
    for(String key: symbolTable.keySet())
    {
       declarations = symbolTable.get(key);
       if(declarations.get(0).level == level+1)
       {
         indent(level+2);
         if(showTable) 
             System.out.println(declarations.get(0).name + ": " + declarations.get(0).type);
         
         if(declarations.size() <= 1)
         {
            keyRemoval += key + ",";
            checkRemove = true;
         }
         else if(declarations.size() > 1)
         {
            declarations.remove(0);
            symbolTable.put(key, declarations);
         }
       }
    }
    if(checkRemove == true)
    {
       keyRemoval = keyRemoval.substring(0, keyRemoval.length() - 1);
       String[] keyRemovalTokenizer = keyRemoval.split(",");
       for(int i = 0; i < keyRemovalTokenizer.length; i++)
          symbolTable.remove(keyRemovalTokenizer[i]);
     }

    indent(level+1);
    level--;
    if(showTable) 
        System.out.println("Leaving the WHILE block.");
  }

  public void visit( CompoundExp exp, int level ) {
    if ( exp.decs != null && exp.exps != null )
      level++;
    if ( exp.decs != null ) {
      exp.decs.accept( this, level );
    }
    if ( exp.exps != null ) {
      exp.exps.accept( this, level );
    }
  }
  
  public void visit( FunctionDec exp, int level ) {
    lastFunc = exp.type;
    indent(level+1);
    if(showTable) 
        System.out.println("Entering a new FUNCTION scope for function \"" + exp.id + "\":");
    if (exp.paramlist != null )
      exp.paramlist.accept( this, level+1 );
    if (exp.body != null )
      exp.body.accept( this, level );
      
    if(symbolTable.get(exp.id) == null)
    {
       declarations = new ArrayList<Entry>();
    }
    else if(symbolTable.get(exp.id).get(0).level == level)
    {
       System.err.println("\u001B[31mERROR\u001B[0m: Function \"" + exp.id + "\" already declared, in line " + (exp.row + 1) + ", column " + exp.col + ".");
       indent(level+1);
       if(showTable) 
           System.out.println("Leaving the FUNCTION scope for function \"" + exp.id + "\":");
       level--;
       return;
    }
    else
    {
       declarations = symbolTable.get(exp.id);
    }  

    String type = "(";
    VarDecList t = exp.paramlist;
    while(t != null)
    {
       if(t.head instanceof SimpleDec)
       {
         SimpleDec param = (SimpleDec) t.head;
         type = type + param.type + ",";
         t = t.tail;
       }
       else
       {
         ArrayDec param = (ArrayDec) t.head;
         type = type + param.type + ",";
         t = t.tail;
       }
    }
    if(!type.equals("("))
        type = type.substring(0, type.length() - 1);
    else
        type = "(void";
    type = type + ") -> " + exp.type;
    declarations.add(0, new Entry(exp.id, level, type, exp));
    symbolTable.put(exp.id, declarations);
    
    String keyRemoval = "";
    boolean checkRemove = false;
    
    for(String key: symbolTable.keySet())
    {
       declarations = symbolTable.get(key);
       if(declarations.get(0).level == level+1)
       {
         indent(level+2);
         if(showTable) 
             System.out.println(declarations.get(0).name + ": " + declarations.get(0).type);
         
         if(declarations.size() <= 1)
         {
            keyRemoval += key + ",";
            checkRemove = true;
         }
         else if(declarations.size() > 1)
         {
            declarations.remove(0);
            symbolTable.put(key, declarations);
         }
       }
    }
    if(checkRemove == true)
    {
       keyRemoval = keyRemoval.substring(0, keyRemoval.length() - 1);
       String[] keyRemovalTokenizer = keyRemoval.split(",");
       for(int i = 0; i < keyRemovalTokenizer.length; i++)
          symbolTable.remove(keyRemovalTokenizer[i]);
    }
    indent(level+1);
    if(showTable) 
        System.out.println("Leaving the FUNCTION scope for function \"" + exp.id + "\".");
    level--;
  }
  
  public void visit( ArrayDec exp, int level ) {
    if (exp.size != null )
      exp.size.accept( this, level );
    
    if(symbolTable.get(exp.name) == null)
    {
       declarations = new ArrayList<Entry>();
       declarations.add(0, new Entry(exp.name, level, exp.type, exp));
       symbolTable.put(exp.name, declarations);
    }
    else
    {
       declarations = symbolTable.get(exp.name);
       declarations.add(0, new Entry(exp.name, level, exp.type, exp));
       symbolTable.put(exp.name, declarations);
    }
  }
  
  public void visit( NilExp exp, int level ) {

  }
  
  public void visit( CallExp exp, int level ) {
    if (exp.args != null )
      exp.args.accept( this, level );

    declarations = symbolTable.get(exp.func);
    if(declarations == null)
    {
        System.err.println("\u001B[31mERROR\u001B[0m: Call to undeclared function: \"" + exp.func + "\" in line " + (exp.row + 1) + ", column " + exp.col + ".");
        return;
    }
    ExpList args = exp.args;
    String params = declarations.get(0).type.substring(1, declarations.get(0).type.indexOf(")"));
    
    if(args == null && params.equals(""))
        return;
        
    String[] paramTokens = params.split(",");
    int index = 0;
    
    while(args != null)
    {
        if(args.head instanceof VarExp)
        {
            VarExp head = (VarExp) args.head;
            if(head.variable instanceof SimpleVar)
            {
                SimpleVar arg = (SimpleVar) head.variable;
                if(symbolTable.get(arg.name) != null && (index >= paramTokens.length || !symbolTable.get(arg.name).get(0).type.equals(paramTokens[index++])))
                {
                    System.err.println("\u001B[31mERROR\u001B[0m: Function call parameter mismatch for \"" + exp.func + "\" in line " + (exp.row + 1) + ", column " + exp.col + ".");
                    return;
                }
                args = args.tail;
            }
            else
            {
                IndexVar arg = (IndexVar) head.variable;
                if(symbolTable.get(arg.name) != null && (index >= paramTokens.length || !symbolTable.get(arg.name).get(0).type.equals(paramTokens[index++])))
                {
                    System.err.println("\u001B[31mERROR\u001B[0m: Function call parameter mismatch for \"" + exp.func + "\" in line " + (exp.row + 1) + ", column " + exp.col + ".");
                    return;
                }
                args = args.tail;
            }
        }
        else if(args.head instanceof IntExp)
        {
            if(index >= paramTokens.length || !paramTokens[index++].equals("int"))
            {
                System.err.println("\u001B[31mERROR\u001B[0m: Function call parameter mismatch for \"" + exp.func + "\" in line " + (exp.row + 1) + ", column " + exp.col + ".");
                return;
            }
            args = args.tail;
        }
        else if(args.head instanceof OpExp)
        {
            OpExp head = (OpExp) args.head;
            String expType = checkOp(head);
            if(index >= paramTokens.length || (expType != null && !expType.equals(paramTokens[index++])))
            {
                System.err.println("\u001B[31mERROR\u001B[0m: Function call parameter mismatch for \"" + exp.func + "\" in line " + (exp.row + 1) + ", column " + exp.col + ".");
                return;
            }
            args = args.tail;
        }
        else if(args.head instanceof CallExp)
        {
            CallExp head = (CallExp) args.head;
            if(symbolTable.get(head.func) == null)
                return;
            FunctionDec function = (FunctionDec) symbolTable.get(head.func).get(0).dec;
            if(index >= paramTokens.length || !function.type.equals(paramTokens[index++]))
            {
                System.err.println("\u001B[31mERROR\u001B[0m: Function call parameter mismatch for \"" + exp.func + "\" in line " + (exp.row + 1) + ", column " + exp.col + ".");
                return;
            }
            args = args.tail;
        }
    }
    if(index < paramTokens.length)
    {
        System.err.println("\u001B[31mERROR\u001B[0m: Function call parameter mismatch for \"" + exp.func + "\" in line " + (exp.row + 1) + ", column " + exp.col + ".");
        return;
    }
  }
  
  public void visit( SimpleVar exp, int level ) {
     if(symbolTable.get(exp.name) == null)
     {
         System.err.println("\u001B[31mERROR\u001B[0m: Undeclared variable \"" + exp.name + "\" in line " + (exp.row + 1) + ", column " + exp.col + ".");
         return;
     }
  }
  
  public void visit( IndexVar exp, int level ) {
    if (exp.index != null )
      exp.index.accept( this, level );
      
    if(symbolTable.get(exp.name) == null)
    {
        System.err.println("\u001B[31mERROR\u001B[0m: Undeclared variable \"" + exp.name + "\" in line " + (exp.row + 1) + ", column " + exp.col + ".");
        return;
    }
      
    if(exp.index instanceof VarExp)
    {
        VarExp expIndex = (VarExp) exp.index;
        if(expIndex.variable instanceof SimpleVar)
        {
            SimpleVar expIndexVar = (SimpleVar) expIndex.variable;
            if(symbolTable.get(expIndexVar.name) == null)
            {
                return;
            }
            else if(symbolTable.get(expIndexVar.name).get(0).type != "int")
            {
                System.err.println("\u001B[31mERROR\u001B[0m: Index variable type mismatch \"" + expIndexVar.name + "\" in line " + (expIndexVar.row + 1) + ", column " + expIndexVar.col + ".");
                return;
            }
        }
        else if(expIndex.variable instanceof IndexVar)
        {
            IndexVar expIndexVar = (IndexVar) expIndex.variable;
            if(symbolTable.get(expIndexVar.name) == null)
            {
                return;
            }
            else if(symbolTable.get(expIndexVar.name).get(0).type != "int")
            {
                System.err.println("\u001B[31mERROR\u001B[0m: Index variable type mismatch \"" + expIndexVar.name + "\" in line " + (expIndexVar.row + 1) + ", column " + expIndexVar.col + ".");
                return;
            }
        }
    }
    else if(exp.index instanceof OpExp)
    {
        OpExp index = (OpExp) exp.index;
        String expType = checkOp(index);
        if(expType != null && !expType.equals("int"))
        {
            System.err.println("\u001B[31mERROR\u001B[0m: Invalid index for variable \"" + exp.name + "\" in line " + (exp.row + 1) + ", column " + exp.col + ".");
        }
    }
    else if(exp.index instanceof CallExp)
    {
        CallExp index = (CallExp) exp.index;
        if(symbolTable.get(index.func) == null)
            return;
        FunctionDec function = (FunctionDec) symbolTable.get(index.func).get(0).dec;
        if(!function.type.equals("int"))
        {
            System.err.println("\u001B[31mERROR\u001B[0m: Invalid index for variable \"" + exp.name + "\" in line " + (exp.row + 1) + ", column " + exp.col + ".");
        }
    }
    else if(exp.index instanceof IntExp)
    {
        IntExp expIndex = (IntExp) exp.index;
        Dec expDec = declarations.get(0).dec;
        ArrayDec expArray = (ArrayDec) expDec;
        if(expArray.size != null && expIndex.value >= expArray.size.value)
        {
            System.err.println("\u001B[31mERROR\u001B[0m: Index out of range for variable \"" + exp.name + "\" in line " + (exp.row + 1) + ", column " + exp.col + ".");
            return;
        }
    }
    else
    {
        System.err.println("\u001B[31mERROR\u001B[0m: Invalid index for variable \"" + exp.name + "\" in line " + (exp.row + 1) + ", column " + exp.col + ".");
        return;
    }
  }
  
  public void visit( SimpleDec exp, int level ) {
    
    if(symbolTable.get(exp.id) == null)
    {
       declarations = new ArrayList<Entry>();
       declarations.add(0, new Entry(exp.id, level, exp.type, exp));
       symbolTable.put(exp.id, declarations);
    }
    else if(symbolTable.get(exp.id).get(0).level == level)
    {
       System.err.println("\u001B[31mERROR\u001B[0m: Variable \"" + exp.id + "\" already declared, in line " + (exp.row + 1) + ", column " + exp.col + ".");
       return;
    }
    else
    {
       declarations = symbolTable.get(exp.id);
       declarations.add(0, new Entry(exp.id, level, exp.type, exp));
       symbolTable.put(exp.id, declarations);
    }
  }
  
  public void visit( IntExp exp, int level ) {

  }
  
  public void visit( VarDec exp, int level ) {
  }
}
