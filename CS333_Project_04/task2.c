#include <stdio.h>
#include <stdlib.h>

// Function to calculate the factorial of a number
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <number>\n", argv[0]);
        return 1;
    }

    int number = atoi(argv[1]);

    if (number < 0) {
        printf("Please provide a non-negative number.\n");
        return 1;
    }

    int result = factorial(number);

    printf("The factorial of %d is %d\n", number, result);

    return 0;
}
