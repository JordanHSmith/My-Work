/*
Jordan Smith
03/18/22
Agent.java
Section C
Project 5
CS 231
*/

import java.awt.Graphics;

public class Agent
{
    //Makes an agent with an x and y position
    private double xPos;
    private double yPos;

    public Agent(double x0, double y0)
    {
        //Constructor for Agent class
        xPos = x0;
        yPos = y0;
    }

    public double getX()
    {
        //Returns x position of Agent
        return xPos;
    }

    public double getY()
    {
        //Returns y position of Agent
        return yPos;
    }

    public void setX(double newX)
    {
        //Sets x position of Agent
        xPos = newX;
    }

    public void setY(double newY)
    {
        //Sets y position of Agent
        yPos = newY;
    }

    public String toString()
    {
        //Returns a string of the x and y positions as a point
        return("(" + getX() + ", " + getY() + ")");
    }

    public void updateState(Landscape scape)
    {

    }

    public void draw(Graphics g)
    {

    }

    public static void main(String[] args)
    {
        //Test functions for Agent class
        Agent agent1 = new Agent(10,20);
        System.out.println(agent1.getX());
        System.out.println(agent1.getY());
        System.out.println(agent1.toString());
        agent1.setX(30);
        agent1.setY(40);
        System.out.println(agent1.getX());
        System.out.println(agent1.getY());
        System.out.println(agent1.toString());
    }
}