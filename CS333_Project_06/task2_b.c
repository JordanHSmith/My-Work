/*
Jordan Smith
task2_b.c
11/08/23
SIGFPE Handler
*/

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

// Signal handler function
void sigfpe_handler(int signal) {
    printf("Caught a Floating Point Exception (SIGFPE)\n");

    // Handle the exception here or take appropriate action
    // For this example, we'll just print a message

    // Optionally, you can reset the signal handler to the default behavior
    // signal(SIGFPE, SIG_DFL);
}

int main() {
    // Register the sigfpe_handler function to handle SIGFPE
    signal(SIGFPE, sigfpe_handler);

    printf("Attempting a division by zero...\n");

    int numerator = 10;
    int denominator = 0;
    int result;

    // Trigger a division by zero
    result = numerator / denominator;

    // The program continues to execute after the exception is caught
    printf("The result of the division is: %d\n", result); //This value will be incorrect since
                                                           //zero-division is impossible

    return 0;
}
