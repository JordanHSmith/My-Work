/**
 * Adds one to infinity to demonstrate that it is still infinity
 *
 * Jordan Smith
 * 09/12/23
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
        
int main (int arg, char *argv[]) {
    float positive_infinity = INFINITY; 
    printf("inf + 1 = %f\n", positive_infinity + 1.0); //Proves that adding one to infinity is still infinit in C
    return 0;
}  
    