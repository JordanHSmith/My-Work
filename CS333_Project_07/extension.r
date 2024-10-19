# Jordan Smith
# extension.r
# 11/21/23
# Garbage Collection Sweep Detector

# Function to allocate and deallocate memory
allocateMemory <- function() {
  array <- list()

  for (i in 1:100000) {
    array[[i]] <- numeric(1000)
  }

  array <- NULL
}

# Function to measure execution time
measureExecutionTime <- function() {
  start <- Sys.time()

  # Call the function that allocates and deallocates memory
  allocateMemory()

  end <- Sys.time()
  executionTime <- as.numeric(difftime(end, start, units = "secs"))
  return(executionTime)
}

# Perform the experiment multiple times
times <- numeric(30)
endTimes <- numeric(30)

for (i in 1:30) {
  times[i] <- measureExecutionTime()
  if(i==1)
  {
    endTimes[i] = times[i]
  }
  else
  {
    endTimes[i] <- endTimes[i-1] + times[i]
  }

  cat("Execution Time:", times[i], "seconds\n")
}

# Detect Garbage Collection Sweep
for (i in 2:29) {
  if (times[i] > times[i - 1] && times[i] > times[i + 1]) {
    cat("Garbage Collection Sweep at index", i, "and time:", endTimes[i], "\n")
  }
}