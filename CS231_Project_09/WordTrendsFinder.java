/*
Jordan Smith
04/25/22
WordTrendsFinder.java
CS231
Section C
Project 9
To run in terminal type: java WordTrendsFinder reddit_comments_ 2008 2015 <words>
*/

import java.util.ArrayList;

public class WordTrendsFinder
{
    //Creates a word finder
    static void findWords(String[] args, int numFiles, CommonWordFinder wordFinder)
    {
        //Stores an ArrayList of ArrayLists, which each holds key value pairs of each word and its frequency for a given year
        ArrayList<ArrayList<KeyValuePair<String,Float>>> KeyValuePairsYears = new ArrayList<ArrayList<KeyValuePair<String,Float>>>();
        for(int i=0; i<numFiles; i++)
        {
            ArrayList<KeyValuePair<String,Float>> KVPairs = new ArrayList<KeyValuePair<String,Float>>();
            String baseFile = args[0];
            String fileNumBegin = args[1];
            int fileNumBeginInt = Integer.valueOf(fileNumBegin);
            String[] fileNums = new String[numFiles];
            fileNums[i] = String.valueOf(fileNumBeginInt+i);
            String currentFile = baseFile + fileNums[i] + ".txt";
            wordFinder.readWords(currentFile);
            for(int j=3; j<args.length; j++)
            {
                KeyValuePair<String,Float> KVPair = new KeyValuePair<String,Float>(args[j],wordFinder.getFrequency(args[j]));
                KVPairs.add(KVPair);
            }
            KeyValuePairsYears.add(KVPairs);
        }

        for(int i=0; i<args.length-3; i++) //iterates through each word
        {
            System.out.print(args[3+i] + " ");
            for(int j=0; j<numFiles; j++) //iterates through each file
            {
                System.out.print(KeyValuePairsYears.get(j).get(i).getValue() + " ");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args)
    {
        //Code to run WordFinder
        CommonWordFinder wordFinder = new CommonWordFinder("bst");
        String fileNumBegin = args[1];
        String fileNumEnd = args[2];
        int numFiles = Integer.valueOf(fileNumEnd) - Integer.valueOf(fileNumBegin) + 1;

        System.out.println("Interesting words");
        findWords(args,numFiles,wordFinder);
    }
}
