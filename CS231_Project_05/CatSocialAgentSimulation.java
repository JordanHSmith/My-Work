/*
Jordan Smith
02/21/22
CatSocialAgentSimulation.java
Section C
Project 2
CS 231
*/

import java.util.Random;

public class CatSocialAgentSimulation
{
    //Creates a simulation for the social agents
    public static void main(String[] args) throws InterruptedException
    {
        //Creates catSocialAgents and updates their positions
        Landscape scape = new Landscape(500,500);
        Random gen = new Random();

        for(int i=0;i<100;i++) {
            scape.addAgent( new CatSocialAgent( gen.nextDouble() * scape.getWidth(),gen.nextDouble() * scape.getHeight(),1) );
        }
        for(int i=0;i<100;i++) {
            scape.addAgent( new CatSocialAgent( gen.nextDouble() * scape.getWidth(),gen.nextDouble() * scape.getHeight(),2) );
        }

        LandscapeDisplay display = new LandscapeDisplay(scape);

        display.repaint();

        for (int i = 0; i < 200; i++)
        {
            scape.updateAgents();
            display.repaint();
            Thread.sleep(250);
        }
    }
}
