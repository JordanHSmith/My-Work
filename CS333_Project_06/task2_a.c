/*
Jordan Smith
task2_a.c
11/08/23
SIGINT Handler
*/

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

// Signal handler function
void sigint_handler(int signal) {
    printf("Interrupted!\n");
    exit(0);
}

int main() {
    // Register the sigint_handler function to handle SIGINT (Ctrl-C)
    signal(SIGINT, sigint_handler);

    printf("Press Ctrl-C to interrupt...\n");

    while (1) {
        // Stuck in an infinite loop
    }

    return 0;
}
