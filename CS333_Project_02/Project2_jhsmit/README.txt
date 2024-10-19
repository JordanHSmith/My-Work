CS333 - Project 2 - README
Jordan Smith
09/27/23
Google Sites URL: https://sites.google.com/colby.edu/jordan-smiths-cs333/home

Directory Layout:
Project2_jhsmit
.
└── Project2_jhsmit
    ├── Clite
    ├── README.txt
    ├── encode
    ├── encode.yy
    ├── extension.r
    ├── lex.yy.c
    ├── part_1_task_4
    ├── part_1_task_4.c
    ├── part_1_task_4.yy
    ├── part_2_task_4.js
    ├── repl
    ├── replace.yy
    ├── task2
    ├── task2.txt
    ├── task2.yy
    ├── task3
    ├── task3.html
    ├── task3.yy
    └── task3_2.html

Operating System and C Compiler info:
Apple clang version 14.0.3 (clang-1403.0.22.14.1)
Target: arm64-apple-darwin22.6.0

Task 1)

Compile:
flex encode.yy
gcc -o encode lex.yy.c -ll 

Run:
echo "string" | ./encode

Expected Output: 
E.g. If input is MPD then output should be ZcQ

Explanation:
Using the regex sybmol [a-zA-Z], the program checks if there is a capital or lowercase
letter in the inputted string. If there is, then it is shifted forward 13 places in the
alphabet using ASCII numbering. If this new character goes beyond the end of the
alphabet, the if statement will catch this fact and cycle back to the beginning of the 
alphabet, maintaining case in the process.

Task 2)

Compile:
flex task2.yy
gcc -o task2 lex.yy.c -ll

Run:
./task2 < task2.txt 

Expected Output:

Rows: 3
Characters: 45
Occurrences of vowels:
a: 3
e: 4
i: 3
o: 4
u: 0

Explanation:
This file takes in a txt file as a command line argument. The program defines three
variables, one to count the number of rows, another to count the characters, and one
is an array with five spots, each correspodning to one of the vowels. Regex commands
are then used to increment these variables at the appropriate times. Finally, these
counts are printed to the terminal.

Task 3)
Compile:
flex task3.yy
gcc -o task3 lex.yy.c -ll

Run:
./task3 < task3.html (Can also be run with "./task3 < task3_2.html" for bigger example)

Expected Output for ./task3 < task3.html:
This is a page title

Here is a header
Here is some body  text in a paragraph
Here is a link to cs.colby.edu
inside a paragraph.

This is the paragraph we should ignore because it is in a comment.
Bonus if you remove this!
 comment -->
 
This is the final paragraph.

Explanation:
The program uses regex commands to look for things like html key rags placed between "<>"
as well as extra spaces used for formatting purposes.

Task 4)
Compile:
flex part_1_task_4.yy
gcc -o part_1_task_4 lex.yy.c -ll

Run:
./part_1_task_4 < part_1_task_4.c

Expected Output:
Keyword-int
Identifier-main
Open-paren
Close-paren
Open-bracket
Keyword-int
Identifier-a
Assignment
Integer-6
Keyword-int
Identifier-b
Assignment
Float-5.0
Keyword-if
Open-paren
Identifier-a
Comparison-<
Identifier-b
Close-paren
Open-bracket
Identifier-a
Assignment
Identifier-a
Identifier-b
Close-bracket
Close-bracket

Explanation:
The program uses a series of regex commands to determine if a certain symbol has been
used. If it has, then the program prints the corresponding label along witht the specific
instance used.

Part 2)
Task 4)
*PLEASE NOTE THAT MY WHOLE PROJECT INCLUDING MY WORK WITH JAVASCRIPT AND MY
    EXTENSIONS WERE COMPLETED INDEPENDENTLY WITH NO ASSISTANCE OF A PARTNER*

Run: node part_2_task_4.js 
For everything else, see my Google Sites.

Extensions:
Run: Rscript extension.r

For my extension this week, I researched another langauge, R, and created a simple program with it.
For this, see my google site under Jordan Smith's R Work - Project 2.
