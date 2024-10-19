/*
Jordan Smith
04/11/22
WordCounter2.java
CS231
Section C
Project 8
*/

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;
import java.io.FileWriter;

class WordCounter2
{
    //Creates a word counter
    MapSet<String,Integer> map;
    int totalWordCount;

    public WordCounter2(String dataStructure)
    {
        //Constructor for word counter that allows one to select which type of
        //map they wish to store the data in
        if(dataStructure == "bst")
        {
            map = new BSTMap<String,Integer>(new AscendingString());
        }
        else
        {
            map = new Hashmap<String,Integer>(new AscendingString());
        }
    }

    public ArrayList<String> readWords(String filename)
    {
        //Populates a map
        ArrayList<String> wordList = new ArrayList<String>();
        map.clear();
        totalWordCount = 0;
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
                    totalWordCount++;
                    String word = words[i].trim().toLowerCase();
                    //Check for if the word is blank
                    if(word.length() != 0)
                    {
                        //Updates word counter for the word
                        if(map.containsKey(word))
                        {
                            wordList.add(word);
                            map.put(word,map.get(word)+1);
                        }
                        else
                        {
                            map.put(word,1);
                        }
                    }
                    else
                    {
                        totalWordCount--;
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
        return wordList;
    }

    public double buildMap(ArrayList<String> words)
    {
        //Builds a map and returns how long it took to do so
        map.clear();
        long initTime = System.nanoTime();
        for(String word: words)
        {
            if(map.get(word) == null)
            {
                map.put(word,1);
            }
            else
            {
                map.put(word,map.get(word)+1);
            }
        }
        long finalTime = System.nanoTime();
        return (finalTime - initTime) / 1000000.00;
    }

    public void clearMap()
    {
        //Resets the map
        map.clear();
    }

    public int totalWordCount()
    {
        //Returns the total word count of the map
        return totalWordCount;
    }

    public int uniqueWordCount()
    {
        //Returns the number of unique words in the map
        return map.size();
    }

    public int getCount(String word)
    {
        //Returns the value associated with a given word
        if(!map.containsKey(word))
        {
            return 0;
        }
        else
        {
            return map.get(word);
        }
    }

    public double getFrequency(String word)
    {
        //Returns the frequency with which a given word occurs
        double tempWordAmount = map.get(word);
        return tempWordAmount / totalWordCount();
    }

    public void writeWordCountFile(String filename) throws IOException
    {
        //Writes the contents of a BSTMap to a txt file
        String str = "";
        str += "totalWordCount: " + totalWordCount + "\n";
        ArrayList<KeyValuePair<String,Integer>> entrySetTest = map.entrySet();
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

    public int getMapDepth()
    {
        return map.getDepth();
    }

    public static void main(String[] args)
    {
        //Code for running calculations
        WordCounter2 wordCounter = new WordCounter2("hashmap");

        ArrayList<String> wordList = wordCounter.readWords(args[0]);
        ArrayList<Double> averageTimes = new ArrayList<Double>();
        for(int i=0; i<5; i++)
        {
            System.out.println("current iteration: " + i);
            averageTimes.add(wordCounter.buildMap(wordList));
        }
        int smallestTimeIndex = 0;
        for(int i=0; i<averageTimes.size(); i++)
        {
            if(averageTimes.get(i) < averageTimes.get(smallestTimeIndex))
            {
                smallestTimeIndex = i;
            }
        }
        averageTimes.remove(smallestTimeIndex);

        int largestTimeIndex = 0;
        for(int i=0; i<averageTimes.size(); i++)
        {
            if(averageTimes.get(i) > averageTimes.get(largestTimeIndex))
            {
                largestTimeIndex = i;
            }
        }
        averageTimes.remove(largestTimeIndex);

        double averageTime = 0.00;
        for(int i=0; i<averageTimes.size(); i++)
        {
            averageTime += averageTimes.get(i);
        }
        averageTime /= 3.00;

        System.out.println("Run Time: " + averageTime);
        System.out.println("NumCollisions: " + wordCounter.getMapDepth());

        //Previous Test Code

        // System.out.println("Run Time: " + averageTime);
        // System.out.println("Total Word Count: " + wordCounter.totalWordCount());
        // System.out.println("Unique Word Count: " + wordCounter.uniqueWordCount());
        // System.out.println("Depth: " + wordCounter.getMapDepth());

        // System.out.println(wordCounter.buildMap(wordList));
        // System.out.println("Word Count: " + wordCounter.totalWordCount());
    }
}