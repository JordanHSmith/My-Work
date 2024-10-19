/*
Jordan Smith
04/04/22
CheckoutAgent.java
CS231
Section C
Project 6
*/

import java.awt.*;

public class CheckoutAgent
{
    //Simulates a person checking out items
    private int xPos;
    private int yPos;
    private int length;
    private MyQueue<Customer> customers;

    public CheckoutAgent(int x, int y)
    {
        //Constructor for CheckoutAgent
        xPos = x;
        yPos = y;
        customers = new MyQueue<Customer>();
    }

    public void addCustomerToQueue(Customer c)
    {
        //adds the customer c to the queue of customers
        customers.offer(c);
        length += c.getNumItems();
    }

    public int getNumItems()
    {
        return length;
    }

    public int getNumInQueue()
    {
        //returns the size of the customers
        return customers.size();
    }

    public void draw(Graphics g)
    {
        //draws the checkout counter
        Color red = new Color(255,0,0);
        g.setColor(red);
        g.fillRect(xPos, yPos-(10*getNumInQueue()), 10, 10*getNumInQueue());
    }

    public void updateState(Landscape scape)
    {
        //Increments the timer for all customers and makes them give up an item
        int counter = 0;
        for(Customer customer: customers)
        {
            customer.incrementTime();
            //Checks if the customer is the first one in line
            if(counter == 0)
            {
                customer.giveUpItem();
                //Removes first customer if it has no items left
                if(customer.getNumItems() == 0)
                {
                    customers.poll();
                    scape.addFinishedCustomer(customer);
                }
            }
            counter = 1;
        }
    }

    public static void main(String[] args)
    {
        CheckoutAgent testcheckoutAgent = new CheckoutAgent(200, 200);
        System.out.println("This value should be: 0 . It is: " + testcheckoutAgent.getNumInQueue() + ".");
        System.out.println("This value should be: 0 . It is: " + testcheckoutAgent.getNumItems() + ".");
    }
}
