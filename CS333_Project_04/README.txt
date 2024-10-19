CS333 - Project 3 - README
Jordan Smith
10/04/23
Google Sites URL: https://sites.google.com/colby.edu/jordan-smiths-cs333/home

Directory Layout:
Project4_jhsmit
.
├── README.txt
├── extension1.r
├── extension2.r
├── extension3.r
├── task1
├── task1.c
├── task1.js
├── task2
├── task2.c
├── task2.js
└── task3.js

Operating System and C Compiler info:
Apple clang version 14.0.3 (clang-1403.0.22.14.1)
Target: arm64-apple-darwin22.6.0

Task 1)
Compile:
gcc -o task1 task1.c

Run:
./task1

Expected Output:
The sorted array is: 12 10 8 6 4 2 0 1 3 5 7 9 11 13 

Explanation:
In task.1, the main function was provided. All that was necessary was implementing the comparator
to arrange the numbers in the proper order. To accomplish this, the comparator first checks if
x and y are both even; if so it uses the descending order rules of comparison. So, for example,
if the first element being compared (x) is greater than the second item being compared (y), then
y will go before x, which is represented by returning -1. Conversely, if both x and y are odd,
then the ascending comparison rules will be used. Finally, if an odd number and even number are
compared, then the even number always goes first.

Task 2)
Compile:
gcc -o task2 task2.c

Run:
./task2 <integer>

Some Sample Outputs:
The factorial of 5 is 120
The factorial of 12 is 479001600
The factorial of 13 is 1932053504
The factorial of 14 is 1278945280
The factorial of 15 is 2004310016

Explanation:
In the examples above, one can see that the factorial method ceases to provide accurate
values starting at 13! This is because this is where the bits required to store the correct
value of 13! exceed those allocated by C to store ints. Accordingly, wrap around results in
unexpected values.

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