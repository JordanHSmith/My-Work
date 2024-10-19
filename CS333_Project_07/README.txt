CS333 - Project 7 - README
Jordan Smith
11/21/23
Google Sites URL: https://sites.google.com/colby.edu/jordan-smiths-cs333/home

Directory Layout:
Project7_jhsmit
.
├── README.txt
├── task1
├── task1_a
├── task1_a.c
├── task1_b
├── task1_b.c
└── task2.js

Operating System and C Compiler info:
Apple clang version 14.0.3 (clang-1403.0.22.14.1)
Target: arm64-apple-darwin22.6.0

Part 1)
Task 1.a)
Compile:
gcc -o task1_a task1_a.c

Run:
./task1_a

Sample Expected Output:
Memory size: 10 bytes, Average time per call: 0.069800 seconds
Memory size: 1000 bytes, Average time per call: 0.165000 seconds
Memory size: 10000 bytes, Average time per call: 0.060900 seconds
Memory size: 100000 bytes, Average time per call: 0.072600 seconds
Memory size: 100000000 bytes, Average time per call: 0.836400 seconds

Explanation:
To calculate the average time it takes to allocate the various number of bytes, I ran 10,000 iterations
of allocating the memory. As can be seen above, when dealing with relatively large numbers (10,000
bytes and above) there is a positive correlation between the number of bytes allocated and time per
call. With smaller numbers of bytes (1000 or fewer), however, there are some anomalies. For example,
allocating 1,000 bytes takes the most time; this is likely simply because different memory allocators
use different algorithms, some of which are optimized for storing larger number of bytes. This seems
to be the case in the current instance, which is why the smaller bytes take longer to allocate than
would be expected when analyzing byte size alone.

Task1.b)
Compile:
gcc -o task1_b task1_b.c

Run:
./task1_b

Sample Expected Output:
Iterations: 1000, Average time per call: 0.260000 seconds
Iterations: 1000, Average time per call: 0.090000 seconds
Iterations: 1000, Average time per call: 0.080000 seconds
Iterations: 1000, Average time per call: 0.080000 seconds
Iterations: 1000, Average time per call: 0.080000 seconds
Iterations: 1000, Average time per call: 0.090000 seconds
Iterations: 1000, Average time per call: 0.080000 seconds
Iterations: 1000, Average time per call: 0.090000 seconds
Iterations: 1000, Average time per call: 0.080000 seconds
Iterations: 1000, Average time per call: 0.090000 seconds

Explanation:
As can be seen above, all the allocations take roughly the same amount of time. This is because 
the allocated memory is immediately freed, so the memory space can be reused. Therefore, effectively
the same operation is being performed with every run, so the time taken will naturally be comparable.
The one exception is the first iteration, which will always take longer because compilers take extra
time to set up the program at the start.


Part 2)
*PLEASE NOTE THAT MY WHOLE PROJECT INCLUDING MY WORK WITH JAVASCRIPT AND MY
    EXTENSIONS WERE COMPLETED INDEPENDENTLY WITH NO ASSISTANCE OF A PARTNER*
Task 1)
For code examples and explanations of allocation/deallocation/memory management in JavaScript, see
my Google Sites.

Task 2)
Run: node task2.js
For output and analysis, see my Google Sites.


Extensions:
Run: Rscript extension.r

For my extensions this week, I recreated the garbage collection sweep detector.
See my Google Sites for more information.