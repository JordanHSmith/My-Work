/*
Jordan Smith
clltest.c
10/25/23
Test file for Linked List
*/

#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"
#include <string.h>

// Function that prints an integer
void printInt(void *i) {
    int *a = (int *)i;
    printf("int value: %d\n", *a);
}

// Function that squares an integer
void squareInt(void *i) {
    int *a = (int *)i;
    *a = *a * *a;
}

// Function that compares two integers and returns 1 if they are equal
int compInt(void *i, void *j) {
    int *a = (int *)i;
    int *b = (int *)j;
    return (*a == *b);
}

// Prints square of a double
void printDouble(void *i) {
    double *d = (double *)i;
    printf("double value: %f\n", *d);
}

// Function that squares an integer
void squareDouble(void *i) {
    double *d = (double *)i;
    *d = *d * *d;
}

// Function that compares two integers and returns 1 if they are equal
int compDouble(void *i, void *j) {
    double *a = (double *)i;
    double *b = (double *)j;
    return (*a == *b);
}

int main(int argc, char *argv[]) {
    struct LinkedList *l;
	struct LinkedList *l2;
    int *a;
	double *d;
    int *intTarget;
	double *doubleTarget;
    int i;

    // Create a list
    l = ll_create();
	l2 = ll_create();

    // Push data on the list (integers)
    for (i = 0; i < 20; i += 2) {
        a = malloc(sizeof(int));
        *a = i;
        ll_push(l, a);
    }

    // Push data on the list (doubles)
    for (double j = 1.5; j < 20.0; j += 1.5) {
        d = malloc(sizeof(double));
        *d = j;
        ll_push(l2, d);
    }

    // Printing the list and testing map for both data types
    printf("After initialization\n");
    ll_map(l, printInt);
    ll_map(l2, printDouble);

    // Testing squaring for both data types
    ll_map(l, squareInt);
    ll_map(l2, squareDouble);

    printf("\nAfter squaring\n");
    ll_map(l, printInt);
    ll_map(l2, printDouble);

    // Testing removing data (integers)
    intTarget = malloc(sizeof(int));
    *intTarget = 16;
    a = ll_remove(l, intTarget, compInt);
    if (a != NULL)
        printf("\nRemoved integer: %d\n", *a);
    else
        printf("\nNo instance of integer %d\n", *intTarget);

    *intTarget = 11;
    a = ll_remove(l, intTarget, compInt);
    if (a != NULL)
        printf("\nRemoved integer: %d\n", *a);
    else
        printf("\nNo instance of integer %d\n", *intTarget);

    // Testing removing data (doubles)
    doubleTarget = malloc(sizeof(double));
    *doubleTarget = 6.75;
    d = ll_remove(l2, &doubleTarget, compDouble);
    if (d != NULL)
        printf("\nRemoved double: %f\n", *d);
    else
        printf("\nNo instance of double %f\n", *doubleTarget);

    *doubleTarget = 10.5;
    d = ll_remove(l2, &doubleTarget, compDouble);
    if (d != NULL)
        printf("\nRemoved double: %f\n", *d);
    else
        printf("\nNo instance of double %f\n", *doubleTarget);

    printf("\nAfter removals\n");
    ll_map(l, printInt);
    ll_map(l2, printDouble);

    // Testing appending data (integers)
    ll_append(l, intTarget);

    // Testing appending data (doubles)
    ll_append(l2, doubleTarget);

    printf("\nAfter append\n");
    ll_map(l, printInt);
    ll_map(l2, printDouble);

    // Test clearing
    ll_clear(l, free);
	ll_clear(l2, free);

    printf("\nAfter clear\n");
    ll_map(l, printInt);
    ll_map(l2, printDouble);

    // Rebuild and test append and pop
    for (i = 0; i < 5; i++) {
        a = malloc(sizeof(int));
        *a = i;
        ll_append(l, a);
    }

    for (double j = 0.5; j < 5.0; j += 0.5) {
        d = malloc(sizeof(double));
        *d = j;
        ll_append(l2, d);
    }

    printf("\nAfter appending\n");
    ll_map(l, printInt);
    ll_map(l2, printDouble);

    a = ll_pop(l);
    printf("\nPopped integer: %d\n", *a);
    free(a);

    d = ll_pop(l2);
    printf("Popped double: %f\n", *d);
    free(d);

    printf("\nAfter popping\n");
    ll_map(l, printInt);
    ll_map(l2, printDouble);

    printf("\nInt List size: %d\n", ll_size(l));
	printf("Double List size: %d\n", ll_size(l2));


	//Additional example for why freefunc() parameter is necessary
	struct Person {
    char *name;
    int age;
	};

	struct LinkedList *personList = ll_create();

    // Insert some Person objects into the list
    struct Person *person1 = (struct Person *)malloc(sizeof(struct Person));
    person1->name = strdup("Alice");
    person1->age = 30;

    struct Person *person2 = (struct Person *)malloc(sizeof(struct Person));
    person2->name = strdup("Bob");
    person2->age = 25;

    ll_append(personList, person1);
    ll_append(personList, person2);

    // Clear the list without providing a freefunc
    ll_clear(personList, NULL); //Results in memory leak

    return 0;
}