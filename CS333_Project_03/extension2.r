# Jordan Smith
# extension2.r
# 10/03/23
# Implements a binary search on a sorted vector

binary_search <- function(sorted_vector, target) {
  left <- 1
  right <- length(sorted_vector)
  
  while (left <= right) {
    mid <- floor((left + right) / 2) #Update middle value
    mid_value <- sorted_vector[mid]
    
    if (mid_value == target) {
      return(mid-1)  # Target found, return its index
    } else if (mid_value < target) {
      left <- mid + 1
    } else {
      right <- mid - 1
    }
  }
  
  return(-1)  # Target not found
}


sorted_vector <- c(1, 3, 8, 7, 9, 11, 13, 16, 17, 19)
target <- 13
result <- binary_search(sorted_vector, target)

if (result != -1) {
  cat("The target", target, "was found at index", result, "\n")
} else {
  cat("The target", target, "was not found in the vector\n")
}
