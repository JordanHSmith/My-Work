/**
 * Creates a struct and tests how much data is represented in memory
 *
 * Jordan Smith
 * 09/15/23
 */

#include <stdio.h>
#include <stdlib.h>

struct MyStruct {
    char a; //1 byte
    short b; //2 bytes
    unsigned int c; //4 bytes
};

int main() {
    struct MyStruct *myStructPtr;
    myStructPtr = (struct MyStruct *)malloc(sizeof(struct MyStruct)); //Creates a pointer from the struct

    myStructPtr->a = 'A';
    myStructPtr->b = 42;
    myStructPtr->c = 123456;

    unsigned char *bytePtr = (unsigned char *)myStructPtr; //Allows memory to be interpreted byte by byte

    //Prints out the hex values of the variables in MyStruct
    printf("Memory layout of MyStruct:\n");
    for (int i = 0; i < sizeof(struct MyStruct); i++) {
        printf("Byte %d: 0x%02X\n", i, bytePtr[i]);
    }

    free(myStructPtr);

    return 0;
}
