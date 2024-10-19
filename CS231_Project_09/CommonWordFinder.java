/*
Jordan Smith
04/25/22
WordCounter2.java
CS231
Section C
Project 9
*/

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;
import java.io.FileWriter;

class CommonWordFinder
{
    //Creates a word counter
    static MapSet<String,Integer> map;
    int totalWordCount;

    public CommonWordFinder(String dataStructure)
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

    public Float getFrequency(String word)
    {
        //Returns the frequency with which a given word occurs
        float tempWordAmount;
        if(map.get(word) == null)
        {
            tempWordAmount = 0;
        }
        else
        {
            tempWordAmount = map.get(word);
        }
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
        //Returns the depth of a BST and numCollisions of a hashmap
        return map.getDepth();
    }

    public void getCommonWords(int N)
    {
        //Gets the N most common words from the file using a priority queue
        ArrayList<KeyValuePair<String,Integer>> entrySet = map.entrySet();
        ArrayList<Float> frequencyList = new ArrayList<Float>();
        PQHeap<KeyValuePair<String,Float>> heap = new PQHeap(new KVTestComparator());
        for(KeyValuePair<String,Integer> KVPair: entrySet)
        {
            frequencyList.add(getFrequency(KVPair.getKey()));
        }
        for(int i=0; i<entrySet.size(); i++)
        {
            KeyValuePair<String,Float> KVPair = new KeyValuePair<String,Float>(entrySet.get(i).getKey(),frequencyList.get(i));
            heap.add(KVPair);
        }
        for(int i=0; i<N; i++)
        {
            System.out.println(heap.remove());
        }
    }

    public void getHeap()
    {
        //returns the elements of the heap in order of priority
        ArrayList<KeyValuePair<String,Integer>> entrySet = map.entrySet();
        PQHeap<String> heap = new PQHeap(new AscendingString());
        for(KeyValuePair<String,Integer> KVPair: entrySet)
        {
            heap.add(String.valueOf(KVPair.getValue()));
        }
        heap.getHeap();
    }

    public static void main(String[] args)
    {
        //Code for running calculations
        CommonWordFinder wordFinder = new CommonWordFinder("bst");

        int numFiles = args.length;
        int N = Integer.parseInt(args[0]);

        for(int i=1; i<numFiles; i++)
        {
            System.out.println(args[i]);
            wordFinder.readWords(args[i]);
            wordFinder.getCommonWords(N);
        }
    }
}