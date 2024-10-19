/*
Jordan Smith
03/18/22
SocialAgentSimulation.java
Section C
Project 5
CS 231
*/
import java.util.Random;
public class AntiSocialAgentSimulation
{
    //Simulates social agent interaction
    public static void main(String[] args) throws InterruptedException
    {
        //Creates many social agents and then updates their location and coloring
        Landscape scape = new Landscape(500,500);
        Random gen = new Random();

        for(int i=0;i<200;i++) {
            scape.addAgent( new AntiSocialAgent( gen.nextDouble() * scape.getWidth(),gen.nextDouble() * scape.getHeight(),60) );
        }

        LandscapeDisplay display = new LandscapeDisplay(scape);
        display.repaint();

        for (int i = 0; i < 20; i++)
        {
            scape.updateAgents();
            display.repaint();
            Thread.sleep(250);
        }
    }
}
