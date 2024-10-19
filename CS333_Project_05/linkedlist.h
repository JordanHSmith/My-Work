/*
Jordan Smith
linkedlist.h
10/25/23
Header file for Linked List
*/

#ifndef LINKEDLIST_H
#define LINKEDLIST_H

// Node struct to hold data and a pointer to the next Node
struct Node {
    void *data;
    struct Node *next;
};

// LinkedList struct to hold the head of the list
struct LinkedList {
    struct Node *head;
    int size;
};

// Function to create a new LinkedList
struct LinkedList *ll_create();

// Function to insert a new Node with data at the front of the list
void ll_push(struct LinkedList *list, void *data);

// Function to remove and return the data from the front of the list
void *ll_pop(struct LinkedList *list);

// Function to add a new Node with data at the end of the list
void ll_append(struct LinkedList *list, void *data);

// Function to remove the first node with data matching the target using the given comparison function
void *ll_remove(struct LinkedList *list, void *target, int (*compfunc)(void *, void *));

// Function to get the size of the list
int ll_size(struct LinkedList *list);

// Function to clear the list and free associated data using the given function
void ll_clear(struct LinkedList *list, void (*freefunc)(void *));

// Function to apply a function to the data at each node
void ll_map(struct LinkedList *list, void (*mapfunc)(void *));

#endif
