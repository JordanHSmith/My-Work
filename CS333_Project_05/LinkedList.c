/*
Jordan Smith
LinkedList.c
10/25/23
Linked List
*/

#include <stdio.h>
#include <stdlib.h>

// Node struct to hold data and a pointer to the next Node
struct Node {
    void *data;           // Pointer to the stored data
    struct Node *next;    // Pointer to the next Node in the list
};

// LinkedList struct to hold the head of the list
struct LinkedList {
    struct Node *head;     // Pointer to the first Node in the list
    int size;              // Size of the list
};

// Function to create a new LinkedList
struct LinkedList *ll_create() {
    struct LinkedList *list = (struct LinkedList *)malloc(sizeof(struct LinkedList));
    if (list) {
        list->head = NULL;
        list->size = 0;
    }
    return list;
}

// Function to insert a new Node with data at the front of the list
void ll_push(struct LinkedList *list, void *data) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    if (newNode) {
        newNode->data = data;
        newNode->next = list->head;
        list->head = newNode;
        list->size++;
    }
}

// Function to remove and return the data from the front of the list
void *ll_pop(struct LinkedList *list) {
    if (list->head) {
        struct Node *temp = list->head;
        list->head = list->head->next;
        void *data = temp->data;
        free(temp);
        list->size--;
        return data;
    }
    return NULL;
}

// Function to add a new Node with data at the end of the list
void ll_append(struct LinkedList *list, void *data) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    if (newNode) {
        newNode->data = data;
        newNode->next = NULL;

        if (list->head == NULL) {
            list->head = newNode;
        } else {
            struct Node *current = list->head;
            while (current->next != NULL) {
                current = current->next;
            }
            current->next = newNode;
        }
        list->size++;
    }
}

// Function to remove the first node with data matching the target using the given comparison function
void *ll_remove(struct LinkedList *list, void *target, int (*compfunc)(void *, void *)) {
    struct Node *current = list->head;
    struct Node *prev = NULL;

    while (current != NULL) {
        if (compfunc(current->data, target) == 0) {
            if (prev != NULL) {
                prev->next = current->next;
            } else {
                list->head = current->next;
            }

            void *data = current->data;
            free(current);
            list->size--;
            return data;
        }

        prev = current;
        current = current->next;
    }

    return NULL;
}

// Function to get the size of the list
int ll_size(struct LinkedList *list) {
    return list->size;
}

// Function to clear the list and free associated data using the given function
void ll_clear(struct LinkedList *list, void (*freefunc)(void *)) {
    struct Node *current = list->head;
    while (current != NULL) {
        struct Node *temp = current;
        current = current->next;
        if (freefunc) {
            freefunc(temp->data);
        }
        free(temp);
    }
    list->head = NULL;
    list->size = 0;
}

// Function to apply a function to the data at each node
void ll_map(struct LinkedList *list, void (*mapfunc)(void *)) {
    struct Node *current = list->head;
    while (current != NULL) {
        mapfunc(current->data);
        current = current->next;
    }
}