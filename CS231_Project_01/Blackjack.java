/**
 * Blackjack.java
 * Jordan Smith
 * CS 231
 * Project 01
 * 02/15/22
 */

public class Blackjack
{
    //Simulates a round of blackjack
    Deck deck;
    Hand playerHand;
    Hand dealerHand;
    int playerScore;
    int dealerScore;
    int pushCounter;
    int reshuffleCutoff;

    public Blackjack(int reshuffleCutoff)
    {
        //Constructor for Blackjack
        deck = new Deck();
        playerHand = new Hand();
        dealerHand = new Hand();
        playerScore = 0;
        dealerScore = 0;
        pushCounter = 0;
        this.reshuffleCutoff = reshuffleCutoff;
        reset();
    }

    public void reset()
    {
        //sets up a new round of blackjack
        if(deck.size() < reshuffleCutoff)
        {
            deck = new Deck();
            deck.shuffle();
        }
        else
        {
            playerHand = new Hand();
            dealerHand = new Hand();
        }
    }

    public void deal()
    {
        //gives botht the player and the dealer two cards
        Card playerCard1 = new Card();
        Card playerCard2 = new Card();
        Card dealerCard1 = new Card();
        Card dealerCard2 = new Card();

        playerHand.add(playerCard1);
        playerHand.add(playerCard2);
        dealerHand.add(dealerCard1);
        dealerHand.add(dealerCard2);
    }

    public boolean playerTurn()
    {
        //Has the player play until he or she busts or reaches a sum of 17
        while(playerHand.getTotalValue() < 17) // used to be <16
        {
            Card card = new Card();
            playerHand.add(card);
            if(playerHand.getTotalValue() > 21)
            {
                return false;
            }
        }
        return true;
    }

    public boolean dealerTurn()
    {
        //Has the dealer play until he or she busts or reaches a sum of 17
        while(dealerHand.getTotalValue() < 17)
        {
            Card card = new Card();
            dealerHand.add(card);
            if(dealerHand.getTotalValue() > 21)
            {
                return false;
            }
        }
        return true;
    }

    public void setReshuffleCutoff(int cutoff)
    {
        //(int) -> (None)
        //sets the reshuffle cutoff to a specified number
        reshuffleCutoff = cutoff;
    }

    public int getReshuffleCutoff()
    {
        //(None) -> (int)
        //returns the reshuffle cutoff
        return reshuffleCutoff;
    }

    public String toString()
    {
        //(None) -> (String)
        //neatly returns the raw numbers of wins and draws as well as their related percentages
        return "The player has " + playerHand.size() + " cards, the total of which is " + playerHand.getTotalValue() +
        ". The dealer has " + dealerHand.size() + " cards, the total of which is " + dealerHand.getTotalValue() + 
        ". The player's score is " + playerScore + ", and the dealer's score is " + dealerScore + ".";
    }

    public int game(boolean verbose)
    {
        //(boolean) -> (int)
        //Simulates a round of blackjack, returning a number based on the winner
        reset();
        deal();
        if(verbose)
        {
            System.out.println(toString());
        }
        if(!dealerTurn()) //used to be !playerTurn()
        {
            playerScore++; //used to be dealerScore++;
            if(verbose)
            {
                System.out.println(toString());
            }
            return -1;
        }
        else if(!playerTurn()) //used to be !dealerTurn()
        {
            dealerScore++; //used to be playerScore
            if(verbose)
            {
                System.out.println(toString());
            }
            return 1;
        }
        else if(playerHand.getTotalValue() > dealerHand.getTotalValue())
        {
            playerScore++;
            if(verbose)
            {
                System.out.println(toString());
            }
            return 1;
        }
        else if(playerHand.getTotalValue() < dealerHand.getTotalValue())
        {
            dealerScore++;
            if(verbose)
            {
                System.out.println(toString());
            }
            return -1;
        }
        else
        {
            pushCounter++;
            if(verbose)
            {
                System.out.println(toString());
            }
            return 0;
        }
    }

    public static void main(String[] args)
    {
        //tests Blackjack methods
        Blackjack blackjack = new Blackjack(15);
        System.out.println(blackjack.game(true));
        System.out.println(blackjack.game(true));
        System.out.println(blackjack.game(true));
    }
}
