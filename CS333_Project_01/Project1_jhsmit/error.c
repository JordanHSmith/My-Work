/**
 * Raises a bus error by attempting to access unaligned memory
 *
 * Jordan Smith
 * 09/15/23
 */

#include <stdio.h>
#include <stdlib.h>
        

int main (int arg, char *argv[]) {
    int *ptr = (int *)4099; //Assigns unaligned address since 4099 is not divisible by 4
    *ptr = 12;
    return 0;
}  