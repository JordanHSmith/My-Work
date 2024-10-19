/**
 * Deck.java
 * Jordan Smith
 * CS 231
 * Project 01
 * 02/15/22
 */

import java.util.ArrayList;

public class Deck
{
    //Simulates a deck of cards
    private ArrayList<Card> deck;

    public Deck()
    {
        //Constructor for Deck
        deck = new ArrayList<Card>();
        build();
    }

    public void build()
    {
        //Makes a standard deck
        //Loops make 4 of each of the 14 kinds of cards in a deck
        for(int i=1; i<14*6; i++) //used to be i<14
        {
            for(int j=0; j<4; j++)
            {
                //Checks to see if the card value is one of the unique ones or repeated
                if(i < 10)
                {
                    Card card = new Card(i);
                    deck.add(card);
                }
                else
                {
                    Card card = new Card(10);
                    deck.add(card);
                }
            }
        }     
    }

    public int size()
    {
        //(None) -> (int)
        //returns the number of cards in the deck
        return deck.size();
    }

    public Card deal()
    {
        //(None) -> (Card)
        //returns the card at the top of the deck and removes it from the deck
        Card topCard = deck.get(0);
        deck.remove(0);
        return topCard;
    }

    public Card pick(int i)
    {
        //(int) -> (Card)
        //returns the Card object at index i and removes it from the deck
        Card topCard = deck.get(i);
        deck.remove(i);
        return topCard;
    }

    public void shuffle()
    {
        //shuffles the deck
        ArrayList<Card> tempDeck = new ArrayList<Card>();
        tempDeck = deck;
        for(int i=tempDeck.size()-1; i>0; i--)
        {
            //sets each value of the copy of the original deck to a random location in the original deck
            deck.set(i,tempDeck.get((int)(Math.random() * tempDeck.size())));
        }
    }

    public String toString()
    {
        //(None) -> (String)
        //Neatly returns the values of the cards in order
        ArrayList<Integer> deckNums = new ArrayList<Integer>();
        for(Card card: deck)
        {
            deckNums.add(card.getValue());
        }
        return "The cards of the deck in order are: " + deckNums;

    }

    public static void main(String[] args)
    {
        //tests Deck methods
        Deck deck1 = new Deck();
        System.out.println(deck1.toString());
        deck1.shuffle();
        System.out.println(deck1.toString());
    }
}
