/*
Jordan Smith
04/04/22
Landscape.java
CS231
Section C
Project 6
*/

import java.util.ArrayList;
import java.awt.*;

public class Landscape
{
    //Simulates a landscape with many customers
    int width;
    int height;
    ArrayList<CheckoutAgent> checkoutAgents;
    LinkedList<Customer> doneCustomers;

    public Landscape(int w, int h, ArrayList<CheckoutAgent> checkouts)
    {
        //Constructor for Landscape class
        width = w;
        height = h;
        checkoutAgents = checkouts;
        doneCustomers = new LinkedList<Customer>();
    }

    public int getHeight()
    {
        //returns the height of the landscape
        return height;
    }

    public int getWidth()
    {
        //returns the width of the landscape
        return width;
    }

    public String toString()
    {
        //returns a String stating the number of checkout agents and customers that are done
        return "There are " + checkoutAgents.size() + " checkouts and " + doneCustomers.size() + " customers that are done checking out.";
    }

    public void addFinishedCustomer(Customer c)
    {
        //adds a customer to the list of those done checking out
        doneCustomers.addFirst(c);
    }

    public void draw(Graphics g)
    {
        //draws each agent
        for(CheckoutAgent checkoutAgent: checkoutAgents)
        {
            checkoutAgent.draw(g);
        }
    }

    public void updateCheckouts()
    {
        //updates each agent
        for(CheckoutAgent checkoutAgent: checkoutAgents)
        {
            checkoutAgent.updateState(this);
        }
    }

    public void printFinishedCustomerStatistics()
    {
        //Prints out the average time it took each agent to check out and the corresponding standard deviation
        int sum = 0;
        double avg = 0;
        double stdDev = 0;


        for(Customer customer: doneCustomers)
        {
            sum += customer.getTime();
        }

        avg = sum / doneCustomers.size();

        for(Customer customer: doneCustomers)
        {
            stdDev += Math.pow(customer.getTime() - avg, 2);
        }

        stdDev = Math.sqrt(stdDev / doneCustomers.size());

        System.out.println("The average time it took for a customer to finish was " + 
        avg + ", and the standard deviation is " + stdDev + ".");
    }

    public static void main(String[] args)
    {
        ArrayList<CheckoutAgent> checkouts = new ArrayList<CheckoutAgent>();
        CheckoutAgent checkoutAgent1 = new CheckoutAgent(10, 10);
        CheckoutAgent checkoutAgent2 = new CheckoutAgent(20, 20);
        checkouts.add(checkoutAgent1);
        checkouts.add(checkoutAgent2);
        Landscape testLandscape = new Landscape(200, 200,checkouts);
        System.out.println("This value should be: 200 . It is: " + testLandscape.getWidth() + ".");
        System.out.println("This value should be: 200 . It is: " + testLandscape.getHeight() + ".");
        System.out.println(testLandscape.toString());
    }
}
