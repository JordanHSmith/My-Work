/*
Jordan Smith
04/11/22
AscendingString.java
CS231
Section C
Project 7
*/

import java.util.Comparator;

public class AscendingString implements Comparator<String>
{
    //Allows String values to be comparared to one another
    public int compare(String str1, String str2)
    {
        return str1.compareTo(str2);
    }
}
