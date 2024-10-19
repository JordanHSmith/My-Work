/*
Jordan Smith
colorize.c
12/11/23
Colorize Photo Using Parallelism
*/ 


#include <stdio.h>
#include <stdlib.h>
#include "ppmIO.h"
#include <pthread.h>
#include <sys/timeb.h>

// Struct to pass parameters to the thread function
struct ThreadData {
    Pixel *src;
    int start;
    int end;
};

// Thread function for processing a range of pixels
void *process_pixels(void *data) {
    struct ThreadData *threadData = (struct ThreadData *)data;

    for (int i = threadData->start; i < threadData->end; i++) {
        threadData->src[i].r = threadData->src[i].r > 128 ? (220 + threadData->src[i].r) / 2 : (30 + threadData->src[i].r) / 2;
        threadData->src[i].g = threadData->src[i].g > 128 ? (220 + threadData->src[i].g) / 2 : (30 + threadData->src[i].g) / 2;
        threadData->src[i].b = threadData->src[i].b > 128 ? (220 + threadData->src[i].b) / 2 : (30 + threadData->src[i].b) / 2;
    }

    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc < 4) {
        printf("Usage: %s <image filename> <num_threads> <num_iterations>\n", argv[0]);
        exit(-1);
    }

    // Set the number of threads and iterations
    int num_threads = atoi(argv[2]);
    int num_iterations = atoi(argv[3]);

    Pixel *src;
    int rows, cols, colors;
    int i, j;

    // read image and check for errors
    src = ppm_read(&rows, &cols, &colors, argv[1]);
    if (!src) {
        printf("Unable to read file %s\n", argv[1]);
        exit(-1);
    }

    // Initialize pthreads
    pthread_t threads[num_threads];
    struct ThreadData threadData[num_threads];

    // Calculate the range of pixels each thread will process
    int pixels_per_thread = rows * cols / num_threads;
    int remaining_pixels = rows * cols % num_threads;

    // Record start time
    struct timeb start_time;
    ftime(&start_time);

    for (j = 0; j < num_iterations; j++) {
        // Launch threads
        int start = 0;
        for (i = 0; i < num_threads; i++) {
            threadData[i].src = src;
            threadData[i].start = start;
            threadData[i].end = start + pixels_per_thread + (i < remaining_pixels ? 1 : 0);

            pthread_create(&threads[i], NULL, process_pixels, (void *)&threadData[i]);

            start = threadData[i].end;
        }

        // Wait for threads to finish
        for (i = 0; i < num_threads; i++) {
            pthread_join(threads[i], NULL);
        }
    }

    // Record end time
    struct timeb end_time;
    ftime(&end_time);

    // Calculate the elapsed time
    double elapsed_time = (double)(end_time.time - start_time.time) + (double)(end_time.millitm - start_time.millitm) / 1000;
    printf("start: %ld\nend: %ld\n", start_time.time, end_time.time);
    printf("Total Elapsed Time for %d Iterations: %f seconds\n", num_iterations, elapsed_time);

    // write out the image
    ppm_write(src, rows, cols, colors, "bold_parallel.ppm");

    free(src);

    return 0;
}





// #include <stdio.h>
// #include <stdlib.h>
// #include "ppmIO.h"
// #include <pthread.h>
// #include <time.h>

// // Struct to pass parameters to the thread function
// struct ThreadData {
//     Pixel *src;
//     int start;
//     int end;
// };

// // Thread function for processing a range of pixels
// void *process_pixels(void *data) {
//     struct ThreadData *threadData = (struct ThreadData *)data;

// 	// printf("Working");

//     for (int i = threadData->start; i < threadData->end; i++) {
//         threadData->src[i].r = threadData->src[i].r > 128 ? (220 + threadData->src[i].r) / 2 : (30 + threadData->src[i].r) / 2;
//         threadData->src[i].g = threadData->src[i].g > 128 ? (220 + threadData->src[i].g) / 2 : (30 + threadData->src[i].g) / 2;
//         threadData->src[i].b = threadData->src[i].b > 128 ? (220 + threadData->src[i].b) / 2 : (30 + threadData->src[i].b) / 2;
//     }

//     return NULL;
// }

// int main(int argc, char *argv[]) {
//     if (argc < 4) {
//         printf("Usage: %s <image filename> <num_threads> <num_iterations>\n", argv[0]);
//         exit(-1);
//     }

