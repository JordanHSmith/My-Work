# Jordan Smith
# extension1.r
# 11/08/23
# Word Frequency Counter in R

# Read the filename from the command line
args <- commandArgs(trailingOnly = TRUE)

# User message for incorrect iput
if (length(args) == 0) {
  cat("Usage: Rscript extension1.R <filename>\n")
  quit(status = 1)
}

filename <- args[1]

# Read the file content
text <- tolower(readLines(filename, warn = FALSE))

# Combine the lines into a single string
text <- paste(text, collapse = " ")

# Remove punctuation
text <- gsub("[[:punct:]]", " ", text)

# Tokenize the text into words
words <- unlist(strsplit(text, "\\s+"))

# Create a table of word frequencies
word_table <- table(words)

# Sort the table by frequency in descending order
sorted_word_table <- sort(word_table, decreasing = TRUE)

# Print out top twenty words and corresponding counts
for(i in 1:20){
    word = names(sorted_word_table)[i]
    cat(word, ":", sorted_word_table[word], "\n")
}