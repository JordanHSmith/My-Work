/*
Jordan Smith
task2.js
10/03/23
Implements a binary search on a sorted array
*/

function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2); //Assign middle value

        if (arr[mid] === target) {
            return mid; // Found the target
        } else if (arr[mid] < target) {
            left = mid + 1; // Increase the left boundary
        } else {
            right = mid - 1; // Decrease the right boundary
        }
    }

    return -1; // Target not in array
}

const sortedArray = [2, 4, 7, 10, 13, 19, 23, 29, 34, 45, 56, 67];
const targetValue = 23;
const result = binarySearch(sortedArray, targetValue);

if (result !== -1) {
    console.log(`Found ${targetValue} at index ${result}`);
}
else {
    console.log(`${targetValue} not found in the array.`);
}
