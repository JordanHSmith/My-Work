/*
Jordan Smith
04/04/22
MyQueue.java
CS231
Section C
Project 6
*/

package Lab_06;

import java.util.Iterator;

public class MyQueue<T> implements Iterable<T>
{
    //Creates methods for a queue
    private Node head;
    private Node tail;
    private int numItems;

    public MyQueue()
    {
        //Constructor for queue
        head = null;
        tail = null;
        numItems = 0;
    }

    public int size()
    {
        //returns the size of the queue
        return numItems;
    }

    public boolean empty()
    {
        //returns true if the queue is empty and false otherwise
        if(numItems == 0)
        {
            return true;
        }
        return false;
    }

    public boolean offer(T item)
    {
        //Adds a new node with its element as item to the head of the queue
        Node newNode = new Node(item);
        newNode.setNext(null);
        newNode.setPrevious(tail);
        if(!empty())
        {
            tail.setNext(newNode);
        }
        else
        {
            head = newNode;
        }
        numItems++;
        tail = newNode;
        return true;
    }

    public T peek()
    {
        //Returns the element of the queue's head
        if(empty())
        {
            return null;
        }
        return head.getThing();
    }

    public T poll()
    {
        //Removes the head of the queue
        if (!empty())
        {
			T data = head.getThing();
            head = head.getNext();
            if(numItems > 1)
            {
                head.setPrevious(null);
            }
			numItems--;
			return data;
		}
        else
        {
			return null;
		}
    }

    public Iterator<T> iterator()
    {
        //Makes an iterator object
        return new DLLIterator(this.head);
    }

    private class Node
    {
        //Makes a node that stores a value and a reference to the next node
        private Node next;
        private Node previous;
        private T container;

        public Node(T item)
        {
            //Constructor for the Node class
            next = null;
            previous = null;
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

        public void setPrevious(Node p)
        {
            //Sets the previous node to n
            previous = p;
        }

        public Node getPrevious()
        {
            //Returns the previous node
            return previous;
        }
    }

    private class DLLIterator implements Iterator<T>
    {
        //Creates a linked list iterator
        private Node current;

        public DLLIterator(Node head)
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

    public static void main(String[] args)
    {
        //Test code for the queue
        MyQueue<Integer> myQueueTest = new MyQueue<>();
        myQueueTest.offer(10);
        System.out.println("Should be 1. NumItems: " + myQueueTest.size());
        myQueueTest.offer(20);
        System.out.println("Should be 2. NumItems: " + myQueueTest.size());
        System.out.println("Should be 10. Top item: " + myQueueTest.peek());
        System.out.println("Should be 10. Top item: " + myQueueTest.poll());
        System.out.println("Should be 20. Top item: " + myQueueTest.poll());
        System.out.println("Should be null. Top item: " + myQueueTest.poll());


        myQueueTest.offer(30);
        myQueueTest.offer(40);
        myQueueTest.offer(50);
        myQueueTest.offer(60);
        myQueueTest.offer(70);
        System.out.println("Should be 5 items printed.");
        int counter = 0;
        for(Integer item: myQueueTest)
        {
            counter++;
			System.out.println("Item: " + item);
		}
        System.out.println("There were " + counter + " items printed.");
    }
}