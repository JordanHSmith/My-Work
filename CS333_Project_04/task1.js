// If-Else Statement
let x = 10;
let y = 5;

//Prints based on numerical values x and y
if (x > y) {
  console.log("x is greater than y.");
} else {
  console.log("x is not greater than y.");
}

console.log("");

// Switch Statement
let dayOfWeek = 3;

//prints Wednesday because value of dayOfWeek matches value of the case
switch (dayOfWeek) {
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  case 3:
    console.log("Wednesday");
    break;
  default:
    console.log("Unknown day");
}

console.log("");

// While Loop
let i = 1;

//Runs so long as condition is satisfied
while (i <= 5) {
  console.log("While loop iteration " + i);
  i++;
}

console.log("");

// Do-While Loop
let j = 1;

//Will print code within the do block before checking the condition
do {
  console.log("Do-While loop iteration " + j);
  j++;
} while (j <= 5);

console.log("");

// For Loop
for (let k = 1; k <= 5; k++) {
  console.log("For loop iteration " + k);
}

console.log("");

// For-In Loop (for iterating over object properties)
const person = {
  name: "John",
  age: 30,
  city: "New York"
};

//Iterates through each property in person and its correspodning value
for (let prop in person) {
  console.log(prop + ": " + person[prop]);
}

console.log("");

// For-Of Loop (for iterating over arrays and iterable objects)
const colors = ["red", "green", "blue"];

//Iterates through each color in colors
for (let color of colors) {
  console.log("For-Of loop: " + color);
}

console.log("");

// Break and Continue Statements
for (let m = 1; m <= 10; m++) {
  if (m % 2 === 0) {
    continue; // Skip even numbers
  }
  if (m === 7) {
    break; // Exit the loop when m is 7
  }
  console.log("Current value of m: " + m);
}
