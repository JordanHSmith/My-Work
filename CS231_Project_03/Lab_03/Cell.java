/*
Jordan Smith
03/11/22
Cell.java
CS231 B
Project 03/04
*/

package Lab_03;

public class Cell
{
    int rowIndex;
    int colIndex;
    int value;
    boolean isLocked;

    public Cell()
    {
        rowIndex = 0;
        colIndex = 0;
        value = 0;
        isLocked = false;
    }

    public Cell(int row, int col, int value)
    {
        rowIndex = row;
        colIndex = col;
        this.value = value;
        isLocked = false;
    }

    public Cell(int row, int col, int value, boolean locked)
    {
        rowIndex = row;
        colIndex = col;
        this.value = value;
        isLocked = locked;
    }

    public int getRow()
    {
        return rowIndex;
    }

    public int getCol()
    {
        return colIndex;
    }

    public int getValue()
    {
        return value;
    }

    public void setValue(int newVal)
    {
        value = newVal;
    }

    public boolean isLocked()
    {
        return isLocked;
    }

    public void setLocked(boolean lock)
    {
        isLocked = lock;
    }

    public Cell clone()
    {
        Cell newCell = new Cell();
        newCell.rowIndex = getRow();
        newCell.colIndex = getCol();
        newCell.setValue(getValue());
        newCell.setLocked(isLocked());
        return newCell;
    }

    public String toString()
    {
        return "The cell's value is: " + getValue();
    }

    
}