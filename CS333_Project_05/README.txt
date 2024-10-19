CS333 - Project 4 - README
Jordan Smith
10/24/23
Google Sites URL: https://sites.google.com/colby.edu/jordan-smiths-cs333/home

Directory Layout:
Project5_jhsmit
.
├── LinkedList.c
├── README.txt
├── c_cpp_properties.json
├── clltest
├── clltest.c
├── extension1.r
├── linkedlist.h
├── linkedlist.js
├── package-lock.json
├── settings.json
└── task1_test.js

Operating System and C Compiler info:
Apple clang version 14.0.3 (clang-1403.0.22.14.1)
Target: arm64-apple-darwin22.6.0

Part 1)
Tasks 1-5)
Compile:
gcc -o clltest clltest.c LinkedList.c 

Run:
./clltest

Expected Output for Original Test File:
After initialization
value: 18
value: 16
value: 14
value: 12
value: 10
value: 8
value: 6
value: 4
value: 2
value: 0

After squaring
value: 324
value: 256
value: 196
value: 144
value: 100
value: 64
value: 36
value: 16
value: 4
value: 0

removed: 324

removed: 256

After removals
value: 196
value: 144
value: 100
value: 64
value: 36
value: 16
value: 4
value: 0

After append
value: 196
value: 144
value: 100
value: 64
value: 36
value: 16
value: 4
value: 0
value: 11

After clear

After appending
value: 0
value: 1
value: 2
value: 3
value: 4

popped: 0
popped: 1

After popping
value: 2
value: 3
value: 4

List size: 3

Expected Output for Extended Test File:

After initialization
int value: 18
int value: 16
int value: 14
int value: 12
int value: 10
int value: 8
int value: 6
int value: 4
int value: 2
int value: 0
double value: 19.500000
double value: 18.000000
double value: 16.500000
double value: 15.000000
double value: 13.500000
double value: 12.000000
double value: 10.500000
double value: 9.000000
double value: 7.500000
double value: 6.000000
double value: 4.500000
double value: 3.000000
double value: 1.500000

After squaring
int value: 324
int value: 256
int value: 196
int value: 144
int value: 100
int value: 64
int value: 36
int value: 16
int value: 4
int value: 0
double value: 380.250000
double value: 324.000000
double value: 272.250000
double value: 225.000000
double value: 182.250000
double value: 144.000000
double value: 110.250000
double value: 81.000000
double value: 56.250000
double value: 36.000000
double value: 20.250000
double value: 9.000000
double value: 2.250000

Removed integer: 324

Removed integer: 256

Removed double: 380.250000

Removed double: 324.000000

After removals
int value: 196
int value: 144
int value: 100
int value: 64
int value: 36
int value: 16
int value: 4
int value: 0
double value: 272.250000
double value: 225.000000
double value: 182.250000
double value: 144.000000
double value: 110.250000
double value: 81.000000
double value: 56.250000
double value: 36.000000
double value: 20.250000
double value: 9.000000
double value: 2.250000

After append
int value: 196
int value: 144
int value: 100
int value: 64
int value: 36
int value: 16
int value: 4
int value: 0
int value: 11
double value: 272.250000
double value: 225.000000
double value: 182.250000
double value: 144.000000
double value: 110.250000
double value: 81.000000
double value: 56.250000
double value: 36.000000
double value: 20.250000
double value: 9.000000
double value: 2.250000
double value: 10.500000

After clear

After appending
int value: 0
int value: 1
int value: 2
int value: 3
int value: 4
double value: 0.500000
double value: 1.000000
double value: 1.500000
double value: 2.000000
double value: 2.500000
double value: 3.000000
double value: 3.500000
double value: 4.000000
double value: 4.500000

Popped integer: 0
Popped double: 0.500000

After popping
int value: 1
int value: 2
int value: 3
int value: 4
double value: 1.000000
double value: 1.500000
double value: 2.000000
double value: 2.500000
double value: 3.000000
double value: 3.500000
double value: 4.000000
double value: 4.500000

Int List size: 4
Double List size: 8

Explanation:
The second output reprints all the content of the original test file but adds to it a demonstration
that my linked list has been extended to work with double data types as well. Though nothing is
printed out (for the sake of avoiding clutter), at the bottom of clltest.c there is an example
of data leaking resulting from passing in NULL as the freefunc paramter for the ll_clear method.
This example shows that the freefunc parameter is necessary in order to free any dynamically
allocated memory within a custom-made struct.


Part 2)
Task 1)
*PLEASE NOTE THAT MY WHOLE PROJECT INCLUDING MY WORK WITH JAVASCRIPT AND MY
    EXTENSIONS WERE COMPLETED INDEPENDENTLY WITH NO ASSISTANCE OF A PARTNER*

Run: node task1_test.js
For output and analysis, see my Google Sites.


Extensions:
Run: Rscript extension1.r

For my extensions this week, I completed all the assignment for Part 2 of the project in R.
See my Google Sites for more information.