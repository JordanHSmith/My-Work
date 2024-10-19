# Jordan Smith
# extension1.r
# 10/03/23
# Demonstrates scope in R

# Declare a global variable
global_var <- 42

# Demonstrate variable scoping
variable_scope_demo <- function() {
  local_var <- 10
  
  # Access the global variable from within the function
  cat("Accessing global_var within the function: ", global_var, "\n")
  
  # Access the local variable within the function
  cat("Accessing local_var within the function: ", local_var, "\n")
}

variable_scope_demo()

# Variable naming demonstration with "."
my.identifier <- "This is a valid identifier"
.valid123 <- "Another valid identifier"

#Demonstrate same variable can hold int and string
global_var <- "Now I'm a string!"

cat("Value of global_var: ", global_var, "\n")
cat("Value of my.identifier: ", my.identifier, "\n")
cat("Value of .valid123: ", .valid123, "\n")
