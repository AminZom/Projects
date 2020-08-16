package absyn;

public class ArrayDec extends VarDec {
  public String type;
  public String name;
  public IntExp size;

  public ArrayDec( int row, int col, String type, String name , IntExp size) {
    this.row = row;
    this.col = col;
    this.name = name;
    this.size = size;
    this.type = type;
  }

  public void accept( AbsynVisitor visitor, int level ) {
    visitor.visit( this, level );
  }
}
