/**
 * Hand.java
 * Jordan Smith
 * CS 231
 * Project 01
 * 02/15/22
 */

import java.util.ArrayList;

public class Hand
{
    //Simulates a hand of cards
    private ArrayList<Card> hand;
        
    public Hand()
    {
        //Constructor for Hand
        hand = new ArrayList<Card>();
    }

    public void reset()
    {
        //makes the hand empty
        hand.clear();
    }

    public void add(Card card)
    {
        //(Card) -> (None)
        //adds a specified card
        hand.add(card);
    }

    public int size()
    {
        //(None) -> (int)
        //returns the number of cards in hand
        return hand.size();
    }

    public Card getCard(int i)
    {
        //(int) -> (Card)
        //returns the card at index i
        return hand.get(i);
    }

    public int getTotalValue()
    {
        //(None) -> (int)
        //returns the sum value of all the values of the cards in hand
        int sum = 0;
        for(Card card : hand)
        {
            sum += card.getValue();
        }
        return sum;
    }

    public String toString()
    {
        //(None) -> (String)
        //Neatly returns the number of card in hand and the sum of their values
        return "Your hand has " + hand.size() + " cards, the total value of which is " + getTotalValue() + ".";
    }

    public static void main(String[] args)
    {
        //tests Hand methods
        Card card1 = new Card();
        Card card2 = new Card();
        Hand hand1 = new Hand();
        System.out.println(hand1.toString());
        hand1.add(card1);
        hand1.add(card2);
        System.out.println(hand1.toString());
    }
}
