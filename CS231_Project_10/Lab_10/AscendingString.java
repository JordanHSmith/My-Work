package Lab_10;

/*
Jordan Smith
04/11/22
AscendingString.java
CS231
Section C
Project 7
*/

import java.util.Comparator;

public class AscendingString implements Comparator<Vertex>
{
    //Allows String values to be comparared to one another
    public int compare(Vertex v1, Vertex v2)
    {
        return v1.compareTo(v2);
    }
}
