/*
Jordan Smith
04/04/22
PickyCustomerSimulation.java
CS231
Section C
Project 6
*/

import java.util.ArrayList;

public class RandomCustomer extends Customer
{
    //Simulates a customer who picks a ranodm checkout line
    public RandomCustomer(int numItems)
    {
        //Constructor for RandomCustomer
        super(numItems, 1);
    }

    public int chooseLine(ArrayList<CheckoutAgent> checkouts)
    {
        //returns a random index of one of the checkouts
        return (int)(Math.random() * checkouts.size());
    }

    public static void main(String[] args)
    {
        RandomCustomer testCustomer = new RandomCustomer(10);
        ArrayList<CheckoutAgent> checkouts = new ArrayList<CheckoutAgent>();
        CheckoutAgent checkoutAgent1 = new CheckoutAgent(10, 10);
        CheckoutAgent checkoutAgent2 = new CheckoutAgent(20, 20);
        CheckoutAgent checkoutAgent3 = new CheckoutAgent(30, 30);
        checkouts.add(checkoutAgent1);
        checkouts.add(checkoutAgent2);
        checkouts.add(checkoutAgent3);
        System.out.println("The random index is: " + testCustomer.chooseLine(checkouts));
        System.out.println("The random index is: " + testCustomer.chooseLine(checkouts));
        System.out.println("The random index is: " + testCustomer.chooseLine(checkouts));
    }
}
