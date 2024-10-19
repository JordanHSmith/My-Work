/**
 * Card.java
 * Jordan Smith
 * CS 231
 * Project 01
 * 02/15/22
 */

public class Card
{
    //Simulates a card with a certain value
    private int cardVal;

    public Card()
    {
        //Constructor for Card
        int randVal = (int)(Math.random() * 10)+2;
        cardVal = randVal;
    }
    public Card(int v)
    {
        //(int) -> (None)
        //Assigns cardVal an inputted value v
        cardVal = v;
    }
    public int getValue()
    {
        //(None) -> (int)
        //returns cardVal
        return(cardVal);
    }
    public String toString()
    {
        //(None) -> (String)
        //Neatly returns the value of the card
        return "The card's value is " + cardVal + ".";
    }

    public static void main(String[] args)
    {
        //tests the Card functions
        Card card1 = new Card();
        System.out.println(card1.toString());
        Card card2 = new Card(3);
        System.out.print("Specificied card value: 3. ");
        System.out.println(card2.toString());
    }
}
