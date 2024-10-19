/*
Jordan Smith
task1.js
11/08/23
Word Frequency Counter
*/

//Grants access to the fs module
const fs = require('fs');

// Read the filename from the command line arguments
const filename = process.argv[2];

if (!filename) {
  console.error('Usage: node task1.js <filename>');
  process.exit(1);
}

// Read the file content
const text = fs.readFileSync(filename, 'utf8');

// Remove punctuation and convert to lowercase
const sanitizedText = text.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, '').toLowerCase();

// Split the text into words
const words = sanitizedText.split(/\s+/);

// Create an object to store word frequencies
const wordFrequency = {};

// Count word frequencies
words.forEach((word) => {
  if (word) {
    wordFrequency[word] = (wordFrequency[word] || 0) + 1;
  }
});

// Convert the word frequency object into an array of word-frequency pairs
const wordFrequencyArray = Object.entries(wordFrequency);

// Sort the word-frequency pairs by frequency in descending order
wordFrequencyArray.sort((a, b) => b[1] - a[1]);

// Print the top 20 words
const top20Words = wordFrequencyArray.slice(0, 20);

console.log('Top 20 words by frequency:');
top20Words.forEach(([word, frequency]) => {
  console.log(`${word}: ${frequency}`);
});
