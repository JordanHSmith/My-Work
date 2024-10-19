/*
Jordan Smith
04/11/22
AscendingString.java
CS231
Section C
Project 7
*/

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;
import java.io.FileWriter;

public class WordCounter
{
    //Creates a word counter
    private BSTMap<String, Integer> bstMap;
    private int wordCount;

    public WordCounter()
    {
        //Constructor for word counter
        bstMap = new BSTMap<String, Integer>(new AscendingString());
        wordCount = -3;
    }

    public void analyze(String filename)
    {
        //Populates a BSTMap
        bstMap = new BSTMap<String, Integer>(new AscendingString());
        wordCount = -3;
        try
        {
            FileReader fileReader = new FileReader(filename);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            //Gets individual line of file
            String line = bufferedReader.readLine();
            while(line != null)
            {
                //Gets individual word
                String[] words = line.split("[^a-zA-Z0-9']");
                for (int i = 0; i < words.length; i++)
                {
                    wordCount++;
                    String word = words[i].trim().toLowerCase();
                    //Check for if the word is blank
                    if(word.length() != 0)
                    {
                        //Updates word counter for the word
                        if(bstMap.containsKey(word))
                        {
                            bstMap.put(word,bstMap.get(word)+1);
                        }
                        else
                        {
                            bstMap.put(word,1);
                        }
                    }
                }
                //continues iteration to next line
                line = bufferedReader.readLine();
            }
        }
        catch(FileNotFoundException ex)
        {
            System.out.println("Board.read():: unable to open file " + filename );
        }
        catch(IOException ex)
        {
            System.out.println("Board.read():: error reading file " + filename);
        }
    }

    public int getTotalWordCount()
    {
        //return wordCount
        return wordCount;
    }

    public int getUniqueWordCount()
    {
        //returns the number of nodes in the BST
        return bstMap.size();
    }

    public double getFrequency(String word)
    {
        //Returns frequency with which a word occurs
        double tempWordAmount = bstMap.get(word);
        return tempWordAmount / wordCount;
    }

    public void writeWordCountFile(String filename) throws IOException
    {
        //Writes the contents of a BSTMap to a txt file
        String str = "";
        str += "totalWordCount: " + wordCount + "\n";
        ArrayList<KeyValuePair<String,Integer>> entrySetTest = bstMap.entrySet();
        System.out.println("EntrySet Size: " + entrySetTest.size());
        for(KeyValuePair<String,Integer> entry: entrySetTest)
        {
            System.out.println(entry.getKey() + " " + entry.getValue());
            str += entry.getKey() + " " + entry.getValue() + "\n";
        }
        FileWriter fw = new FileWriter(filename);
        fw.write(str);
        fw.close();
    }

    public void readWordCountFile(String filename)
    {
        //reads the contents of a txt file 
        try
        {
            FileReader fileReader = new FileReader(filename);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String line = bufferedReader.readLine();

            line = bufferedReader.readLine();
            while(line != null)
            {
                String[] words = line.split(" ");
                for (int i = 0; i < words.length; i++)
                {
                    String word = words[i].trim().toLowerCase();
                }
                line = bufferedReader.readLine();
            }
        }
        catch(FileNotFoundException ex)
        {
            System.out.println("Board.read():: unable to open file " + filename );
        }
        catch(IOException ex)
        {
            System.out.println("Board.read():: error reading file " + filename);
        }
    }

    //Extension
    public ArrayList<KeyValuePair<String,Integer>> mostCommonWords()
    {
        //returns an arraylist of the most common words in the file
        ArrayList<KeyValuePair<String,Integer>> keyValuePairs = this.bstMap.entrySet();
        ArrayList<KeyValuePair<String,Integer>> mostCommon = new ArrayList<KeyValuePair<String,Integer>>();
        for(KeyValuePair<String,Integer> keyValuePair: keyValuePairs)
        {
            if(keyValuePair.getValue() > (0.01 * getTotalWordCount()))
            {
                mostCommon.add(keyValuePair);
            }
        }
        return mostCommon;
    }

    public static void main(String[] args) throws IOException
    {
        //Commands for making files and calculations
        WordCounter wordCounterTest = new WordCounter();
        long initTime = System.currentTimeMillis();
        wordCounterTest.analyze(args[0]);
        long finalTime = System.currentTimeMillis();
        long timeTaken = finalTime - initTime;
        wordCounterTest.writeWordCountFile(args[1]);
        System.out.println("The time it took to process the file is: " + timeTaken + " milliseconds");
        System.out.println("Unique Word Count: " + wordCounterTest.getUniqueWordCount());
        System.out.println("The most common words and their values in the file are:");
        for(KeyValuePair<String,Integer> keyValuePair: wordCounterTest.mostCommonWords())
        {
            System.out.print("Key: " + keyValuePair.getKey());
            System.out.println(", Value: " + keyValuePair.getValue());
        }

        //Test Code
        // System.out.println("Frequency: " + wordCounterTest.getFrequency("best"));
        // System.out.println("Frequency: " + wordCounterTest.getFrequency("it"));
        // System.out.println("Frequency: " + wordCounterTest.getFrequency("times"));
        // System.out.println("Frequency: " + wordCounterTest.getFrequency("of"));
        // System.out.println("Unique Word Count: " + wordCounterTest.getUniqueWordCount());
        System.out.println("Total Word Count: " + wordCounterTest.getTotalWordCount());


        // WordCounter wordCounterTest = new WordCounter();
        // long initTime = System.currentTimeMillis();
        // wordCounterTest.analyze(args[0]);
        // long finalTime = System.currentTimeMillis();
        // long timeTaken = finalTime - initTime;
        // System.out.println("The time it took to process the file is: " + timeTaken + " milliseconds");

        // System.out.println("Frequency: " + wordCounterTest.getFrequency("best"));
        // System.out.println("Frequency: " + wordCounterTest.getFrequency("it"));
        // System.out.println("Frequency: " + wordCounterTest.getFrequency("times"));
        // System.out.println("Frequency: " + wordCounterTest.getFrequency("of"));
        // System.out.println("Unique Word Count: " + wordCounterTest.getUniqueWordCount());
        // System.out.println("Total Word Count: " + wordCounterTest.getTotalWordCount());
    }

}
