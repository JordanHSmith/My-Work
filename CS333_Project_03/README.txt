CS333 - Project 3 - README
Jordan Smith
10/04/23
Google Sites URL: https://sites.google.com/colby.edu/jordan-smiths-cs333/home

Directory Layout:
Project3_jhsmit
.
└── Project3_jhsmit
    ├── README.txt
    ├── cstk.c
    ├── cstk.h
    ├── cstktest
    ├── cstktest.c
    ├── extension1.r
    ├── extension2.r
    ├── extension3.r
    ├── task1.js
    ├── task2.js
    └── task3.js

Operating System and C Compiler info:
Apple clang version 14.0.3 (clang-1403.0.22.14.1)
Target: arm64-apple-darwin22.6.0

Task 1)

Explanation:
cstk.h is a header file which defines, but does not implement, the functions necessary
for a stack in C. This includes various functions like push and pop as well as a struct
named stack, which holds a variable for the stack itself (represented as an array) and
the top element of said stack.

Task 2)

Explanation:
cstk.c actually implements all of the functions defined in cstk.h. The push and pop functions
work like in any other langauge, but there are additional functions like create and destroy,
which use C's unique malloc and free commands to (de-)allocate memory appropriately for the
stack struct.

Task 3)
Compile:
gcc -o cstktest cstktest.c cstk.c

Run:
./cstktest

Expected Output:
The original list: 0 1 2 3 4 5 6 7 8 9 
The reversed list: 9 8 7 6 5 4 3 2 1 0 

Explanation:
The test file creates a stack struct and then pushes the numbers 0 through 9 onto the
stack. The stack is then printed in original order and reverse order. Finally, the
stack is destroyed, thereby freeing the memory dedicated to the stack.

Part 2)
Task 1)
*PLEASE NOTE THAT MY WHOLE PROJECT INCLUDING MY WORK WITH JAVASCRIPT AND MY
    EXTENSIONS WERE COMPLETED INDEPENDENTLY WITH NO ASSISTANCE OF A PARTNER*

Run: node task1.js
For output and analysis, see my Google Sites.

Task 2)
Run: node task2.js
For output and analysis, see my Google Sites.

Task 3)
Run: node task3.js
For output and analysis, see my Google Sites.

Extensions:
Run: Rscript extension1.r
Run: Rscript extension2.r
Run: Rscript extension3.r

For my extensions this week, I completed all the assignment for Part 2 of the project in R.
See my Google Sites for more information.

