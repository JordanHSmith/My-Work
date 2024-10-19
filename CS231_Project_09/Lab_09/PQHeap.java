package Lab_09;

/*
Jordan Smith
04/25/22
PQHeap.java
CS231
Section C
Project 9
*/

import java.util.Comparator;

public class PQHeap<T>
{
    //Makes a Priority Queue
    private T[] heapArray;
    private int numElements;
    private Comparator<T> comp;

    public PQHeap(Comparator<T> comparator)
    {
        //Constructor for Priority Queue that takes in a comparator
        heapArray = (T[]) new Object[16];
        numElements = 0;
        comp = comparator;
    }

    public int size()
    {
        //Returns the number of elements in the priority queue
        return numElements;
    }

    public void add(T obj)
    {
        //Adds a new item and puts it at the right location based on priority
        if(numElements >= heapArray.length * (2.0/4))
        {
            //Resets heapArray
            T[] oldHeapArray = heapArray;
            numElements = 0;
            heapArray = (T[]) new Object[heapArray.length*2];

            //Adds elements of old array to new array
            for (T item: oldHeapArray)
            {
                if(item != null)
                {
                    add(item);
                }
            }
        }

        heapArray[numElements] = obj;
        int currentIndex = numElements;
        numElements += 1;

        //Compares elements if there are two or more
        if(numElements != 1)
        {
            while(comp.compare(heapArray[currentIndex],(heapArray[(currentIndex-1) / 2])) > 0)
            {
                swap(currentIndex,(currentIndex-1) / 2);
                currentIndex = (currentIndex-1) / 2;
            }
        }
    }

    public T remove()
    {
        //Removes highest priority element
        T removed = heapArray[0];
        if(numElements == 0)
        {
            return null;
        }
        heapArray[0] = heapArray[numElements-1];
        numElements--;
        bubbleUp(0);
        heapArray[numElements] = null;
        return removed;
    }

    private void bubbleUp(int removeIndex)
    {
        //Pushes high prioty elements to top and low priority elements to bottom
        if(!isLeaf(removeIndex))
        {
            if(comp.compare(heapArray[removeIndex],heapArray[(removeIndex*2)+1]) < 0
            || comp.compare(heapArray[removeIndex],heapArray[(removeIndex*2)+2]) < 0)
            {
                if(comp.compare(heapArray[(removeIndex*2)+1],heapArray[(removeIndex*2)+2]) > 0)
                {
                    swap(removeIndex,(removeIndex*2)+1);
                    bubbleUp((removeIndex*2)+1);
                }
                else
                {
                    swap(removeIndex,(removeIndex*2)+2);
                    bubbleUp((removeIndex*2)+2);
                }
            }
        }
    }

    private boolean isLeaf(int checkIndex)
    {
        //Checks if array index has two child node indices
        if(heapArray[(checkIndex*2)+1] == null || heapArray[(checkIndex*2)+2] == null)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    private void swap(int childIndex, int parentIndex)
    {
        //Swaps value of two memory locations
        T temp = heapArray[childIndex];
        heapArray[childIndex] = heapArray[parentIndex];
        heapArray[parentIndex] = temp;
    }

    public void getHeap()
    {
        //Prints out the whole heap in order of priority
        for(T str: heapArray)
        {
            System.out.println("Str: " + str);
        }
    }


    public static void main(String[] args)
    {
        //Test Code
        PQHeap<String> heapTest = new PQHeap<>(new AscendingString());
        heapTest.add("Clara");
        System.out.println("Size: " + heapTest.size());
        heapTest.add("Andy");
        System.out.println("Size: " + heapTest.size());
        heapTest.add("Beth");
        System.out.println("Size: " + heapTest.size());
        heapTest.add("Dave");
        System.out.println("Size: " + heapTest.size());
        heapTest.getHeap();
        System.out.println("Removed: " + heapTest.remove());
        heapTest.getHeap();
        System.out.println("Removed: " + heapTest.remove());
        heapTest.getHeap();
        System.out.println("Removed: " + heapTest.remove());
        heapTest.getHeap();
        System.out.println("Removed: " + heapTest.remove());
        heapTest.getHeap();
        System.out.println("Size: " + heapTest.size());
    }
}