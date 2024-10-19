/*
Jordan Smith
task3.c
09/25/23
Parser for Clite
*/

#include <stdio.h>
#include <stdlib.h>
        

int main (int arg, char *argv[]) {
  int *mem;

  //Allocates a small amount of memory and then immediately frees it
  for(int i=0; i<100000; i++)
  {
    mem = malloc(2);
    free(mem);
  }
  
  return 0;
}  