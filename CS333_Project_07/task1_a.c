/*
Jordan Smith
task1_a.c
11/21/23
Average Allocation Time for Different Memory Sizes
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void measureTime(int size, int iterations) {
    clock_t start, end;
    double cpu_time_used;

    start = clock();

    //Repeatedly Allocate and Deallocate memory
    for (int i = 0; i < iterations; ++i) {
        void* ptr = malloc(size);
        free(ptr);
    }

    end = clock();
    cpu_time_used = ((double) (end - start)); //Calculate time taken to (de-)allocate memory

    printf("Memory size: %d bytes, Average time per call: %f seconds\n", size, cpu_time_used / iterations);
}

int main() {
    int iterations = 10000;

    // Experiment with different memory sizes
    measureTime(10, iterations);    // Small size
    measureTime(1000, iterations);
    measureTime(10000, iterations);  // Medium size
    measureTime(100000, iterations);
    measureTime(100000000, iterations); // Large size

    return 0;
}
