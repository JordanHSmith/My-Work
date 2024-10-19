// Assigning a function to a variable
const add = function(a, b) {
    return a + b;
};
  
const subtract = function(a, b) {
    return a - b;
};

// Passing a function to another function and executing it
function calculate(operation, x, y) {
    return operation(x, y);
}

const result1 = calculate(add, 5, 3);
const result2 = calculate(subtract, 8, 2);

console.log("Result of addition: " + result1);
console.log("Result of subtraction: " + result2);

// Function without a name (anonymous function)
const multiply = function(x, y) {
    return x * y;
};

const result3 = calculate(multiply, 4, 6);

console.log("Result of multiplication: " + result3);
