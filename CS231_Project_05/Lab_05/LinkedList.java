/*
Jordan Smith
03/18/22
LinkedList.java
Section C
Project 5
CS 231
*/

package Lab_05;

import java.util.Iterator;    // defines the Iterator interface
import java.util.ArrayList;   
import java.util.Collections; // contains a shuffle function

public class LinkedList<T> implements Iterable<T>
{
    private Node head;
    private int numItems;

    public LinkedList()
    {
        head = null;
        numItems = 0;
    }

    public void clear()
    {
        head = null;
        numItems = 0;
    }

    public int size()
    {
        return numItems;
    }

    public T getHead()
    {
        return head.getThing();
    }

    public T getNext()
    {
        return head.getNext().getThing();
    }

    public void addFirst(T item)
    {
        Node newNode = new Node(item);
        newNode.setNext(head);
        head = newNode;
        numItems += 1;
    }

    public void addLast(T item)
    {
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
            System.out.println("Head: " + head.getThing());
            numItems++;
        }
    }

    public T remove(int index)
    {
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
        return new LLIterator(this.head);
    }

    public ArrayList<T> toArrayList()
    {
        ArrayList<T> arrayList = new ArrayList<T>();
        for (T item: this) {
			arrayList.add(item);
		}
        return arrayList;
        //arrayList.forEach(add(0,this.getHead()));
    }

    public ArrayList<T> toShuffledList()
    {
        ArrayList<T> shuffledArrayList = new ArrayList<T>(toArrayList());
        Collections.shuffle(shuffledArrayList);
        return shuffledArrayList;
    }

    private class Node
    {
        private Node next;
        private T container;

        public Node(T item)
        {
            next = null;
            container = item;
        }

        public T getThing()
        {
            return container;
        }

        public void setNext(Node n)
        {
            next = n;
        }

        public Node getNext()
        {
            return next;
        }
    }

    private class LLIterator implements Iterator<T>
    {
        private Node current;

        public LLIterator(Node head)
        {
            current = head;
            if(hasNext())
            {
                current.setNext(head.getNext());
            }
        }

        public boolean hasNext()
        {
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
            //Node current = head;
            // T temp = head.getThing();
            // head = head.getNext();
            // return(temp);
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