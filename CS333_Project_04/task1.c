#include <stdio.h>
#include <stdlib.h>

int comparator(const void *p, const void *q) {
    int x = *((int *)p);
    int y = *((int *)q);

    // Check if both x and y are even or odd
    if ((x % 2 == 0) && (y % 2 == 0)) {
        // Both x and y are even, sort in descending order
        if (x > y) {
            return -1;
        }
        if (x < y) {
            return 1;
        }
    } else if ((x % 2 != 0) && (y % 2 != 0)) {
        // Both x and y are odd, sort in ascending order
        if (x > y) {
            return 1;
        }
        if (x < y) {
            return -1;
        }
    } else {
        // One is even, the other is odd
        // Odd numbers come after even numbers
        if (x % 2 == 0) {
            return -1;
        }
        else{
            return 1;
        }
    }

    return 0; // They are equal
}

int main() {
    int ary[] = {10, 11, 1, 8, 9, 0, 13, 4, 2, 7, 6, 3, 5, 12};
    int size = sizeof(ary) / sizeof(int);

    qsort((void *)ary, size, sizeof(int), comparator); // Built in sort method

    printf("The sorted array is: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", ary[i]);
    }
    printf("\n");

    return 0;
}
