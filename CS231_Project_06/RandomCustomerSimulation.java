/*
Jordan Smith
04/04/22
RandomCustomerSimulation.java
CS231
Section C
Project 6
*/

import java.util.Random;
import java.util.ArrayList;

public class RandomCustomerSimulation
{
    //Simulates many customers randomly picking a checkout line
    public static void main(String[] args) throws InterruptedException {
        Random gen = new Random();
        ArrayList<CheckoutAgent> checkouts = new ArrayList<CheckoutAgent>(5);

        for(int i=0;i<5;i++) {
            CheckoutAgent checkout = new CheckoutAgent( i*100+50, 480 );
            checkouts.add( checkout );
        }
        Landscape scape = new Landscape(500,500, checkouts);
        LandscapeDisplay display = new LandscapeDisplay(scape);
        
        for (int j = 0; j < 1000; j++) {
            if(j % 100 == 0 && j != 0)
            {
                scape.printFinishedCustomerStatistics();
            }
            Customer cust = new RandomCustomer(1+gen.nextInt(7));
            int choice = cust.chooseLine( checkouts );
            checkouts.get(choice).addCustomerToQueue( cust );
            scape.updateCheckouts();
            display.repaint();
            Thread.sleep( 250 );
        }
    }
}