//     // Set the number of threads and iterations
//     int num_threads = atoi(argv[2]);
//     int num_iterations = atoi(argv[3]);

//     Pixel *src;
//     int rows, cols, colors;
//     int i, j;

//     // read image and check for errors
//     src = ppm_read(&rows, &cols, &colors, argv[1]);
//     if (!src) {
//         printf("Unable to read file %s\n", argv[1]);
//         exit(-1);
//     }

//     // Initialize pthreads
//     pthread_t threads[num_threads];
//     struct ThreadData threadData[num_threads];

//     // Calculate the range of pixels each thread will process
//     int pixels_per_thread = rows * cols / num_threads;
//     int remaining_pixels = rows * cols % num_threads;

//     // Record start time
// 	// printf("Starting! \n"); //Happens near immediately
//     clock_t start_time = clock();

//     for (j = 0; j < num_iterations; j++) {
//         // Launch threads
//         int start = 0;
//         for (i = 0; i < num_threads; i++) {
//             threadData[i].src = src;
//             threadData[i].start = start;
//             threadData[i].end = start + pixels_per_thread + (i < remaining_pixels ? 1 : 0);

//             pthread_create(&threads[i], NULL, process_pixels, (void *)&threadData[i]);

//             start = threadData[i].end;
//         }

//         // Wait for threads to finish
//         for (i = 0; i < num_threads; i++) {
//             pthread_join(threads[i], NULL);
//         }
//     }

//     // Record end time
//     clock_t end_time = clock();

//     // Calculate the elapsed time
//     double elapsed_time = (((double)(end_time - start_time)) / CLOCKS_PER_SEC);
// 	printf("start: %lu\nend: %lu\n", start_time, end_time);
//     printf("Total Elapsed Time for %d Iterations: %f seconds\n", num_iterations, elapsed_time);

//     // write out the image
//     ppm_write(src, rows, cols, colors, "bold_parallel.ppm");

//     free(src);

//     return 0;
// }









// #include <stdio.h>
// #include <stdlib.h>
// #include "ppmIO.h"
// #include <pthread.h>
// #include <time.h>

// // Struct to pass parameters to the thread function
// struct ThreadData {
//     Pixel *src;
//     int start;
//     int end;
// };

// // Thread function for processing a range of pixels
// void *process_pixels(void *data) {
//     struct ThreadData *threadData = (struct ThreadData *)data;

//     for (int i = threadData->start; i < threadData->end; i++) {
//         threadData->src[i].r = threadData->src[i].r > 128 ? (220 + threadData->src[i].r) / 2 : (30 + threadData->src[i].r) / 2;
//         threadData->src[i].g = threadData->src[i].g > 128 ? (220 + threadData->src[i].g) / 2 : (30 + threadData->src[i].g) / 2;
//         threadData->src[i].b = threadData->src[i].b > 128 ? (220 + threadData->src[i].b) / 2 : (30 + threadData->src[i].b) / 2;
//     }

//     return NULL;
// }

// int main(int argc, char *argv[]) {
//     if (argc < 3) {
//         printf("Usage: %s <image filename> <num_threads>\n", argv[0]);
//         exit(-1);
//     }

//     // Set the number of threads
//     int num_threads = atoi(argv[2]);

//     Pixel *src;
//     int rows, cols, colors;
//     int i;

//     // read image and check for errors
//     src = ppm_read(&rows, &cols, &colors, argv[1]);
//     if (!src) {
//         printf("Unable to read file %s\n", argv[1]);
//         exit(-1);
//     }

//     // Initialize pthreads
//     pthread_t threads[num_threads];
//     struct ThreadData threadData[num_threads];

//     // Calculate the range of pixels each thread will process
//     int pixels_per_thread = rows * cols / num_threads;
//     int remaining_pixels = rows * cols % num_threads;

//     // Record start time
//     clock_t start_time = clock();

//     // Launch threads
//     int start = 0;
//     for (i = 0; i < num_threads; i++) {
//         threadData[i].src = src;
//         threadData[i].start = start;
//         threadData[i].end = start + pixels_per_thread + (i < remaining_pixels ? 1 : 0);

//         pthread_create(&threads[i], NULL, process_pixels, (void *)&threadData[i]);

