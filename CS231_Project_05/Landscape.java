/*
Jordan Smith
03/18/22
Landscape.java
Section C
Project 5
CS 231
*/

import java.util.ArrayList;
import java.awt.Graphics;

public class Landscape
{
    //Creates a landscape that holds many agents
    private int width;
    private int height;
    private LinkedList<Agent> agentList;

    public Landscape(int w, int h)
    {
        //Constructor for Landscape class
        agentList = new LinkedList<Agent>();
        width = w;
        height = h;
    }

    public int getHeight()
    {
        //Returns height of landscape
        return height;
    }

    public int getWidth()
    {
        //Returns width of landscape
        return width;
    }

    public void addAgent(Agent a)
    {
        //Adds agents to the beginning of agent list
        agentList.addFirst(a);
    }

    public String toString()
    {
        //Returns a string of how many agents are in the agentList
        return("There are " + agentList.size() + " agents on the Landscape.");
    }

    public ArrayList<Agent> getNeighbors(double x0, double y0, double radius)
    {
        //Returns an arrayList of agents within the radius of the specified location
        ArrayList<Agent> agents = new ArrayList<Agent>();
        for(Agent agent: agentList)
        {
            if(Math.sqrt(Math.pow(x0-agent.getX(),2)+(Math.pow(y0-agent.getY(),2)))<radius)
            {
                agents.add(agent);
            }
        }
        return agents;
    }

    public void draw(Graphics g)
    {
        //Draws all agents
        for(Agent agent: agentList)
        {
            agent.draw(g);
        }
    }

    public void updateAgents()
    {
        //Updates the position of all agents in a random order
        ArrayList<Agent> shuffledList = new ArrayList<Agent>();
        shuffledList = agentList.toShuffledList();
        for(Agent agent: shuffledList)
        {
            agent.updateState(this);
        }
    }

    public static void main(String[] args)
    {
        //Test code for Landscape class
        Landscape landscape = new Landscape(500,500);
        Agent agent1 = new Agent(10,10);
        Agent agent2 = new Agent(20,20);
        Agent agent3 = new Agent(21,21);
        System.out.println(landscape.getWidth());
        System.out.println(landscape.getHeight());
        System.out.println(landscape.toString());
        landscape.addAgent(agent1);
        System.out.println(landscape.toString());
        landscape.addAgent(agent1);
        landscape.addAgent(agent2);
        landscape.addAgent(agent3);
        System.out.println(landscape.toString());
        ArrayList<Agent> neighbors = new ArrayList<Agent>();
        neighbors = landscape.getNeighbors(20,20,5);
        for(Agent agent: neighbors)
        {
            System.out.println(agent.getX());
        }
    }
}
