/*
Jordan Smith
02/21/22
Cell.java
Section C
Project 2
CS 231
*/


import java.awt.Color;
import java.awt.Graphics;
import java.util.ArrayList;
import java.util.Random;


public class Cell
{
    //simulates a single cell
    
    boolean isAlive;

    //constructor for cell class
    public Cell()
    {
        Random rand = new Random();
        setAlive(rand.nextBoolean());
    }

    //constructor for cell with ability to specify whether dead or alive
    public Cell(boolean alive)
    {
        setAlive(alive);
    }

    //returns  true if cell is alive
    public boolean getAlive()
    {
        return isAlive;
    }

    //sets cell to dead
    public void reset()
    {
        isAlive = false;
    }

    //sets isAlive to alive
    public void setAlive(boolean alive)
    {
        isAlive = alive;
    }

    //draws cell onto the graphics screen
    public void draw(Graphics g, int x, int y, int scale)
    {
        if(getAlive())
        {
            g.setColor(Color.DARK_GRAY);
            g.fillRect(x*scale,y*scale,55,55);
        }
    }

    //toString method for cell
    public String toString()
    {
        //returns 0 if the cell is alive and a space if it is dead.
        if(isAlive)
        {
            return "0";
        }
        else
        {
            return " ";
        }
    }

    //updates whether cell is dead or alive based on whether its neighbors are
    public void updateState(ArrayList<Cell> neighbors)
    {
        int aliveCounter = 0;
        for(Cell cell: neighbors)
        {
            if(cell.getAlive())
            {
                aliveCounter++;
            }
        }
        if(this.getAlive())
        {
            if(aliveCounter == 2 || aliveCounter == 3)
            {
                this.setAlive(true);
            }
            else
            {
                this.setAlive(false);
            }
        }
        else
        {
            if(aliveCounter == 3)
            {
                this.setAlive(true);
            }
        }
    }

    //test cell functions
    public static void main(String[] args)
    {
        Cell cell1 = new Cell();
        System.out.println(cell1.getAlive());
        System.out.println(cell1.toString());
        cell1.setAlive(true);
        System.out.println(cell1.getAlive());
        System.out.println(cell1.toString());
    }
}