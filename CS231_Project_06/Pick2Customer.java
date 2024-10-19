/*
Jordan Smith
04/04/22
Pick2Customer.java
CS231
Section C
Project 6
*/

import java.util.ArrayList;

public class Pick2Customer extends Customer
{
    //Simulares a customer who picks the shortest of two random lines
    public Pick2Customer(int numItems)
    {
        //Constructor for Pick2Customer
        super(numItems,2);
    }

    public int chooseLine(ArrayList<CheckoutAgent> checkouts)
    {
        //Returns the index of the shorter of two randomly selected lines
        CheckoutAgent[] checkoutArray = new CheckoutAgent[checkouts.size()];
        
        int counter = 0;
        for(CheckoutAgent checkout: checkouts)
        {
            checkoutArray[counter] = checkout;
            counter++;
        }

        int randIndex1 = (int)(Math.random() * checkoutArray.length);
        int randIndex2 = (int)(Math.random() * checkoutArray.length);

        //Makes it so that random lines cannot be the same;
        while(randIndex1 == randIndex2)
        {
            randIndex2 = (int)(Math.random() * checkoutArray.length);
        }

        CheckoutAgent randomCheckout1 = checkoutArray[randIndex1];
        CheckoutAgent randomCheckout2 = checkoutArray[randIndex2];

        if(randomCheckout1.getNumInQueue() < randomCheckout2.getNumInQueue())
        {
            return randIndex1;
        }
        else
        {
            return randIndex2;
        }
    }

    public static void main(String[] args)
    {
        Pick2Customer testCustomer = new Pick2Customer(10);
        ArrayList<CheckoutAgent> checkouts = new ArrayList<CheckoutAgent>();
        CheckoutAgent checkoutAgent1 = new CheckoutAgent(10, 10);
        CheckoutAgent checkoutAgent2 = new CheckoutAgent(20, 20);
        CheckoutAgent checkoutAgent3 = new CheckoutAgent(30, 30);
        checkouts.add(checkoutAgent1);
        checkouts.add(checkoutAgent2);
        checkouts.add(checkoutAgent3);
        System.out.println("The shoter random checkout is: " + testCustomer.chooseLine(checkouts));
        System.out.println("The shoter random checkout is: " + testCustomer.chooseLine(checkouts));
        System.out.println("The shoter random checkout is: " + testCustomer.chooseLine(checkouts));
        System.out.println("The shoter random checkout is: " + testCustomer.chooseLine(checkouts));
    }
}
