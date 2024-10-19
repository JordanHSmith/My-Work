/*
Jordan Smith
03/18/22
AntiSocialAgent.java
Section C
Project 5
CS 231
*/

import java.util.ArrayList;
import java.util.Random;

public class AntiSocialAgent extends SocialAgent
{
    //Makes an agent that is attracted to its neighbors
    private boolean moved;
    
    public AntiSocialAgent(double x0, double y0, int radius)
    {
        //Constructor for AntiSocialAgent
        super(x0,y0,radius);
        moved = false;
    }

    public void updateState(Landscape scape)
    {
        //Moves agents based on their proximity to other agents
        ArrayList<Agent> neighbors = new ArrayList<Agent>();
        neighbors = scape.getNeighbors(this.getX(), this.getY(), this.getRadius());
        if(neighbors.size() > 3)
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
            int rand = (int)(Math.random()*100);
            if(rand < 1)
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
    }

    public static void main(String[] args)
    {
        //Test code for SocialAgent class
        SocialAgent socialAgent = new SocialAgent(10,20,100);
        System.out.println(socialAgent.getX());
        System.out.println(socialAgent.getY());
        System.out.println(socialAgent.getRadius());
        System.out.println(socialAgent.toString());
        socialAgent.setX(30);
        socialAgent.setY(40);
        socialAgent.setRadius(200);
        System.out.println(socialAgent.getX());
        System.out.println(socialAgent.getY());
        System.out.println(socialAgent.getRadius());
        System.out.println(socialAgent.toString());

        SocialAgent socialAgent1 = new SocialAgent(5,5,5);
        SocialAgent socialAgent2 = new SocialAgent(10,10,5);
        SocialAgent socialAgent3 = new SocialAgent(15,15,5);
        SocialAgent socialAgent4 = new SocialAgent(20,20,5);
        Landscape testLandscape = new Landscape(500, 500);
        testLandscape.addAgent(socialAgent1);
        testLandscape.addAgent(socialAgent2);
        testLandscape.addAgent(socialAgent3);
        testLandscape.addAgent(socialAgent4);
        socialAgent1.updateState(testLandscape);
        ArrayList<Agent> neighbors = new ArrayList<Agent>();
        neighbors = testLandscape.getNeighbors(5,5,10);
        System.out.println("First run");
        for(Agent agent: neighbors)
        {
            System.out.println(agent.getX());
        }

        socialAgent1.setX(5);
        socialAgent1.setY(5);
        socialAgent1.updateState(testLandscape);
        neighbors = testLandscape.getNeighbors(5,5,15);
        System.out.println("Second run");
        for(Agent agent: neighbors)
        {
            System.out.println(agent.getX());
        }

        socialAgent1.setX(5);
        socialAgent1.setY(5);
        socialAgent1.updateState(testLandscape);
        neighbors = testLandscape.getNeighbors(5,5,25);
        System.out.println("Third run");
        for(Agent agent: neighbors)
        {
            System.out.println(agent.getX());
        }
    }
}
