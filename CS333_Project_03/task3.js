/*
Jordan Smith
task3.js
10/03/23
Demonstrates data types
*/

const numberType = 42; // number
const stringType = "Hello, World!"; // string
const booleanType = true; // boolean
const nullType = null; // null - does not have a place for value to be stored
const undefinedType = undefined; // undefined - value not yet assigned
const arrayType = [1, 2, 3, 4, 5]; // array

// Makes an object
const objectType = {
  name: "John",
  age: 30,
  isStudent: false,
}; // Object

// Defines a function
function add(a, b) {
  return a + b;
}

// Demonstrating Operators and Their Resulting Types
const resultAdd = numberType + numberType; // number
const resultSubtract = numberType - numberType; // number
const resultMultiply = numberType * numberType; // number
const resultDivide = numberType / numberType; // number
const resultModulo = numberType % 5; // number

const resultStringConcat = stringType + " JavaScript"; // string

const resultBooleanAnd = booleanType && true; // boolean
const resultBooleanOr = booleanType || false; // boolean

const resultArrayIndex = arrayType[2]; // number

const resultObjectProperty = objectType.name; // string

const resultFunctionCall = add(5, 3); // number

//Displays results
console.log("Addition: " + resultAdd);
console.log("Subtraction: " + resultSubtract);
console.log("Multiplication: " + resultMultiply);
console.log("Division: " + resultDivide);
console.log("Modulo: " + resultModulo);
console.log("String Concatenation: " + resultStringConcat);
console.log("Logical AND: " + resultBooleanAnd);
console.log("Logical OR: " + resultBooleanOr);
console.log("Array Indexing: " + resultArrayIndex);
console.log("Object Property Access: " + resultObjectProperty);
console.log("Function Call: " + resultFunctionCall);
