# Jordan Smith
# extension3.r
# 10/03/23
# Demonstrates data types

# Numeric data type
num1 <- 5
num2 <- 2
result_numeric <- num1 + num2
cat("Numeric Addition: ", result_numeric, "\n")

# Character data type
str1 <- "Hello, "
str2 <- "World!"
result_character <- str1
result_character <- paste(result_character, str2) #concatenates strings
cat("Character Concatenation: ", result_character, "\n")

# Logical data type
logical1 <- TRUE
logical2 <- FALSE
result_logical_and <- logical1 & logical2
result_logical_or <- logical1 | logical2
cat("Logical AND: ", result_logical_and, "\n")
cat("Logical OR: ", result_logical_or, "\n")

# Complex data type
complex1 <- 3 + 2i
complex2 <- 1 - 4i
#adds the whole and imaginary numbers seperately
result_complex_add <- complex1 + complex2
cat("Complex Addition: ", result_complex_add, "\n")

# Vector
vector1 <- c(1, 2, 3, 4, 5)
vector2 <- c(6, 7, 8, 9, 10)
#adds each element of one vector to the corresponding element in the other vector
result_vector_addition <- vector1 + vector2
cat("Vector Addition: ", result_vector_addition, "\n")

# List
list1 <- list(name = "John", age = 30, city = "New York")
list2 <- list(name = "Alice", age = 25, city = "Los Angeles")
result_list_concatenation <- c(list1, list2) #combines the lists together
cat("List Concatenation: \n")
print(result_list_concatenation)

# Data Frame
df1 <- data.frame(name = c("John", "Alice"), age = c(30, 25))
df2 <- data.frame(name = c("Bob", "Eve"), age = c(35, 28))
result_df_merge <- rbind(df1, df2) #Merges the dataframes together
cat("Data Frame Merge: \n")
print(result_df_merge)
