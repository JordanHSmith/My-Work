# Defining anonymous functions and assigning them to variables
add <- function(x, y) {
  return(x + y)
}

subtract <- function(x, y) {
  return(x - y)
}

multiply <- function(x, y) {
  return(x * y)
}

# Passing a function to another function
calculate <- function(func, a, b) {
  result <- func(a, b)
  return(result)
}

result1 <- calculate(add, 5, 3)
cat("Result of addition:", result1, "\n")

result2 <- calculate(subtract, 8, 2)
cat("Result of subtraction:", result2, "\n")

result3 <- calculate(multiply, 4, 6)
cat("Result of multiplication:", result3, "\n")
