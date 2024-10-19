/*
Jordan Smith
03/11/22
Cell.java
CS231 B
Project 03/04
*/

import java.awt.*;

public class Cell
{
    //Creates a singlular cell of a Sudoku Board
    private int rowIndex;
    private int colIndex;
    private int value;
    private boolean isLocked;

    public Cell()
    {
        //Default constructor for Cell
        rowIndex = 0;
        colIndex = 0;
        value = 0;
        isLocked = false;
    }

    public Cell(int row, int col, int value)
    {
        //Constructor for Cell with specified values for row, col, and value
        rowIndex = row;
        colIndex = col;
        this.value = value;
        isLocked = false;
    }

    public Cell(int row, int col, int value, boolean locked)
    {
        //Constructor for Cell with specified values for row, col, value, and locked
        rowIndex = row;
        colIndex = col;
        this.value = value;
        isLocked = locked;
    }

    public int getRow()
    {
        //Returns rowIndex
        return rowIndex;
    }

    public int getCol()
    {
        //Returns colIndex
        return colIndex;
    }

    public int getValue()
    {
        //Returns value
        return value;
    }

    public void setValue(int newVal)
    {
        //(int) -> (None)
        //Sets value to newVal
        value = newVal;
    }

    public boolean isLocked()
    {
        //Returns isLocked
        return isLocked;
    }

    public void setLocked(boolean lock)
    {
        //(boolean) -> (None)
        //Sets isLocked to lock
        isLocked = lock;
    }

    public Cell clone()
    {
        //Creates a clone (copy) of a Cell object
        Cell newCell = new Cell();
        newCell.rowIndex = getRow();
        newCell.colIndex = getCol();
        newCell.setValue(getValue());
        newCell.setLocked(isLocked());
        return newCell;
    }

    public void draw(Graphics g, int x0, int y0, int scale)
    {
        //Displays a cell value onto a window
        char[] chars = new char[2];
        chars[0] = (char)('0' + this.value);
        chars[1] = 0;
        g.drawChars(chars,0,1,x0 * scale,y0 * scale);
    }
}