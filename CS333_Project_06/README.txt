CS333 - Project 6 - README
Jordan Smith
11/09/23
Google Sites URL: https://sites.google.com/colby.edu/jordan-smiths-cs333/home

Directory Layout:
Project6_jhsmit
.
├── README.txt
├── extension1.r
├── task1
├── task1.c
├── task1.js
├── task1_test.txt
├── task2_1
├── task2_a
├── task2_a.c
├── task2_b
├── task2_b.c
├── task2_c
└── task2_c.c

Operating System and C Compiler info:
Apple clang version 14.0.3 (clang-1403.0.22.14.1)
Target: arm64-apple-darwin22.6.0

Part 1)
Task 1)
Compile:
gcc -o task1 task1.c

Run:
./task1

Expected Output with task1_test.txt:
the: 17
of: 7
and: 6
was: 5
in: 4
with: 4
a: 3
windows: 3
broken: 2
wings: 2
central: 2
portion: 2
had: 2
been: 2
but: 2
up: 2
were: 2
these: 1
blocked: 1
wooden: 1

Explanation:
In order to store the key-value pairs of words and their corresponding counts, I used
a struct which holds a character array to hold a word and an int to hold its number
of occurences. In the main function, I create an array of this struct to hold the
words that are read into the program from the test file using the built-in fopen
method and then read into the word variable using the built-in fscanf method. For 
each word in the file, the word is added to the total occurence count. Once this
process is completed, the word-occurence pairs are sorted based on frequency, and the
twenty most commonly occurring words are printed out with the respective occurences.

Task 2)
Task2.a)
Compile:
gcc -o task2_a task2_a.c

Run:
./task2_a 

Expected Output:
Press Ctrl-C to interrupt...
^CInterrupted!

Explanation:
This program uses the built-in signal method and SIGINT signal to call the custom-
made sigint_handler method and associate it with the SIGINT signal. This ends the
program when control-C is pressed.

Task2.b)
Compile:
gcc -o task2_b task2_b.c

Run:
./task2_b

Expected Output for VSCode compiler:
Attempting a division by zero...
The result of the division is: 0

Expected Output for online compiler (https://www.onlinegdb.com/online_c_compiler):
Attempting a division by zero...
Caught a Floating Point Exception (SIGFPE)
Caught a Floating Point Exception (SIGFPE)
Caught a Floating Point Exception (SIGFPE)
...

Explanation:
With the compiler provided by VSCode, the program is incapable of detecting the
SIGFPE error signal when zero-division is performed (Professor Taylor said this might
happen), so the code continues as if nothing is wrong and prints an inaccurate value
for the result of the zero division. If an online compiler is used (as Professor
Taylor suggested ought to be doen if the VSCode compiler could not detect the error),
then it will print "Caught a Floating Point Exception (SIGFPE)" infinitely.

Task2.c)
Compile:
gcc -o task2_c task2_c.c

Run:
./task2_c

Expected Output:
Attempting to access illegal memory...
Caught a Segmentation Fault (SIGSEGV)

Explanation:
This program uses the built-in signal method and SIGSEGV signal to call the custom-
made sigsegv_handler method and associate it with the SIGSEGV signal. This ends the
program when a segmentation fault is detected, such as when a null pointer is
assigned a value.


Part 2)
Task 1)
*PLEASE NOTE THAT MY WHOLE PROJECT INCLUDING MY WORK WITH JAVASCRIPT AND MY
    EXTENSIONS WERE COMPLETED INDEPENDENTLY WITH NO ASSISTANCE OF A PARTNER*

Run: node task1.js task1_test.txt
For output and analysis, see my Google Sites.


Extensions:
Run: Rscript extension1.r task1_test.txt

For my extensions this week, I made a word frequency counter in R.
See my Google Sites for more information.