/*
Jordan Smith
05/13/22
AscendingString.java
CS231
Section C
Project 10
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