//         start = threadData[i].end;
//     }

//     // Wait for threads to finish
//     for (i = 0; i < num_threads; i++) {
//         pthread_join(threads[i], NULL);
//     }

//     // Record end time
//     clock_t end_time = clock();

//     // Calculate the elapsed time
//     double elapsed_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
//     printf("Elapsed Time: %f seconds\n", elapsed_time);

//     // write out the image
//     ppm_write(src, rows, cols, colors, "bold_parallel.ppm");

//     free(src);

//     return 0;
// }


// #include <stdio.h>
// #include <stdlib.h>
// #include "ppmIO.h"
// #include <pthread.h>

// // Struct to pass parameters to the thread function
// struct ThreadData {
//     Pixel *src;
//     int start;
//     int end;
// };

// // Thread function for processing a range of pixels
// void *process_pixels(void *data) {
//     struct ThreadData *threadData = (struct ThreadData *)data;

//     for (int i = threadData->start; i < threadData->end; i++) {
//         threadData->src[i].r = threadData->src[i].r > 128 ? (220 + threadData->src[i].r) / 2 : (30 + threadData->src[i].r) / 2;
//         threadData->src[i].g = threadData->src[i].g > 128 ? (220 + threadData->src[i].g) / 2 : (30 + threadData->src[i].g) / 2;
//         threadData->src[i].b = threadData->src[i].b > 128 ? (220 + threadData->src[i].b) / 2 : (30 + threadData->src[i].b) / 2;
//     }

//     return NULL;
// }

// int main(int argc, char *argv[]) {
//     if (argc < 3) {
//         printf("Usage: %s <image filename> <num_threads>\n", argv[0]);
//         exit(-1);
//     }

//     // Set the number of threads
//     int num_threads = atoi(argv[2]);

//     Pixel *src;
//     int rows, cols, colors;
//     int i;

//     // read image and check for errors
//     src = ppm_read( &rows, &cols, &colors, argv[1] );
//     if( !src ) {
//         printf("Unable to read file %s\n", argv[1]);
//         exit(-1);
//     }

//     // Initialize pthreads
//     pthread_t threads[num_threads];
//     struct ThreadData threadData[num_threads];

//     // Calculate the range of pixels each thread will process
//     int pixels_per_thread = rows * cols / num_threads;
//     int remaining_pixels = rows * cols % num_threads;

//     // Launch threads
//     int start = 0;
//     for (i = 0; i < num_threads; i++) {
//         threadData[i].src = src;
//         threadData[i].start = start;
//         threadData[i].end = start + pixels_per_thread + (i < remaining_pixels ? 1 : 0);

//         pthread_create(&threads[i], NULL, process_pixels, (void *)&threadData[i]);

//         start = threadData[i].end;
//     }

//     // Wait for threads to finish
//     for (i = 0; i < num_threads; i++) {
//         pthread_join(threads[i], NULL);
//     }

//     // write out the image
//     ppm_write( src, rows, cols, colors, "bold_parallel.ppm" );

//     free(src);

//     return 0;
// }





// #include <stdio.h>
// #include <stdlib.h>
// #include "ppmIO.h"

// int main(int argc, char *argv[]) {
//     Pixel *src;
//     int rows, cols, colors;
//     int i;

//     // check usage
//     if( argc < 2 ) {
//         printf("Usage: %s <image filename>\n", argv[0]);
//         exit(-1);
//     }

//     // read image and check for errors
//     src = ppm_read( &rows, &cols, &colors, argv[1] );
//     if( !src ) {
//         printf("Unable to read file %s\n", argv[1]);
//         exit(-1);
//     }

//     // process image in parallel
// #pragma omp parallel for private(i) shared(src)
//     for(i = 0; i < rows * cols; i++) {
//         src[i].r = src[i].r > 128 ? (220 + src[i].r) / 2 : (30 + src[i].r) / 2;
//         src[i].g = src[i].g > 128 ? (220 + src[i].g) / 2 : (30 + src[i].g) / 2;
//         src[i].b = src[i].b > 128 ? (220 + src[i].b) / 2 : (30 + src[i].b) / 2;
//     }

//     // write out the image
//     ppm_write( src, rows, cols, colors, "bold_parallel.ppm" );

//     free(src);

//     return 0;
// }



