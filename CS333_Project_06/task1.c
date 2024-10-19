/*
Jordan Smith
task1.c
11/08/23
Word Frequency Counter
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stddef.h>

#define MAX_WORD_LEN 50  // Maximum word length (adjust as needed)
#define MAX_WORDS 1000   // Maximum number of unique words to count

// Define a struct to hold word-frequency pairs
typedef struct {
    char word[MAX_WORD_LEN];
    int count;
} WordFrequency;

// Function to normalize a word by converting it to lowercase and removing punctuation
void normalizeWord(char *word) {
    int len = strlen(word);
    for (int i = 0; i < len; i++) {
        if (ispunct(word[i]))
            memmove(&word[i], &word[i + 1], len - i);
        else
            word[i] = tolower(word[i]);
    }
}

// Function to find a word's index in the WordFrequency array
int findWordIndex(char *word, WordFrequency *wordFreqArray, int wordCount) {
    for (int i = 0; i < wordCount; i++) {
        //Checks if word variable is equal to the word at index i of wordFreqArray
        if (strcmp(word, wordFreqArray[i].word) == 0) {
            return i;
        }
    }
    //Not in array
    return -1;
}

// Compare function for qsort to sort WordFrequency array by count
int compareWordFrequency(const void *a, const void *b) {
    return ((WordFrequency*)b)->count - ((WordFrequency*)a)->count;
}

int main(int argc, char *argv[]) {
    // Usage statement
    if (argc != 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    // Open file
    char *filename = argv[1];
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Create array to hold word-occurence pairs
    WordFrequency wordFreqArray[MAX_WORDS];
    int wordCount = 0;

    // Stores word in the file into word variable
    char word[MAX_WORD_LEN];
    while (fscanf(file, "%s", word) == 1) {
        // Preprocessing
        normalizeWord(word);

        int index = findWordIndex(word, wordFreqArray, wordCount);
        //If not in array
        if (index == -1) {
            if (wordCount < MAX_WORDS) {
                strcpy(wordFreqArray[wordCount].word, word);
                wordFreqArray[wordCount].count = 1;
                wordCount++;
            }
        } else { //If in array
            wordFreqArray[index].count++;
        }
    }

    fclose(file);

    // Puts words in order of frequency
    qsort(wordFreqArray, wordCount, sizeof(WordFrequency), compareWordFrequency);

    // Prints out top twenty words
    int printCount = wordCount < 20 ? wordCount : 20;
    for (int i = 0; i < printCount; i++) {
        printf("%s: %d\n", wordFreqArray[i].word, wordFreqArray[i].count);
    }

    return 0;
}
