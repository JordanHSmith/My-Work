/*
Jordan Smith
task2_a.c
11/08/23
SIGSEGV Handler
*/

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

// Signal handler function
void sigsegv_handler(int signum) {
    printf("Caught a Segmentation Fault (SIGSEGV)\n");
    exit(1); // Terminate the program after handling the error
}

int main() {
    // Register the sigsegv_handler function to handle SIGSEGV
    signal(SIGSEGV, sigsegv_handler);

    printf("Attempting to access illegal memory...\n");

    int *ptr = NULL;
    *ptr = 13; // This will trigger a segmentation fault

    // The program does not continue here, since the segmentation fault is a serious error

    printf("This line will never be reached.\n");

    return 0;
}
