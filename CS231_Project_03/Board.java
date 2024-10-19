/*
Jordan Smith
03/11/22
Board.java
CS231 B
Project 03/04
*/

import java.io.*;
import java.awt.*;

public class Board
{
    //Creates a board of cells
    private Cell[][] cells;
    public static final int Size = 9;

    public Board()
    {
        //Constructor for Board
        cells = new Cell[Board.Size][Board.Size];
        for(int i=0; i<Board.Size; i++)
        {
            for(int j=0; j<Board.Size; j++)
            {
                cells[i][j] = new Cell(i,j,0);
            }
        }
    }

    public String toString()
    {
        //Returns the contents of cells so that it looks like a Sudoku board
        String board_display = "";
        for(int i=0; i<Board.Size; i++)
        {
            for(int j=0; j<Board.Size; j++)
            {
                //adding spaces between every 3 columns
                if(j == 3 || j == 6)
                {
                    board_display += " ";
                }
                board_display += cells[i][j].getValue() + " ";
            }
            //adding extra line between every 3 rows
            if(i == 2 || i == 5)
            {
                board_display += "\n";
            }
            board_display += "\n";
        }
        return board_display;
    }

    public int getCols()
    {
        //Returns the number of columns
        return Board.Size;
    }

    public int getRows()
    {
        //Returns the number of rows
        return Board.Size;
    }

    public Cell get(int r, int c)
    {
        //(int,int) -> (Cell)
        //Returns the cell at row r, column c
        return cells[r][c];
    }

    public boolean isLocked(int r, int c)
    {
        //(int,int) -> (boolean)
        //Returns true if the cell at row r, column c is locked
        return cells[r][c].isLocked();
    }

    public int numLocked()
    {
        //Returns the number of locked cells on the board
        int sumIsLocked = 0;
        for(int i=0; i<Board.Size; i++)
        {
            for(int j=0; j<Board.Size; j++)
            {
                if(cells[i][j].isLocked())
                {
                    sumIsLocked++;
                }
            }
        }
        return sumIsLocked;
    }

    public int value(int r, int c)
    {
        //(int,int) -> (int)
        //Returns the value of the cell at row r, column c
        return cells[r][c].getValue();
    }

    public void set(int r, int c, int value)
    {
        //(int,int) -> (None)
        //sets the value of the cell at row r, column c to value
        cells[r][c].setValue(value);
    }

    public void set(int r, int c, int value, boolean locked)
    {
        //(int,int, int, boolean) -> (None)
        //sets the value of the cell at row r, column c to value and its isLocked to locked
        cells[r][c].setValue(value);
        cells[r][c].setLocked(locked);
    }


    public boolean read(String filename)
    {
        //Displays the text in filename as a Sudoku board
        try
        {
            FileReader fileReader = new FileReader(filename);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String line = bufferedReader.readLine();

            int counter = 0;
            //Will run until the file has no more lines to read
            while(line != null)
            {
                String[] str = new String[9];
                str = line.split("[ ]+");

                //Assigns one row worth of values
                for(int i=0; i<9; i++)
                {
                    cells[counter][i].setValue(Integer.parseInt(str[i]));
                }

                //Puts spaces in appropriate locations
                for(int i=0; i<str.length; i++)
                {
                    System.out.print(str[i] + " ");
                    if((i+1) % 3 == 0)
                    {
                        System.out.print(" ");
                    }
                }
                
                //Goes to next line when appropriate
                if((counter+1) % 3 == 0)
                {
                    System.out.print("\n");
                }
                System.out.println();
                //Sets conditions for going to next line
                line = bufferedReader.readLine();
                counter++;
            }
            // closes bufferedReader
            bufferedReader.close();
            return true;
        }
        catch(FileNotFoundException ex) {
            System.out.println("Board.read():: unable to open file " + filename );
        }
        catch(IOException ex) {
            System.out.println("Board.read():: error reading file " + filename);
        }
        return false;
    }

    public boolean validValue(int row, int col, int value)
    {
        //Returns true if value can be assigned to cell at row, col without breaking the rules of Sudoku

        //Returns false if the same value occurs twice in the same row or column
        if(value > 0 && value <10)
        {
            for(int i=0; i<Board.Size; i++)
            {
                if((cells[row][i].getValue() == value && i != col) || (cells[i][col].getValue() == value && i != row)) //if((val.equals(board[row][j]) && j != col) || (val.equals(board[i][col]) && i != row)) 
                {
                return false;
                }
            }
        }

        //Returns false if the same value is found in the same 3x3 square
        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;
        for(int i=0; i<3; i++)
        {
            for(int j=0; j<3; j++)
            {
                if(value == cells[startRow+i][startCol+j].getValue() && !(startRow+i==row && startCol+j==col))
                {
                    return false;
                }
            }
        }
        return true;
    }

    public boolean validSolution()
    {
        //Returns true if all values in the board are valid
        for(int i=0; i<cells.length; i++)
        {
            for(int j=0; j<cells.length; j++)
            {
                if(!this.validValue(i,j,cells[i][j].getValue()))
                {
                    return false;
                }
            }
        }
        return true;
    }

    public Cell findBestCell()
    {
        //Goes to the next cell with a value of 0 and tests out values 1-9
        for(int i=0; i<Board.Size; i++)
        {
            for(int j=0; j<Board.Size;j++)
            {
                if(cells[i][j].getValue() == 0)
                {
                    for(int k=1; k<10; k++)
                    {
                        if(validValue(i,j,k))
                        {
                            cells[i][j].setValue(k);
                            return cells[i][j];
                        }
                    }
                    return null;
                }
            }
        }
        return null;
    }


    public void draw(Graphics g, int scale)
    {
        //Displays the value of cell based on its position in the 2d-array
        for(int i=0; i<Board.Size; i++)
        {
            for(int j=0; j<Board.Size; j++)
            {
                cells[i][j].draw(g, 1+j, i+1, scale);
            }
        }
    }
    public static void main(String[] args)
    {
        //Test methods that read in a file
        Board board1 = new Board();
        board1.read(args[0]);

        System.out.println(board1.toString());
        System.out.println("Rows: " + board1.getRows());
        System.out.println("Cols: " + board1.getCols());
        System.out.println("Cell: " + board1.get(2,2));
        System.out.println("isLocked: " + board1.isLocked(2,2));
        System.out.println("numLocked: " + board1.numLocked());
        System.out.println("Value: " + board1.value(2,2));
        board1.set(2,2,6,true);
        System.out.println("isLocked: " + board1.isLocked(2,2));
        System.out.println("numLocked: " + board1.numLocked());
        System.out.println("Value: " + board1.value(2,2));
        System.out.println("Valid Value: " + board1.validValue(1, 1, 4));
        System.out.println("Valid Value: " + board1.validValue(1, 1, 3));
        System.out.println("Valid Value: " + board1.validValue(1, 8, 2));
        System.out.println("Valid Value: " + board1.validValue(1, 8, 3));
        System.out.println("Valid Value: " + board1.validValue(8, 5, 4));
        System.out.println("Valid Value: " + board1.validValue(8, 5, 8));
        System.out.println("Valid Solution: " + board1.validSolution());
    }
}
