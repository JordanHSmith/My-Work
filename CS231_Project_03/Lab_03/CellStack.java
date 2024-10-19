/*
Jordan Smith
03/11/22
CellStack.java
CS231 B
Project 03/04
*/

package Lab_03;

public class CellStack
{
    private Cell[] cellStack;
    private int topIndex;

    public CellStack()
    {
        cellStack = new Cell[10];
        topIndex = 0;
    }

    public CellStack(int max)
    {
        cellStack = new Cell[max];
        topIndex = 0;
    }

    public void push(Cell c)
    {
        if(topIndex < cellStack.length)
        {
            cellStack[topIndex] = c;
            topIndex++;
        }
        else
        {
            Cell newStack[] = new Cell[cellStack.length*2];
            for(int i=0; i<cellStack.length; i++)
            {
                newStack[i] = cellStack[i];
            }
            cellStack = newStack;
            cellStack[topIndex] = c;
        }
    }

    public Cell pop()
    {
        Cell topCell;
        if(!empty())
        {
            topCell = cellStack[topIndex];
            topIndex--;
            return topCell;
        }
        else
        {
            return null;
        }
    }

    public int size()
    {
        return topIndex+1;
    }

    public boolean empty()
    {
        if(size() > 0)
        {
            return false;
        }
        else
        {
            return true;
        }
    }
}
