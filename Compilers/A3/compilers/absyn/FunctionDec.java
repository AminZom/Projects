package absyn;

public class FunctionDec extends Dec {
  public String id;
  public String type;
  public VarDecList paramlist;
  public CompoundExp body;
  
  public FunctionDec( int row, int col, String type, String id, VarDecList paramlist, CompoundExp body) {
    this.row = row;
    this.col = col;
    this.id = id;
    this.type = type;
    this.paramlist = paramlist;
    this.body = body;
  }

  public void accept( AbsynVisitor visitor, int level ) {
    visitor.visit( this, level );
  }
}
