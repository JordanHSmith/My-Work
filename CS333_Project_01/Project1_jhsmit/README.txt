CS333 - Project 1 - README
Jordan Smith
09/20/23
Google Sites URL: https://sites.google.com/colby.edu/jordan-smiths-cs333/home

Directory Layout:
Project1_jhsmit
├── README.txt
├── add
├── add.c
├── error
├── error.c
├── struct
├── task1
├── task1.c
├── task2
├── task2.c
├── task3
├── task3.c
├── task4
├── task4.c
├── task5
└── task5.c

Operating System and C Compiler info:
Apple clang version 14.0.3 (clang-1403.0.22.14.1)
Target: arm64-apple-darwin22.6.0

Task 1)
Compile: gcc -o task1 task1.c
Run: ./task1

Expected Output: 
char: 
0: 48

short: 
0: 0A
1: 00

int: 
0: B0
1: 04
2: 00
3: 00

long: 
0: 14
1: 05
2: 00
3: 00
4: 00
5: 00
6: 00
7: 00

double: 
0: 66
1: 66
2: 66
3: 66
4: 66
5: 66
6: 34
7: 40

1.1.a) Is the machine you are using a big-endian or little-endian machine?
The machine is using little-endian.

1.1.b) How does the program output tell you?
The program output tells me that my computer is little-endian because 
the less significant bits are held in the lower indices.

Task 2)
Compile: gcc -o task2 task2.c
Run: ./task2

Expected Output:
0: 70
1: 32
2: 6B
3: 6F
4: 01
5: 00
6: 00
7: 00
8: 12
9: 00
10: 75
11: 6A
12: 04
13: 00
14: 00
15: 00
16: 28
17: 35
18: 6B
19: 6F
20: 01
21: 00
22: 00
23: 00
24: 01
25: 00
26: 00
27: 00
28: 00
29: 00
30: 00
31: 00
32: 00
33: 35
34: 6B
35: 6F
36: 01
37: 00
38: 00
39: 00
40: 28
41: BF
42: 4D
43: 92
44: 01
45: 00
46: 00
47: 00
48: 00
49: 00
50: 00
51: 00
52: 00
53: 00
54: 00
55: 00
56: 00
57: 00
58: 00
59: 00
60: 00
61: 00
62: 00
63: 00
64: 00
65: 00
66: 00
67: 00
68: 00
69: 00
70: 00
71: 00
72: D8
73: DD
74: 94
75: 00
76: 01
77: 00
78: 00
79: 00
80: 00
81: 00
82: 00
83: 40
84: 00
85: 00
86: 00
87: 00
88: C0
89: A0
90: 8B
91: 00
92: 01
93: 00
94: 00
95: 00
96: B0
97: 40
98: 94
99: 00

1.2.a) What happens at the end of the process?
For me, nothing strange happens at the end of the process.

1.2.b) Can you find the variables defined in your C program
I cannot find the variables defined in my C program.

Task 3)
Compile: gcc -o task3 task3.c
Run: ./task3

Expected Output:
N/A (Only meant for observation in the Activity Monitor)

1.3) When not using the free statement, memory requirements ocntinually
increase because the data is not being released properly. When the free
statement is added, however, the memory requirements stay consistent.

Task 4)
Compile: gcc -o task4 task4.c
Run: ./task4

Expected Output:
Byte 0: 0x41
Byte 1: 0x00
Byte 2: 0x2A
Byte 3: 0x00
Byte 4: 0x40
Byte 5: 0xE2
Byte 6: 0x01
Byte 7: 0x00

1.4.a) There was one more byte of data than I expected given the variables
I included.

1.4.b) There are gaps in the way the fields of the struct are laid out
because of the way data is saved in little endian format. This results
in lines of 0's between the values representing the actual values of the
variables.

Task 5)
Compile: gcc -o task4 task4.c
Run: ./task4

Expected Output:
Error due to assigning string too great a length

1.5) My program crashed as a result of passing in a string that was longer
than the memory allocated.

Extensions:

1) 
Compile: gcc -o error error.c
Run: ./error

Expected Output:
Error due to unaligned memory.

For my first extension, I created a file named error.c, which provided a 
short example of a bus error resulting from unaligned memory. The difference between 
this error and a segmentation error is that the bus error attempted to access memory
which the CPU physically cannot access, whereas a segmentation fault is a higher
level problem which is raised when one tries to access memory that has not been
allocated properly.

2)
Compile: gcc -o add add.c
Run: ./add

Expected Output:
inf + 1 = inf

For my second extension, I created a file add.c, which adds one to the predefined
floating point value of infinity found in the math module. The resulting value is
still infinity.

3)
For my third and final extension, I researched a fourth programming language, C++
(See my GoogleSites).