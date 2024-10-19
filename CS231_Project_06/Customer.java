/*
Jordan Smith
04/04/22
Customer.java
CS231
Section C
Project 6
*/

import java.util.ArrayList;

public abstract class Customer
{
    //Simulates a generic customer
    int numItems;
    int timeStep;

    public Customer(int numItems)
    {
        //default constructor for Customer
        this.numItems = numItems;
        timeStep = 0;
    }

    public Customer(int numItems, int timeSteps)
    {
        //constructor for customer that specified intial timestep
        this.numItems = numItems;
        timeStep = timeSteps;
    }

    public void incrementTime()
    {
        //increments timeStep
        timeStep++;
    }

    public int getTime()
    {
        //returns timeStep
        return timeStep;
    }

    public void giveUpItem()
    {
        //decrements the number of items the customer has
        numItems--;
    }

    public int getNumItems()
    {
        // returns the number of items the customer has
        return numItems;
    }

    //abstract class to be implemented in other classes
    public abstract int chooseLine(ArrayList<CheckoutAgent> checkouts);
}
