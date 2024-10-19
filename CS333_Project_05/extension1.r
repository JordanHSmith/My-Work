# Jordan Smith
# extension1.r
# 10/25/23
# Haiku to demonstrate Polymorphism


# Define a function that demonstrates function overloading
polymorphism <- function(x) {
  if (is.numeric(x)) {
    return(paste("Received a number"))
  } else if (is.character(x)) {
    return(paste("Received a string:", x))
  } else {
    return("Received something else")
  }
}

# Call the function with different argument types
result1 <- polymorphism(42)
result2 <- polymorphism("Hello, R!")
result3 <- polymorphism(TRUE)

# Print the results
cat(result1, "\n")
cat(result2, "\n")
cat(result3, "\n")
