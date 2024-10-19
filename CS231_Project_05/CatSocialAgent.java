/*
Jordan Smith
03/18/22
CatSocialAgent.java
Section C
Project 5
CS 231
*/

import java.awt.Graphics;
import java.awt.Color;
import java.util.ArrayList;
import java.util.Random;

public class CatSocialAgent extends SocialAgent
{
    //Creates social agents of various categories
    private int category;
    private boolean moved;

    public CatSocialAgent(double x0, double y0, int cat)
    {
        //Constructor for CatSocialAgent class
        super(x0,y0,80);
        category = cat;
        moved = false;
    }

    public int getCategory()
    {
        //Returns category of agent
        return category;
    }

    public String toString()
    {
        //Returns the category of the agent in string form
        return String.valueOf(category);
    }

    public void draw(Graphics g)
    {
        //Draws agents as different colors based on which of three categories it is
        Color darkBlue = new Color(0,0,180);
        Color lightBlue = new Color(0,0,255);
        Color darkGreen = new Color(0,180,0);
        Color lightGreen = new Color(0,255,0);
        Color darkRed = new Color(180,0,0);
        Color lightRed = new Color(255,0,0);
        if(this.getCategory() == 1)
        {
            if(moved)
            {
                g.setColor(lightBlue);
            }
            else
            {
                g.setColor(darkBlue);
            }
        }
        else if(this.getCategory() == 2)
        {
            if(moved)
            {
                g.setColor(lightGreen);
            }
            else
            {
                g.setColor(darkGreen);
            }
        }
        else if(this.getCategory() == 3)
        {
            if(moved)
            {
                g.setColor(lightRed);
            }
            else
            {
                g.setColor(darkRed);
            }
        }
        g.fillOval((int)(getX()),(int)(getY()),5,5);
    }

    public void updateState(Landscape scape)
    {
        //Moves agents based on their proximity to other agents and their neighbors' categories
        ArrayList<Agent> neighbors = new ArrayList<Agent>();
        ArrayList<CatSocialAgent> catNeighbors = new ArrayList<CatSocialAgent>();
        int numSameCat = 0;
        int numDifCat = 0;
        neighbors = scape.getNeighbors(this.getX(), this.getY(), this.getRadius());
        //Makes array list of neighboring agents with category included
        
        for(Agent neighbor: neighbors)
        {
            CatSocialAgent catAgent = new CatSocialAgent(neighbor.getX(), neighbor.getY(), this.getCategory());
            catNeighbors.add(catAgent);
        }

        //Counts number of neighboring cells with same category
        for(CatSocialAgent catAgent: catNeighbors)
        {
            if(this.getCategory() == catAgent.getCategory())
            {
                numSameCat++;
            }
            else
            {
                numDifCat++;
            }
        }
        
        //Moves if there at least 2 neighbors and the ones of the same category are more numerous
        if(neighbors.size() >= 2 && numSameCat > numDifCat)
        {
            if((int)(Math.random()*100) < 1)
            {
                Random random = new Random();
                double deltaX = random.nextFloat()*20 - 10;
                double deltaY = random.nextFloat()*20 - 10;
                this.setX(this.getX() + deltaX);
                this.setY(this.getY() + deltaY);
                this.moved = true;
            }
            else
            {
                this.moved = false;
            }
        }
        else
        {
            Random random = new Random();
            double deltaX = random.nextFloat()*20 - 10;
            double deltaY = random.nextFloat()*20 - 10;
            this.setX(this.getX() + deltaX);
            this.setY(this.getY() + deltaY);
            this.moved = true;
        }
    }
}
