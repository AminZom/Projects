import absyn.*;

public class ShowTreeVisitor implements AbsynVisitor {

  final static int SPACES = 4;

  private void indent( int level ) {
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
    indent( level );
    System.out.println( "AssignExp: =" );
    level++;
    exp.lhs.accept( this, level );
    exp.rhs.accept( this, level );
  }

  public void visit( IfExp exp, int level ) {
    indent( level );
    System.out.println( "IfExp:" );
    level++;
    exp.test.accept( this, level );
    exp.thenpart.accept( this, level );
    if (exp.elsepart != null )
       exp.elsepart.accept( this, level );
  }

  public void visit( OpExp exp, int level ) {
    indent( level );
    System.out.print( "OpExp:" ); 
    switch( exp.op ) {
      case OpExp.PLUS:
        System.out.println( " + " );
        break;
      case OpExp.MINUS:
        System.out.println( " - " );
        break;
      case OpExp.TIMES:
        System.out.println( " * " );
        break;
      case OpExp.OVER:
        System.out.println( " / " );
        break;
      case OpExp.EQ:
        System.out.println( " = " );
        break;
      case OpExp.LT:
        System.out.println( " < " );
        break;
      case OpExp.GT:
        System.out.println( " > " );
        break;
      case OpExp.EQEQ:
        System.out.println( " == " );
        break;
      case OpExp.NEQ:
        System.out.println( " != " );
        break;
      case OpExp.GTE:
        System.out.println( " >= " );
        break;
      case OpExp.LTE:
        System.out.println( " <= " );
        break;
      default:
        System.out.println( "Unrecognized operator at line " + exp.row + " and column " + exp.col);
    }
    level++;
    exp.left.accept( this, level );
    exp.right.accept( this, level );
  }

  public void visit( VarExp exp, int level ) {
    indent( level );
    System.out.println( "VarExp:" );
    level++;
    if (exp.variable != null )
      exp.variable.accept( this, level );
    
  }
  
  public void visit( ReturnExp exp, int level ) {
    indent( level );
    System.out.println( "ReturnExp:" );
    level++;
    if (exp.exp != null )
      exp.exp.accept( this, level );
  }
  
  public void visit( WhileExp exp, int level ) {
    indent( level );
    System.out.println( "While:" );
    level++;
    if (exp.body != null )
      exp.body.accept( this, level );
    if (exp.test != null )
      exp.test.accept( this, level );
  }

  public void visit( CompoundExp exp, int level ) {
    indent( level );
    System.out.println( "CompoundExp:" );
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
    indent( level );
    System.out.println( "FunctionDec: " + exp.id );
    level++;
    if (exp.paramlist != null )
      exp.paramlist.accept( this, level );
    if (exp.body != null )
      exp.body.accept( this, level );
  }
  
  public void visit( ArrayDec exp, int level ) {
    indent( level );
    System.out.println( "ArrayDec: " + exp.name);
    level++;
    if (exp.size != null )
      exp.size.accept( this, level );
  }
  
  public void visit( NilExp exp, int level ) {
    indent( level );
    System.out.println( "NilExp: ");
  }
  
  public void visit( CallExp exp, int level ) {
    indent( level );
    System.out.println( "Callexp: " + exp.func);
    level++;
    if (exp.args != null )
      exp.args.accept( this, level );
  }
  
  public void visit( SimpleVar exp, int level ) {
    indent( level );
    System.out.println( "simple var: " + exp.name);
    level++;
  }
  
  public void visit( IndexVar exp, int level ) {
    indent( level );
    System.out.println( "indexvar: " + exp.name );
    level++;
    if (exp.index != null )
      exp.index.accept( this, level );
  }
  
  public void visit( SimpleDec exp, int level ) {
    indent( level );
    System.out.println( "simple dec: " + exp.id );
    level++;
  }
  
  public void visit( IntExp exp, int level ) {
    indent( level );
    System.out.println( "int exp: " + exp.value );
    level++;
  }
  
  public void visit( VarDec exp, int level ) {
  }
}
