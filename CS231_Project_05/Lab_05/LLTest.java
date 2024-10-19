/*
	Bruce A. Maxwell
	CS 231 Project 5
	Linked List test class
*/

package Lab_05;

import java.util.ArrayList;

public class LLTest {

	public static void main(String[] args) {
		
		LinkedList<Integer> llist = new LinkedList<Integer>();
		
		llist.addFirst(5);
		llist.addFirst(10);
		llist.addFirst(20);

		//System.out.println("Head: " + llist.getHead());

		System.out.printf("\nAfter setup %d\n", llist.size());
		for(Integer item: llist) {
			System.out.printf("thing %d\n", item);
		}
	
		llist.clear();
	
		System.out.printf("\nAfter clearing %d\n", llist.size());
		for (Integer item: llist) {
			System.out.printf("thing %d\n", item);
		}
		
		llist.addLast(5);
		llist.addLast(10);
		llist.addLast(20);
	
		System.out.printf("\nAfter setup %d\n", llist.size());
		for(Integer item: llist) {
			System.out.printf("thing %d\n", item);
		}
	
		llist.clear();
	
		System.out.printf("\nAfter clearing %d\n", llist.size());
		for (Integer item: llist) {
			System.out.printf("thing %d\n", item);
		}
	
		for (int i = 10; i > 0; i -= 2) {
			llist.add(0, i);
		}
		llist.add(5, 12);
		llist.add(3, 0);

		System.out.printf("\nAfter setting %d\n", llist.size());
		for (Integer item: llist) {
			System.out.printf("thing %d\n", item);
		}

		//System.out.println("Head: " + llist.getHead());
		System.out.println(llist.remove(0));
		System.out.printf("\nAfter removing %d\n", llist.size());
		System.out.println("Head1: " + llist.getHead());
		for (Integer item: llist) {
			System.out.printf("thing %d\n", item);
		}
		// System.out.println("Head2: " + llist.getHead());
		
		llist.remove(2);
		System.out.printf("\nAfter removing %d\n", llist.size());
		for (Integer item: llist) {
			System.out.printf("thing %d\n", item);
		}
		
		llist.remove(4);
		System.out.printf("\nAfter removing %d\n", llist.size());
		for (Integer item: llist) {
			System.out.printf("thing %d\n", item);
		}

		ArrayList<Integer> alist = llist.toArrayList();
		System.out.printf("\nAfter copying %d\n", alist.size());
		for(Integer item: alist) {
			System.out.printf("thing %d\n", item);
		}						
		
		alist = llist.toShuffledList();	
		System.out.printf("\nAfter copying %d\n", alist.size());
		for(Integer item: alist) {
			System.out.printf("thing %d\n", item);
		}
	}

}