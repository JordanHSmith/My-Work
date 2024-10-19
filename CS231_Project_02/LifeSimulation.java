/*
Jordan Smith
02/21/22
LifeSimulation.java
Section C
Project 2
CS 231
*/

import java.util.Random;

public class LifeSimulation
{
    //simulates the Game of Life
    public static void main(String[] args) throws InterruptedException
    {
        //code used to display and update the Game of Life
        Landscape scape = new Landscape(100,100);
        Random gen = new Random();
        double density = 0.3;

        // initialize the grid to be 30% full
        for (int i = 0; i < scape.getRows(); i++)
        {
            for (int j = 0; j < scape.getCols(); j++ )
            { 
                scape.getCell( i, j ).setAlive( gen.nextDouble() <= density );
            }
        }

        LandscapeDisplay display = new LandscapeDisplay(scape, 8);

        for (int i = 0; i < 20; i++)
        {
            scape.advance();
            display.repaint();
            Thread.sleep(250);
        }
    }
}