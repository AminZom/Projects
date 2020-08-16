package absyn;

public class Entry {
    public String name;
    public int level;
    public String type;
    public Dec dec;
    
    public Entry (String name, int level, String type, Dec dec) {
        this.name = name;
        this.level = level;
        this.type = type;
        this.dec = dec;
    }
}
