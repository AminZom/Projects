package absyn;

public class SimpleDec extends VarDec {
  public String id;
  public String type;

  public SimpleDec( int row, int col, String type, String id ) {
    this.row = row;
    this.col = col;
    this.id = id;
    this.type = type;
  }

  public void accept( AbsynVisitor visitor, int level ) {
    visitor.visit( this, level );
  }
}
