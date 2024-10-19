/*
Jordan Smith
03/11/22
Sudoku_Extension.java
CS231 B
Project 03/04
*/

public class Sudoku_Extension
{
    //Creates a Sudoku board without displaying it
    private Board board;

    public Sudoku_Extension()
    {
        //Default constructor for Sudoku_Extension
        board = new Board();
    }

    public Sudoku_Extension(int N)
    {
        //Constructor for Sudoku that accounts for intially locked values
        board = new Board();

        //Assigns random, valid values for the number of cells locked (N)
        for(int i=0; i<N; i++)
        {
            int randX = (int)(Math.random() * Board.Size);
            int randY = (int)(Math.random() * Board.Size);
            int randVal = (int)(Math.random() * 9)+1;

            if(board.get(randX,randY).getValue() == 0)
            {
                if(board.validValue(randX,randY,randVal))
                {
                    board.get(randX,randY).setValue(randVal);
                }
                //Decrement is necessary to assign new value if first one was not valid
                else
                {
                    i--;
                }
            }
            else
            {
                i--;
            }
        }
    }

    public Board getBoard()
    {
        //Returns the board
        return board;
    }

    public boolean solve(int numLocked)
    {
        //Solves the Sudoku board by testing if values are valid
        CellStack stack = new CellStack(81);

        //Will run for each cell that does not have a locked value
        while(stack.size() < Board.Size*Board.Size-numLocked)
        {
            Cell nextCell = board.findBestCell();

            //If the proposed value is valid, append it to the stack and apply it to the board
            if(nextCell != null)
            {
                stack.push(nextCell);
                board.set(nextCell.getRow(),nextCell.getCol(),nextCell.getValue());
            }
            else
            {
                boolean isStuck = true;
                while(isStuck && !stack.empty())
                {
                    //Backtracks and tests the next value after the one just tried
                    nextCell = stack.pop();
                    for(int i=nextCell.getValue()+1; i<10; i++)
                    {
                        if(board.validValue(nextCell.getRow(),nextCell.getCol(),i))
                        {
                            board.set(nextCell.getRow(),nextCell.getCol(),i);
                            stack.push(nextCell);
                            isStuck = false;
                            break;
                        }
                    }
                    //Runs if no valid values found
                    if(isStuck)
                    {
                        board.set(nextCell.getRow(),nextCell.getCol(),0);
                    }
                }
                if(stack.empty())
                {
                    return false;
                }
            }
        }
        System.out.println(board.toString());
        return true;
    }
}
