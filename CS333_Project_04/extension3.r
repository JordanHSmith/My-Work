# Generic Quick Sort function
quickSort <- function(arr, order = "ascending") {
  if (length(arr) <= 1) {
    return(arr)
  }
  
  mid <- arr[1]
  less <- arr[arr < mid] #Assigns all values less than mid to less
  equal <- arr[arr == mid] #Assigns all values equal to mid
  greater <- arr[arr > mid] #Assigns all values greater than mid to greater
  
  #Recursively sorts values
  if (order == "ascending") {
    return(c(quickSort(less, "ascending"), equal, quickSort(greater, "ascending"))
    )
  } else if (order == "descending") {
    return(c(quickSort(greater, "descending"), equal, quickSort(less, "descending"))
    )
  } else {
    stop("Invalid order. Use 'ascending' or 'descending'.")
  }
}

# Test the quickSort function with different data types

# Sorting integers in ascending order
numbersAsc <- c(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
cat("Sorting integers in ascending order: ", quickSort(numbersAsc, "ascending"), "\n")

# Sorting integers in descending order
numbersDesc <- c(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
cat("Sorting integers in descending order: ", quickSort(numbersDesc, "descending"), "\n")

# Sorting strings in ascending order
stringsAsc <- c("banana", "apple", "fig", "cherry", "date", "grape")
cat("Sorting strings in ascending order: ", quickSort(stringsAsc, "ascending"), "\n")

# Sorting strings in descending order
stringsDesc <- c("banana", "apple", "fig", "cherry", "date", "grape")
cat("Sorting strings in descending order: ", quickSort(stringsDesc, "descending"), "\n")
