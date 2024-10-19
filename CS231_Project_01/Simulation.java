/**
 * Simulation.java
 * Jordan Smith
 * CS 231
 * Project 01
 * 02/15/22
 */

public class Simulation
{
    //Simulates multiple rounds of blackjack
    public static void main(String[] args)
    {
        //runs 1000 rounds of blackjack and prints the results
        Blackjack blackjack = new Blackjack(15);
        for(int i=0; i<1000; i++)
        {
            blackjack.game(false);
        }
        System.out.println("The player won " + blackjack.playerScore + " games, and the dealer won " + blackjack.dealerScore
        + " games. " + blackjack.pushCounter + " of the games were ties. This means that the player won " +
         blackjack.playerScore/10 + " percent of the games, the dealer won " + blackjack.dealerScore/10 + 
         " percent of the games, and " + blackjack.pushCounter/10 + " percent of the games were ties.");
    }
}
