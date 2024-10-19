# if-else statement
x <- 10
if (x > 5) {
  cat("x is greater than 5\n")
} else {
  cat("x is not greater than 5\n")
}

cat("\n")

# for loop that prints integers 1 through 5
for (i in 1:5) {
  cat("For loop iteration ", i, "\n")
}

cat("\n")

# while loop
j <- 1
# Iterates while condition is true
while (j <= 5) {
  cat("While loop iteration ", j, "\n")
  j <- j + 1
}

cat("\n")

# repeat and break statement
k <- 1

# Will only end if the break command is called
repeat {
  cat("Repeat loop iteration ", k, "\n")
  k <- k + 1
  if (k > 5) { 
    break
  }
}

cat("\n")

# next statement
for (i in 1:5) {
  if (i == 3) {
    next  # Skip the iteration when i is 3
  }
  cat("For loop (with 'next') iteration ", i, "\n")
}
