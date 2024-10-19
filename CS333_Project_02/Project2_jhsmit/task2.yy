/*
Jordan Smith
task2.yy
09/25/23
Counts number of rows and characters in text file as
    well as the occurences of each vowel
*/

%{
#include <stdio.h>
int row_count = 1; //initialized to one since not all lines end in /n
int char_count = 0;
int vowel_counts[5] = {0, 0, 0, 0, 0}; // correspod to aA, eE, iI, oO, uU
%}

%%
//Checks for vowels and increments appropriate variables
[aA] { vowel_counts[0]++; char_count++;}
[eE] { vowel_counts[1]++; char_count++;}
[iI] { vowel_counts[2]++; char_count++;}
[oO] { vowel_counts[3]++; char_count++;}
[uU] { vowel_counts[4]++; char_count++;}

\n { row_count++; char_count++; } //Increments row and char count
. { char_count++; } //Increments char count for any other character

%%
int main(int argc, char* argv[]) {
    //reading in file
    if (argc > 1)
        yyin = fopen( argv[1], "r" );

    yylex();

    printf("Rows: %d\n", row_count);
    printf("Characters: %d\n", char_count);
    printf("Occurrences of vowels:\n");
    printf("a: %d\n", vowel_counts[0]);
    printf("e: %d\n", vowel_counts[1]);
    printf("i: %d\n", vowel_counts[2]);
    printf("o: %d\n", vowel_counts[3]);
    printf("u: %d\n", vowel_counts[4]);

    return 0;
}
