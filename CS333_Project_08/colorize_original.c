/*
Jordan Smith
colorize_original.c
12/11/23
Colorize Photo without Using Parallelism
*/ 

#include <stdio.h>
#include <stdlib.h>
#include "ppmIO.h"
#include <time.h>

int main(int argc, char *argv[]) {
    Pixel *src;
    int rows, cols, colors;
    int i, j;

    // check usage
    if (argc < 2) {
        printf("Usage: %s <image filename>\n", argv[0]);
        exit(-1);
    }

    // read image and check for errors
    src = ppm_read(&rows, &cols, &colors, argv[1]);
    if (!src) {
        printf("Unable to read file %s\n", argv[1]);
        exit(-1);
    }

    // Record start time
    clock_t start_time = clock();

    // Process the image 5000 times
    for (j = 0; j < 1000; j++) {
        // Process image
        for (i = 0; i < rows * cols; i++) {
            src[i].r = src[i].r > 128 ? (220 + src[i].r) / 2 : (30 + src[i].r) / 2;
            src[i].g = src[i].g > 128 ? (220 + src[i].g) / 2 : (30 + src[i].g) / 2;
            src[i].b = src[i].b > 128 ? (220 + src[i].b) / 2 : (30 + src[i].b) / 2;
        }
    }

    // Record end time
    clock_t end_time = clock();

    // Calculate the cumulative elapsed time
    double elapsed_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
    printf("Cumulative Elapsed Time for 1000 Iterations: %f seconds\n", elapsed_time);

    // write out the image
    ppm_write(src, rows, cols, colors, "bold_cumulative.ppm");

    free(src);

    return 0;
}