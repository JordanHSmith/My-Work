/**
 * Demonstrates how variables are saved in memory
 *
 * Jordan Smith
 * 09/15/23
 */

#include <stdio.h>
#include <stdlib.h>
        

int main (int arg, char *argv[]) {

  int num = 4;
  char letter = 'j';
  short shortNum = 18;
  unsigned char *ptr = (unsigned char *)&ptr;

  // Prints 100 bytes after pointer address
  for(int i=0; i<100; i++)
  {
    printf("%d: %02X\n", i, ptr[i]);
  }
		
  return 0;
}  