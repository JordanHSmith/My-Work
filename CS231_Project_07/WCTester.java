/*
Jordan Smith
04/11/22
AscendingString.java
CS231
Section C
Project 7
*/

import java.io.IOException;


public class WCTester
{
    public static void main(String[] args) throws IOException
    {
        //Test Code
        WordCounter wordCounterTest = new WordCounter();
        wordCounterTest.analyze("counttest.txt");
        wordCounterTest.writeWordCountFile("counts_ct.txt");
        wordCounterTest.readWordCountFile("counts_ct.txt");
        wordCounterTest.writeWordCountFile("counts_ct_v2.txt");
    }
}
