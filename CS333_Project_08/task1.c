/*
Jordan Smith
task1.c
12/11/23
Sorting Algoithm with Parallelism
*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>

#define ARRAY_SIZE 1000000
#define NUM_THREADS 8

// Structure for passing arguments to the sorting function
typedef struct {
    int *array;
    int start;
    int end;
    pthread_mutex_t *mutex;
} SortArgs;

// Comparison function for qsort
int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

// Sorting function for each thread
void *sortThread(void *arg) {
    SortArgs *args = (SortArgs *)arg;

    // Lock before sorting to avoid race condition
    pthread_mutex_lock(args->mutex);

    qsort(args->array + args->start, args->end - args->start + 1, sizeof(int), compare);

    // Unlock after sorting to allow other threads to access the array
    pthread_mutex_unlock(args->mutex);

    pthread_exit(NULL);
}

// Sorting function that divides the array and uses threads
void parallelSort(int *array, int size, int num_threads) {
    pthread_t threads[num_threads];
    SortArgs args[num_threads];
    pthread_mutex_t mutex;

    int chunk_size = size / num_threads;
    int i;

    pthread_mutex_init(&mutex, NULL);

    for (i = 0; i < num_threads; i++) {
        args[i].array = array;
        args[i].start = i * chunk_size;
        args[i].end = (i == num_threads - 1) ? size - 1 : (i + 1) * chunk_size - 1;
        args[i].mutex = &mutex;

        pthread_create(&threads[i], NULL, sortThread, (void *)&args[i]);
    }

    for (i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&mutex);
}

int main() {
    int array[ARRAY_SIZE];

    // Initialize array with random values
    for (int i = 0; i < ARRAY_SIZE; i++) {
        array[i] = rand() % 1000;
    }


    // Single-threaded sorting
    clock_t start = clock();
    qsort(array, ARRAY_SIZE, sizeof(int), compare);
    clock_t end = clock();
    double single_thread_time = ((double)end - start) / CLOCKS_PER_SEC;

    printf("Single-threaded sorting time: %f seconds\n", single_thread_time);

    // Multi-threaded sorting
    for (int num_threads = 1; num_threads <= NUM_THREADS; num_threads++) {
        int copy[ARRAY_SIZE]; // Make a copy for each experiment
        memcpy(copy, array, sizeof(array));

        start = clock();
        parallelSort(copy, ARRAY_SIZE, num_threads);
        end = clock();
        double multi_thread_time = ((double)end - start) / CLOCKS_PER_SEC;

        printf("%d threads sorting time: %f seconds\n", num_threads, multi_thread_time);


        //Verify the array is sorted
        for (int i = 1; i < ARRAY_SIZE; i++) {
            if (array[i - 1] > array[i]) {
                printf("Array is not sorted correctly!\n");
                break;
            }
            if(i == ARRAY_SIZE-1){
                printf("Array is sorted correctly!\n");
            }
        }
    }

    return 0;
}


// #include <stdio.h>
// #include <stdlib.h>
// #include <pthread.h>

// // Structure to pass data to each thread
// typedef struct {
//     double *arr;
//     int start;
//     int end;
// } ThreadData;

// // Function to compare for qsort
// int compare(const void *a, const void *b) {
//     return (*(double *)a - *(double *)b);
// }

// // Function to sort a subarray
// void sort_subarray(double *subarray, int size) {
//     qsort(subarray, size, sizeof(double), compare);
// }

// // Thread function for parallel sorting
// void *thread_sort(void *arg) {
//     ThreadData *data = (ThreadData *)arg;
//     sort_subarray(data->arr + data->start, data->end - data->start);
//     return NULL;
// }

// // Function to perform parallelized sorting
// void parallel_sort(double *arr, int array_size, int num_threads) {
//     pthread_t threads[num_threads];
//     ThreadData thread_data[num_threads];

//     // Create threads
//     for (int i = 0; i < num_threads; i++) {
//         thread_data[i].arr = arr;
//         thread_data[i].start = i * (array_size / num_threads);
//         thread_data[i].end = (i == num_threads - 1) ? array_size : (i + 1) * (array_size / num_threads);

//         if (pthread_create(&threads[i], NULL, thread_sort, &thread_data[i]) != 0) {
//             perror("pthread_create");
//             exit(EXIT_FAILURE);
//         }
//     }

//     // Join threads
//     for (int i = 0; i < num_threads; i++) {
//         if (pthread_join(threads[i], NULL) != 0) {
//             perror("pthread_join");
//             exit(EXIT_FAILURE);
//         }
//     }
// }

// int main() {
//     // Experimentation
//     int array_size = 100;  // Adjust the size of the array
//     int num_threads;

//     // Generate random array
//     double *array_to_sort = (double *)malloc(array_size * sizeof(double));
//     for (int i = 0; i < array_size; i++) {
//         array_to_sort[i] = (double)rand() / RAND_MAX;
//     }

//     // Test with different numbers of threads
//     for (num_threads = 1; num_threads <= 8; num_threads *= 2) {
//         printf("Sorting with %d threads\n", num_threads);

//         // Measure time taken
//         clock_t start_time = clock();

//         // Call the parallel sorting function
//         parallel_sort(array_to_sort, array_size, num_threads);

//         clock_t end_time = clock();

//         // Output results
//         printf("Time taken with %d threads: %f seconds\n", num_threads, (double)(end_time - start_time) / CLOCKS_PER_SEC);
//     }

//     // Verify if the array is sorted correctly
//     for (int i = 1; i < array_size; i++) {
//         printf("%d \n", i);
//         if (array_to_sort[i - 1] > array_to_sort[i]) {
//             printf("Array is not sorted correctly!\n");
//             break;
//         }
//     }

//     free(array_to_sort);

//     return 0;
// }
