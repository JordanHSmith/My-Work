/*
Jordan Smith
03/11/22
Simulation.java
CS231 B
Project 03/04
*/

public class Simulation
{
    //Simulates multiple rounds of trying to solve a Sudoku Board

    public static String simulation(int numLocked, int N)
    {
        //(int,int) -> (str)
        /*
        Returns a string stating the number of successful solved boards for a given number
        of locked cells out of the number of runs
        */
        int numSolved = 0;
        for(int i=0; i<N; i++)
        {
            //Creates a Sudoke board and increments numSolved if it can be solved
            Sudoku_Extension sudokuBoard = new Sudoku_Extension(numLocked);
            if(sudokuBoard.solve(numLocked))
            {
                numSolved++;
            }
        }
        String str = "Out of " + N + " boards with " + numLocked + " initial values, " + numSolved + " were solved.";
        return str;
    }

    public static void main(String[] args)
    {
        //Test code
        int locked = Integer.parseInt(args[0]);
        int numRuns = Integer.parseInt(args[1]);
        System.out.println(simulation(locked, numRuns));
    }
}
