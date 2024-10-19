/*
Jordan Smith
task1_b.c
11/21/23
Average Allocation Time When Freeing Memory
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void measureTime(int size, int iterations) {
    clock_t start, end;
    double cpu_time_used;

    start = clock();

    //Repeatedly allocate and deallocate memory
    for (int i = 0; i < iterations; ++i) {
        void* ptr = malloc(size);
        free(ptr);
        if(i % 100 == 0)
        {
            end = clock();
            cpu_time_used = ((double) (end - start)); //Calculate time taken to (de-)allocate memory
            printf("Iterations: %d, Average time per call: %f seconds\n", iterations, cpu_time_used / 100);
            start = clock();
        }
    }
}

int main() {
    int size = 50000;
    int iterations = 1000;

    measureTime(size, iterations);

    return 0;
}
