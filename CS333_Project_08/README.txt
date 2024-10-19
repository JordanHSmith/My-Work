CS333 - Project 8 - README
Jordan Smith
12/09/23
Google Sites URL: https://sites.google.com/colby.edu/jordan-smiths-cs333/home

Directory Layout:
Project8_jhsmit
.
├── IMG_4203.ppm
├── PPMFile.class
├── PPMFile.java
├── PPMFileOriginal.class
├── PPMFileOriginal.java
├── Pixel.class
├── Pixel.java
├── README.txt
├── bold.ppm
├── bold_cumulative.ppm
├── bold_parallel.ppm
├── colorize
├── colorize.c
├── colorize_original
├── colorize_original.c
├── output.ppm
├── outputParallel.ppm
├── ppmIO.c
├── ppmIO.h
├── task1
└── task1.c

Operating System and C Compiler info:
Apple clang version 14.0.3 (clang-1403.0.22.14.1)
Target: arm64-apple-darwin22.6.0

Part 1)
Task 1.a)
Skipped

Task 1.b)
Compile: gcc -o task1 task1.c

Run:
./task1

Sample Output:
Single-threaded sorting time: 0.060094 seconds
1 threads sorting time: 0.012063 seconds
Array is sorted correctly!
2 threads sorting time: 0.010458 seconds
Array is sorted correctly!
3 threads sorting time: 0.009863 seconds
Array is sorted correctly!
4 threads sorting time: 0.009052 seconds
Array is sorted correctly!
5 threads sorting time: 0.009024 seconds
Array is sorted correctly!
6 threads sorting time: 0.008624 seconds
Array is sorted correctly!
7 threads sorting time: 0.008262 seconds
Array is sorted correctly!
8 threads sorting time: 0.008255 seconds
Array is sorted correctly!

Explanation:
As can be seen above, as the number of threads is increased, the execution time decreases.
However, as per Amdahls' Law, this rate of increased efficiency is not linear. Rather,
the first few threads result in relatively significant drops in run-time, and the additional
reduction in run time becomes smaller as each new thread is added. My speedups are lower
than the theporetical due to the time taken to jump between processors and because of the
relatively small size of the task being dealt with. It goes without saying that using
multiple threads decreases runtime compared with serial runtime.

Task 2)
Compile:
gcc -o colorize -I. colorize.c ppmIO.c -lm

Run:
./colorize IMG_4203.ppm <num_threads> <num_iterations>

Sample Expected Outputs:
ordansmith@Jordans-MacBook-Air-2 Project8_jhsmit % ./colorize IMG_4203.ppm 1 1000
start: 1702310352
end: 1702310364
Total Elapsed Time for 1000 Iterations: 11.897000 seconds
jordansmith@Jordans-MacBook-Air-2 Project8_jhsmit % ./colorize IMG_4203.ppm 2 1000
start: 1702310373
end: 1702310380
Total Elapsed Time for 1000 Iterations: 6.666000 seconds
jordansmith@Jordans-MacBook-Air-2 Project8_jhsmit % ./colorize IMG_4203.ppm 4 1000
start: 1702310385
end: 1702310388
Total Elapsed Time for 1000 Iterations: 3.740000 seconds
jordansmith@Jordans-MacBook-Air-2 Project8_jhsmit % ./colorize IMG_4203.ppm 8 1000
start: 1702310393
end: 1702310396
Total Elapsed Time for 1000 Iterations: 2.975000 seconds
jordansmith@Jordans-MacBook-Air-2 Project8_jhsmit % 

Explanation:
What the terminal commands above reveal is that as the number of threads increases, there
is a proportionate decrease in the runtime when dealing with large datasets (hence why I 
use 1000 iterations of processing). These times, except for the first due to the extra
preparation required to use threads, are faster than the serial runtime, which is consistenly
around 10.426502 seconds as one run showed.


Part 2)
*PLEASE NOTE THAT MY WHOLE PROJECT INCLUDING MY WORK WITH JAVASCRIPT AND MY
    EXTENSIONS WERE COMPLETED INDEPENDENTLY WITH NO ASSISTANCE OF A PARTNER*

Task 1)
For code examples and explanations of parallelism in JavaScript, see my Google Sites.

Task 2)
Compile:
javac PPMFile.java

Run: 
java PPMFile
For output and analysis, see my Google Sites.


Extensions:
N/A