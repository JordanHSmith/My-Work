/*
Jordan Smith
05/13/22
Test.java
CS231
Section C
Project 10
*/

import java.util.ArrayList;

public class Test
{
    //Used to test Dijkstra's Algorithm and Graph Class
    public static void main(String[] args)
    {
        //Test code that runs the shortestPath method on a graph of 10 vertices twice
        Graph graph = new Graph();
        
        Vertex vertex1 = new Vertex(0,0,false);
        Vertex vertex2 = new Vertex(5,0,false);
        Vertex vertex3 = new Vertex(0,5,false);
        Vertex vertex4 = new Vertex(5,5,false);
        Vertex vertex5 = new Vertex(10,0,false);
        Vertex vertex6 = new Vertex(10,5,false);
        Vertex vertex7 = new Vertex(0,10,false);
        Vertex vertex8 = new Vertex(5,10,false);
        Vertex vertex9 = new Vertex(10,10,false);
        Vertex vertex10 = new Vertex(20,20,false);

        graph.addUniEdge(vertex1, vertex2);
        graph.addUniEdge(vertex2, vertex1);
        graph.addUniEdge(vertex2, vertex3);
        graph.addUniEdge(vertex3, vertex4);
        graph.addUniEdge(vertex4, vertex5);
        graph.addUniEdge(vertex5, vertex6);
        graph.addUniEdge(vertex6, vertex7);
        graph.addUniEdge(vertex7, vertex8);
        graph.addUniEdge(vertex8, vertex9);
        graph.addUniEdge(vertex9, vertex10);
        graph.addUniEdge(vertex10, vertex1);

        ArrayList<Vertex> vertices = graph.getVertices();

        System.out.println("Before Shortest Path Run:");
        for( Vertex v: vertices)
        {
            System.out.println( v );
        }
        System.out.println();

        graph.shortestPath(vertex1);
        System.out.println("Shortest Path from vertex1:");
        for( Vertex v: vertices)
        {
            System.out.println( v );
        }
        System.out.println();

        graph.shortestPath(vertex7);
        System.out.println("Shortest Path from vertex7:");
        for( Vertex v: vertices)
        {
            System.out.println( v );
        }
        System.out.println();
    }
}
