/*
Jordan Smith
cstk.c
10/03/23
Implements a stack using an array
*/

#include "cstk.h"
#include <stdio.h>
#include <stdlib.h>

int CSTK_MAX = 50;

// Function to create a stack
Stack* stk_create() {
    Stack* myStack = (Stack*)malloc(sizeof(Stack)); //allocates memory for stack
    if (myStack == NULL) {
        return NULL;  // Memory allocation failed
    }

    myStack->stack = (int*)malloc(CSTK_MAX * sizeof(int)); //limits max stack size
    if (myStack->stack == NULL) {
        free(myStack);
        return NULL;  // Memory allocation for stack items failed
    }

    myStack->top = -1;  // Initialize the top index

    return myStack;
}

// Function to destroy (deallocate) a stack
void stk_destroy(Stack* myStack) {
    if (myStack != NULL) {
        free(myStack->stack); //frees memory of array representing the stack
        free(myStack); //frees the stack itself
    }
}

// Function to push a value onto the stack
void stk_push(Stack* myStack, int value) {
    if (myStack == NULL || myStack->top == CSTK_MAX - 1) { // checks if stack is full or invalid
        return;
    }

    myStack->top++; //increment top index
    myStack->stack[myStack->top] = value; //add value to top of stack
}

// Function to pop a value from the stack
int stk_pop(Stack* myStack) {
    if (myStack == NULL || myStack->top == -1) {
        return -1;  // Stack is empty or invalid
    }

    int value = myStack->stack[myStack->top]; //save value being popped
    myStack->top--; //decrement top index
    return value;
}

// Function to display the stack contents
void stk_display(Stack* myStack, int reverse) {
    if (myStack == NULL) {
        return;
    }

    if (reverse) //prints in reverse order
    {
        for (int i = myStack->top; i >= 0; i--)
        {
            printf("%d ", myStack->stack[i]);
        }
    }
    else //prints in normal order
    {
        for (int i = 0; i <= myStack->top; i++)
        {
            printf("%d ", myStack->stack[i]);
        }
    }
    printf("\n");
}
