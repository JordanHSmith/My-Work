/**
 * Tests accessing memory of variables of different types and
 * observing how they are represented in memory
 *
 * Jordan Smith
 * 09/12/23
 */

#include <stdio.h>
#include <stdlib.h>
        
int main (int arg, char *argv[]) {
					
  char c1 = 'H';
  short shortNum = 10;
  int intNum = 1200;
  long longNum = 1300;
  double doubNum = 20.40;

  unsigned char *ptr;

  //pointer now points to address of c1
  ptr = (unsigned char *)&(c1);

  //prints hex value of c1
  printf("char: \n");
  for(int i=0; i<sizeof(char); i++) {
	    printf("%d: %02X\n", i, ptr[i]);
	}

  //pointer now points to address of shortNum
  printf("\n");
  printf("short: \n");
  ptr = (unsigned char *)&(shortNum);

  //prints hex value of shortNum
  for(int i=0; i<sizeof(short); i++) {
	    printf("%d: %02X\n", i, ptr[i]);
	}

  //pointer now points to address of intNum
  printf("\n");
  printf("int: \n");
  ptr = (unsigned char *)&(intNum);

  //prints hex value of intNum
  for(int i=0; i<sizeof(int); i++) {
	    printf("%d: %02X\n", i, ptr[i]);
	}

  //pointer now points to address of longNum
  printf("\n");
  printf("long: \n");
  ptr = (unsigned char *)&(longNum);

  //prints hex value of longNum
  for(int i=0; i<sizeof(long); i++) {
	    printf("%d: %02X\n", i, ptr[i]);
	}

  //pointer now points to address of doubNum
  printf("\n");
  printf("double: \n");
  ptr = (unsigned char *)&(doubNum);

  //prints hex value of doubNum
  for(int i=0; i<sizeof(double); i++) {
	    printf("%d: %02X\n", i, ptr[i]);
	}
					
  return 0;
}  
    