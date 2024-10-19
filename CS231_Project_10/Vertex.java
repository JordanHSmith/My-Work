/*
Jordan Smith
05/13/22
Vertex.java
CS231
Section C
Project 10
*/

import java.util.ArrayList;

public class Vertex implements Comparable<Vertex>
{
    //Provides functions to create and manipulate a vertex
    private ArrayList<Vertex> adjacentVertices;
    private int xPos;
    private int yPos;
    private boolean isVisible;
    private double distFromRootNode;
    private boolean wasVisited;
    private Vertex parent;

    public Vertex(int x, int y, boolean visibility)
    {
        //Constructor for Vertex
        adjacentVertices = new ArrayList<Vertex>();
        xPos = x;
        yPos = y;
        isVisible = visibility;
        parent = null;
        distFromRootNode = 0;
    }

    public double getCost()
    {
        //returns the cost (fistance from the root node) of the vertex
        return distFromRootNode;
    }

    public void setCost(double cost)
    {
        //sets the cost
        distFromRootNode = cost;
    }

    public void setParent(Vertex par)
    {
        //sets the parent
        parent = par;
    }

    public double distance(Vertex other)
    {
        //calculates the distance between two vertices
        return Math.sqrt(Math.pow(other.xPos-this.xPos,2)+(Math.pow(other.yPos-this.yPos,2)));
    }

    public void connect(Vertex other)
    {
        //connects two vertices unidimensionally
        this.adjacentVertices.add(other);
    }

    public Vertex getNeighbor(int x, int y)
    {
        //returns the neighbor at location (x,y) or null if not applicable
        for(Vertex vertex: adjacentVertices)
        {
            if(vertex.xPos == x && vertex.yPos == y)
            {
                return vertex;
            }
        }
        return null;
    }

    public ArrayList<Vertex> getNeighbors()
    {
        //returns all the vertices adjacent to this vertex
        return adjacentVertices;
    }

    public int numNeighbors()
    {
        //returns the number of neighboring vertices
        return adjacentVertices.size();
    }

    public String toString()
    {
        //returns a String that clearly gives the number of neighbors, cost, and marked status of the vertex
        return "This vertex has " + numNeighbors() + " neighbors, has a cost of " + distFromRootNode +
        ", and it is " + wasVisited + " that it has been visited.";
    }

    public int compareTo(Vertex other)
    {
        //Compares distance of this node against that of another
        if(this.distFromRootNode < other.distFromRootNode)
        {
            return -1;
        }
        else if(this.distFromRootNode > other.distFromRootNode)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }

    public void setMarked(boolean mark)
    {
        //sets whether or not the vertex was already visited
        wasVisited = mark;
    }

    public boolean getMarked()
    {
        //returns whether or not the vertex was visited
        return wasVisited;
    }

    public void setDistance(double dist)
    {
        //sets the distance of this vertex from root node
        distFromRootNode = dist;
    }

    public double getDistance()
    {
        //returns this vertex's distance from root node
        return distFromRootNode;
    }

    public boolean wasVisited()
    {
        //returns whether or not this vertex was visited
        return wasVisited;
    }

    public void setVisited(boolean visited)
    {
        //returns whether or not the vertex was visited
        wasVisited = visited;
    }

    public static void main(String[] args)
    {
        //Test code for Vertex class
        Vertex vertex1 = new Vertex(20,20,false);
        Vertex vertex2 = new Vertex(25,25,false);
        Vertex vertex3 = new Vertex(15,20,true);
        Vertex vertex4 = new Vertex(20,15,true);

        vertex1.connect(vertex2);
        vertex1.connect(vertex3);
        vertex1.connect(vertex4);
        System.out.println("Should be 3. NumNeighbors: " + vertex1.numNeighbors());
        System.out.println("Should be 0. NumNeighbors: " + vertex4.numNeighbors());
        vertex4.connect(vertex1);
        System.out.println("Should be 1. NumNeighbors: " + vertex4.numNeighbors());
        System.out.println(vertex1.getNeighbors());
        System.out.println("Should be 25,25: GetNeighbor: " + vertex1.getNeighbor(25,25).xPos + "," + vertex1.getNeighbor(25,25).yPos);
        System.out.println("Should be 5.0. Distance: " + vertex1.distance(vertex4));
        System.out.println(vertex4.distFromRootNode);
    }
}