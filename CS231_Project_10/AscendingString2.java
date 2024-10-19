/*
Jordan Smith
05/13/22
AscendingString2.java
CS231
Section C
Project 10
*/

import java.util.Comparator;

public class AscendingString2 implements Comparator<String>
{
    //Allows Vertex values to be comparared to one another
    public int compare(String v1, String v2)
    {
        return v1.compareTo(v2);
    }
}