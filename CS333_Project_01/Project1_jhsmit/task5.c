/**
 * Tests to see if my compiler can handle a string that is too long
 *
 * Jordan Smith
 * 09/12/23
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
        

int main (int arg, char *argv[]) {
  char str[4];

  int decision = 0;

  strcpy(str,"Hello"); //Assigns string that is too long for str

  if(decision == 0)
  {
    printf("safe\n");
  }
  else
  {
    printf("hacked\n");
  }

  return 0;
}  