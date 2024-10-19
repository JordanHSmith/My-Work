/*
Jordan Smith
04/04/22
LinkedList.java
CS231
Section C
Project 6
*/

import java.util.Iterator;    // defines the Iterator interface
import java.util.ArrayList;   
import java.util.Collections; // contains a shuffle function

public class LinkedList<T> implements Iterable<T>
{
    //Creates a generic linked list
    private Node head;
    private int numItems;

    public LinkedList()
    {
        //Constructor for linked list
        head = null;
        numItems = 0;
    }

    public void clear()
    {
        //Resets linked list
        head = null;
        numItems = 0;
    }

    public int size()
    {
        //Returns the size of the linked list
        return numItems;
    }

    public T getHead()
    {
        //Returns head of the linked list
        return head.getThing();
    }

    public T getNext()
    {
        //Returns the next node in the linked list
        return head.getNext().getThing();
    }

    public void addFirst(T item)
    {
        //Adds a node at the beginning of the linekd list
        Node newNode = new Node(item);
        newNode.setNext(head);
        head = newNode;
        numItems += 1;
    }

    public void addLast(T item)
    {
        //Adds a node at the end of the linked lsit
        Node newNode = new Node(item);
        Node current = head;
        int tempNumItems = numItems;
        if(size() > 0)
        {
            while(numItems > 1)
            {
                current = current.getNext();
                numItems--;
            }
            current.setNext(newNode);
            newNode.setNext(null);
            numItems = tempNumItems + 1;
        }
        else
        {
            addFirst(item);
        }
    }

    public void add(int index, T item)
    {
        //Adds a node at the specified index
        Node newNode = new Node(item);
        Node current = head;
        int counter = 0;
        if(index == 0)
        {
            addFirst(item);
        }
        else if(size() == index)
        {
            addLast(item);
        }
        else
        {
            while(counter < index-1)
            {
                current = current.getNext();
                counter++;
            }
            newNode.setNext(current.getNext());
            current.setNext(newNode);
            numItems++;
        }
    }

    public T remove(int index)
    {
        //Removes and returns the value of the node at the specified index
        Node current = head;
        Node previous = head;
        int counter = 0;
        while(current != null)
        {
            if(counter == index)
            {
                previous.setNext(current.getNext());
                numItems--;
                if(index == 0)
                {
                    head = head.getNext();
                }
                return current.getThing();
            }
            previous = current;
            current = current.getNext();
            counter++;
        }
        return null;
    }

    public Iterator<T> iterator()
    {
        //Returns an iterator object starting at head
        return new LLIterator(this.head);
    }

    public ArrayList<T> toArrayList()
    {
        //Converts the linked list to an arrayList
        ArrayList<T> arrayList = new ArrayList<T>();
        for (T item: this) {
			arrayList.add(item);
		}
        return arrayList;
    }

    public ArrayList<T> toShuffledList()
    {
        //Converts the linked list to a shuffled arrayList
        ArrayList<T> shuffledArrayList = new ArrayList<T>(toArrayList());
        Collections.shuffle(shuffledArrayList);
        return shuffledArrayList;
    }

    private class Node
    {
        //Makes a node that stores a value and a reference to the next node
        private Node next;
        private T container;

        public Node(T item)
        {
            //Constructor for the Node class
            next = null;
            container = item;
        }

        public T getThing()
        {
            //Returns the value of the Node
            return container;
        }

        public void setNext(Node n)
        {
            //Sets the next node to n
            next = n;
        }

        public Node getNext()
        {
            //Returns the next node
            return next;
        }
    }

    private class LLIterator implements Iterator<T>
    {
        //Creates a linked list iterator
        private Node current;

        public LLIterator(Node head)
        {
            //Constructor for LLIterator
            current = head;
            if(hasNext())
            {
                current.setNext(head.getNext());
            }
        }

        public boolean hasNext()
        {
            //Checks to see if the list has another Node to iterate through
            if(current != null)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        public T next()
        {
            //Iterates through the linked list
            if(hasNext())
            {
                T temp = current.getThing();
                current = current.getNext();
                return(temp);
            }
            return null;
        }

        public void remove()
        {

        }
    }
}