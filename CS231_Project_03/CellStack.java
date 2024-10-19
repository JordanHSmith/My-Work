/*
Jordan Smith
03/11/22
CellStack.java
CS231 B
Project 03/04
*/

public class CellStack
{
    //Creates an array-based stack of Cell objects
    private Cell[] cellStack;
    private int topIndex;

    public CellStack()
    {
        //Default Constructor for CellStack()
        cellStack = new Cell[10];
        topIndex = 0;
    }

    public CellStack(int max)
    {
        //Consturctor with specified value for maximum capacity
        cellStack = new Cell[max];
        topIndex = 0;
    }

    public void push(Cell c)
    {
        //Adds Cell c onto the top of the stack if it is not full.
        if(topIndex < cellStack.length)
        {
            cellStack[topIndex] = c;
            topIndex++;
        }
        //If the stack is full, makes new stack with twice the length, data over, and adds Cell c
        else
        {
            Cell newStack[] = new Cell[cellStack.length*2];
            for(int i=0; i<cellStack.length; i++)
            {
                newStack[i] = cellStack[i];
            }
            cellStack = newStack;
            cellStack[topIndex] = c;
            topIndex++;
        }
    }

    public Cell pop()
    {
        //Removes the top element of the array-based stack
        Cell topCell;
        if(!empty())
        {
            topIndex--;
            topCell = cellStack[topIndex];
            return topCell;
        }
        //If stack is empty, returns null
        else
        {
            return null;
        }
    }

    public Cell peek()
    {
        //Returns the top element of the stack
        Cell topCell;
        if(!empty())
        {
            topCell = cellStack[topIndex-1];
            return topCell;
        }
        //Returns null if stack is empty
        else
        {
            return null;
        }
    }

    public int size()
    {
        //Returns topindex (which is the size of the stack)
        return topIndex;
    }

    public boolean empty()
    {
        //Returns true if the stack's size is not 0
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
