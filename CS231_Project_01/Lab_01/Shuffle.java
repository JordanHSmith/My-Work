/**
 * Shuffle.java
 * Jordan Smith
 * 02/08/22
*/

package Lab_01;

import java.util.ArrayList;
import java.util.Random;

public class Shuffle
{
    public static void main(String[] args)
    {
        ArrayList<Integer> arrayList1 = new ArrayList<Integer>();
        for(int i = 0; i < 10; i++)
        {
            // int randNum = (int)(Math.random() * 100);
            // arrayList1.add(randNum);
            // System.out.println(randNum);
            arrayList1.add(i);
        }
        System.out.println("Second Iteration");
        for (int num : arrayList1)
        {
            System.out.println(num);
        }
        for (int i=arrayList1.size() - 1; i>0; i++)
        {
            if(arrayList1.size() > 0)
            {
                int removeIndex = (int)(Math.random() * arrayList1.size());
                //System.out.println("Remove Index: " + removeIndex);
                int randNum = arrayList1.get(removeIndex);
                arrayList1.remove(removeIndex);
                System.out.print("The removed value was: " + randNum + ", and the remaining numbers are:");
                for(int j=0; j<arrayList1.size(); j++)
                {
                    System.out.print(" " + arrayList1.get(j));
                }
                System.out.println();
            }
        }
    }
}
