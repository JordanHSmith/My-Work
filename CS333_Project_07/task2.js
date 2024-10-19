/*
Jordan Smith
task2.js
11/21/23
Garbage Collection Sweep Detector
*/

//Repeatedly allocates and deallocates memory
function allocateMemory() {
    let array = [];

    // Allocate memory
    for (let i = 0; i < 10000; i++) {
        array.push(new Array(1000));
    }

    // Deallocate memory
    array = null;
}

//Measures time taken to allocate and deallocate memory
function measureExecutionTime() {
    const start = performance.now();

    // Call the function that allocates and deallocates memory
    allocateMemory();

    const end = performance.now();
    const executionTime = end - start;
    return executionTime;
}

const startTime = performance.now();
let times = [];
let endTimes = [];

// Perform the experiment multiple times
for (let i = 0; i < 30; i++) {
    times[i] = measureExecutionTime();
    endTimes[i] = performance.now();
    console.log(`Execution Time: ${times[i]} milliseconds`);
}

//Detect Garbage Collection Sweep
for (let i = 1; i < 29; i++) {
    if(times[i] > times[i-1] && times[i] > times[i+1])
    {
        console.log(`Garbage Collection Sweep at index i: ${i} and time: ${endTimes[i]} milliseconds`);
    }
}
