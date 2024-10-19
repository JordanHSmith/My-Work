/*
Jordan Smith
04/04/22
PickyCustomer.java
CS231
Section C
Project 6
*/

import java.util.ArrayList;

public class PickyCustomer extends Customer
{
    //Simulates a customer that always picks the shortest line
    public PickyCustomer(int numItems, int numLines)
    {
        //Constructor for PickyCustomer
        super(numItems, numLines);
    }

    public int chooseLine(ArrayList<CheckoutAgent> checkouts)
    {
        //Returns the index of the shortest line
        CheckoutAgent[] checkoutArray = new CheckoutAgent[checkouts.size()];
        
        //Converts the arraylist into an array
        int counter = 0;
        for(CheckoutAgent checkout: checkouts)
        {
            checkoutArray[counter] = checkout;
            counter++;
        }

        //Finds the shortest line
        int shortest = 10000;
        int shortestIndex = -1;
        for(int i=0; i<checkouts.size(); i++)
        {
            if(checkoutArray[i].getNumInQueue() < shortest)
            {
                shortest = checkoutArray[i].getNumInQueue();
                shortestIndex = i;
            }
        }
        return shortestIndex;
    }

    public static void main(String[] args)
    {
        PickyCustomer testCustomer = new PickyCustomer(10,3);
        ArrayList<CheckoutAgent> checkouts = new ArrayList<CheckoutAgent>();
        CheckoutAgent checkoutAgent1 = new CheckoutAgent(10, 10);
        CheckoutAgent checkoutAgent2 = new CheckoutAgent(20, 20);
        CheckoutAgent checkoutAgent3 = new CheckoutAgent(30, 30);
        checkouts.add(checkoutAgent1);
        checkouts.add(checkoutAgent2);
        checkouts.add(checkoutAgent3);
        System.out.println("This should be 0: " + testCustomer.chooseLine(checkouts));
    }
}
