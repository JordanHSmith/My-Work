/*
Jordan Smith
02/21/22
Landscape.java
Section C
Project 2
CS 231
*/

import java.util.ArrayList;
import java.awt.Graphics;

public class Landscape
{
    //simulates a grid of cells

    Cell[][] cells;
    int rows;
    int cols;

    //constructor for Landscape
    public Landscape(int rows, int cols)
    {
        this.rows = rows;
        this.cols = cols;
        cells = new Cell[rows][cols];
        for(int i=0; i<rows; i++)
        {
            for(int j=0; j<cols; j++)
            {
                cells[i][j] = new Cell();
            }
        }
    }

    //sets all sells in the grid to dead
    public void reset()
    {
        for(int i=0; i<rows; i++)
        {
            for(int j=0; j<cols; j++)
            {
                cells[i][j].reset();
            }
        }
    }

    //returns number of rows in the grid
    public int getRows()
    {
        return rows;
    }

    //returns number of cols in the grid
    public int getCols()
    {
        return cols;
    }

    //returns the cell at the specified row and col
    public Cell getCell(int row, int col)
    {
        return cells[row][col];
    }

    //toString method for Landscape
    public String toString()
    {
        String printerCells = "";
        for(int i=0; i<rows; i++)
        {
            for(int j=0; j<cols; j++)
            {
                printerCells += cells[i][j].toString();
            }
            if(i<rows-1)
            {
                printerCells += "\n";
            }
        }
        return printerCells;
    }

    public ArrayList<Cell> getNeighbors(int row, int col)
    {
        ArrayList<Cell> neighbors = new ArrayList<Cell>();
        int deleteOption = 0;
        
        //These cases check for special cases along the border of the grid
        if(row>0 && row<this.getRows()-1)
        {
            if(col>0 && col<this.getCols()-1)
            {
                for(int i=-1; i<2; i++)
                {
                    for(int j=-1; j<2; j++)
                    {
                        neighbors.add(cells[row+i][col+j]);
                        deleteOption = 0;
                    }
                }
            }
            else if(col == 0)
            {
                for(int i=-1; i<2; i++)
                {
                    for(int j=0; j<2; j++)
                    {
                        neighbors.add(cells[row+i][col+j]);
                        deleteOption = 1;
                    }
                }
            }
            else if(col == this.getCols()-1)
            {
                for(int i=-1; i<2; i++)
                {
                    for(int j=-1; j<1; j++)
                    {
                        neighbors.add(cells[row+i][col+j]);
                        deleteOption = 2;
                    }
                }
            }
        }
        else if(row == 0)
        {
            if(col>0 && col<this.getCols()-1)
            {
                for(int i=0; i<2; i++)
                {
                    for(int j=-1; j<2; j++)
                    {
                        neighbors.add(cells[row+i][col+j]);
                        deleteOption = 3;
                    }
                }
            }
            else if(col==0)
            {
                for(int i=0; i<2; i++)
                {
                    for(int j=0; j<2; j++)
                    {
                        neighbors.add(cells[row+i][col+j]);
                        deleteOption = 4;
                    }
                }
            }
            else if(col==this.getCols()-1)
            {
                for(int i=0; i<2; i++)
                {
                    for(int j=-1; j<1; j++)
                    {
                        neighbors.add(cells[row+i][col+j]);
                        deleteOption = 5;
                    }
                }
            }
        }
        else if(row == this.getRows()-1)
        {
            if(col>0 && col<this.getCols()-1)
            {
                for(int i=-1; i<1; i++)
                {
                    for(int j=-1; j<2; j++)
                    {
                        neighbors.add(cells[row+i][col+j]);
                        deleteOption = 6;
                    }
                }
            }
            else if(col==0)
            {
                for(int i=-1; i<1; i++)
                {
                    for(int j=0; j<2; j++)
                    {
                        neighbors.add(cells[row+i][col+j]);
                        deleteOption = 7;
                    }
                }
            }
            else if(col==this.getCols()-1)
            {
                for(int i=-1; i<1; i++)
                {
                    for(int j=-1; j<1; j++)
                    {
                        neighbors.add(cells[row+i][col+j]);
                        deleteOption = 8;
                    }
                }
            }
        }

        if(deleteOption == 0 || deleteOption == 6)
        {
            neighbors.remove(4);
        }
        else if(deleteOption == 1 || deleteOption == 7)
        {
            neighbors.remove(2);
        }
        else if(deleteOption == 2 || deleteOption == 8)
        {
            neighbors.remove(3);
        }
        else if(deleteOption == 3 || deleteOption == 5)
        {
            neighbors.remove(1);
        }
        else if(deleteOption == 4)
        {
            neighbors.remove(0);
        }

        return neighbors;
    }

    //draws the cells based on their location in the matrix
    public void draw(Graphics g, int gridScale)
    {
        for(int i=0; i<getRows(); i++)
        {
            for(int j=0; j<getCols(); j++)
            {
                cells[i][j].draw(g,i*gridScale,j*gridScale,gridScale);
            }
        }
    }

    //kills, creates, and maintains cells in accordance with the rule of the Game of Life
    public void advance()
    {
        Cell[][] tempCells = new Cell[rows][cols];
        for(int i=0; i<rows; i++)
        {
            for(int j=0; j<cols; j++)
            {
                if(cells[i][j].getAlive())
                {
                    Cell cell = new Cell(true);
                    tempCells[i][j] = cell;
                }
                else
                {
                    Cell cell = new Cell(false);
                    tempCells[i][j] = cell;
                }
            }
        }
        for(int i=0; i<rows; i++)
        {
            for(int j=0; j<cols; j++)
            {
                tempCells[i][j].updateState(getNeighbors(i,j));
            }
        }
        cells = tempCells;
    }

    //test code
    public static void main(String[] args)
    {
        Landscape landscape1 = new Landscape(5,5);
        System.out.println(landscape1.getRows());
        System.out.println(landscape1.getCols());
        System.out.println(landscape1.toString());
        Landscape landscape2 = new Landscape(3,5);
        System.out.println(landscape2.getRows());
        System.out.println(landscape2.getCols());
        System.out.println(landscape2.toString());
        Landscape landscape3 = new Landscape(5,3);
        System.out.println(landscape3.getRows());
        System.out.println(landscape3.getCols());
        System.out.println(landscape3.toString());

        System.out.println("Neighbors: " + landscape1.getNeighbors(3,3));
        landscape1.advance();
        System.out.println("Neighbors: " + landscape1.getNeighbors(3,3));
        
    }
}
