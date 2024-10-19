/*
Jordan Smith
cstk.h
10/03/23
Header file for stack
*/

#ifndef CSTK_H
#define CSTK_H

// Structure to represent a stack
typedef struct stack {
    int* stack;  // Array to store stack elements
    int top;     // Index of the top element
} Stack;

// Function to create a stack
Stack* stk_create();

// Function to destroy (deallocate) a stack
void stk_destroy(Stack* stack);

// Function to push a value onto the stack
void stk_push(Stack* stack, int value);

// Function to pop (remove and return) a value from the stack
int stk_pop(Stack* stack);

// Function to display the stack contents
void stk_display(Stack* stack, int reverse);

#endif  // CSTK_H
