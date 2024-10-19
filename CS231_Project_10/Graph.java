/*
Jordan Smith
05/13/22
Graph.java
CS231
Section C
Project 10
*/

import java.util.ArrayList;
import java.util.*;

public class Graph
{
    //Provides functions to make and manipulate a graph
    private ArrayList<Vertex> vertices;

    public Graph()
    {
        //Default constructor for Graph
        vertices = new ArrayList<Vertex>();
    }

    public ArrayList<Vertex> getVertices()
    {
        //returns the vertices in the graph
        return vertices;
    }

    public int vertexCount()
    {
        //returns the number of vertices in the graph
        return vertices.size();
    }

    public boolean inGraph(Vertex query)
    {
        //returns true if query is in the graph and false otherwise
        for(Vertex vertex: vertices)
        {
            if(vertex == query)
            {
                return true;
            }
        }
        return false;
    }

    public void addUniEdge(Vertex v1, Vertex v2)
    {
        //adds a unidirectional edge between two vertices
        if(!this.inGraph(v1))
        {
            vertices.add(v1);
        }
        if(!this.inGraph(v2))
        {
            vertices.add(v2);
        }
        v2.connect(v1);
    }

    public void addBiEdge(Vertex v1, Vertex v2)
    {
        //adds a bidirectional edge between two vertices
        if(!this.inGraph(v1))
        {
            vertices.add(v1);
        }
        if(!this.inGraph(v2))
        {
            vertices.add(v2);
        }
        v1.connect(v2);
        v2.connect(v1);
    }

    public void shortestPath(Vertex v0)
    {
        //Prepares vertices for the algorithm to work
        for(Vertex vertex: vertices)
        {
            vertex.setVisited(false);
            vertex.setCost(10000000);
            vertex.setParent(null);
        }

        PriorityQueue<Vertex> q = new PriorityQueue<Vertex>();

        //Makes v0 the starting vertex
        v0.setCost(0);
        q.add(v0);

        while(q.size() != 0)
        {
            //Makes it so that the graph knows the vertex has already been visited
            Vertex v = q.remove();
            if(!v.wasVisited())
            {
                v.setVisited(true);
            }

            //Appropriattely updates the costs of each of the neighboring vertices
            for(Vertex w: v.getNeighbors())
            {
                double dist = v.distance(w);
                if(w.wasVisited() == false && v.getCost() + dist < w.getCost())
                {
                    w.setCost(v.getCost() + dist);
                    w.setParent(v);
                    q.add(w);
                }
            }
        }
    }

    public static void main(String[] args)
    {
        //Test code for the Graph class
        Graph testGraph = new Graph();

        Vertex vertex1 = new Vertex(20,20,false);
        Vertex vertex2 = new Vertex(25,25,false);
        Vertex vertex3 = new Vertex(15,20,true);
        Vertex vertex4 = new Vertex(20,15,true);
        Vertex vertex5 = new Vertex(30,30,false);

        testGraph.addUniEdge(vertex1, vertex2);
        testGraph.addUniEdge(vertex1, vertex3);
        testGraph.addUniEdge(vertex3, vertex4);
        testGraph.addUniEdge(vertex4, vertex5);
        testGraph.addUniEdge(vertex2, vertex5);

        for(Vertex v: testGraph.vertices)
        {
            System.out.println(v);
        }
        testGraph.shortestPath(vertex5);
        for(Vertex v: testGraph.vertices)
        {
            System.out.println(v);
        }
    }
}
