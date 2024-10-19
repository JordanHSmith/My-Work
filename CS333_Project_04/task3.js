function quickSort(arr, order = 'ascending') {
  //Return the original array if it is empty or only has one element
  if (arr.length <= 1) {
    return arr;
  }

  //Establish initial conditions for search
  const mid = arr[Math.floor(arr.length / 2)];
  const left = [];
  const right = [];

  //Compare elements to determine if they should be placed to the left or right
  for (const element of arr) {
    if (element < mid) {
      left.push(element);
    } else if (element > mid) {
      right.push(element);
    }
  }

  //Function calls itself recursively dependent on the type of sort inputted
  if (order === 'ascending') {
    return quickSort(left, 'ascending').concat(mid, quickSort(right, 'ascending'));
  } else if (order === 'descending') {
    return quickSort(right, 'descending').concat(mid, quickSort(left, 'descending'));
  } else {
    throw new Error('Invalid order. Use "ascending" or "descending".');
  }
}

const numbersAsc = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
console.log("Sorting integers in ascending order:", quickSort(numbersAsc, 'ascending'));

const numbersDesc = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
console.log("Sorting integers in descending order:", quickSort(numbersDesc, 'descending'));

const stringsAsc = ["banana", "apple", "fig", "cherry", "date", "grape"];
console.log("Sorting strings in ascending order:", quickSort(stringsAsc, 'ascending'));

const stringsDesc = ["banana", "apple", "fig", "cherry", "date", "grape"];
console.log("Sorting strings in descending order:", quickSort(stringsDesc, 'descending'));
