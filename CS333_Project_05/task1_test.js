/*
Jordan Smith
task1_test.js
10/25/23
Test file for Linked List
*/

// Import the linked list implementation
const { LinkedList } = require('./linkedlist'); // Replace with the correct path to your linked list implementation

//Functions to be mapped
function printInt(data) {
    console.log("int value: " + data);
}

function squareInt(data) {
    return data * data;
}

function compInt(i, j) {
    return i === j;
}

function printDouble(data) {
    console.log("double value: " + data);
}

function squareDouble(data) {
    return data * data;
}

function compDouble(i, j) {
    return i === j;
}

//Beginning of test code
let l = LinkedList.ll_create();
let l2 = LinkedList.ll_create();

for (let i = 0; i < 20; i += 2) {
    l.ll_push(i);
}

for (let j = 1.5; j < 20.0; j += 1.5) {
    l2.ll_push(j);
}

console.log("After initialization");
l.ll_map(printInt);
l2.ll_map(printDouble);

l.ll_map(squareInt);
l2.ll_map(squareDouble);

console.log("\nAfter squaring");
l.ll_map(printInt);
l2.ll_map(printDouble);

let intTarget = 16;
let a = l.ll_remove(intTarget, compInt);
if (a !== null) {
    console.log("\nRemoved integer: " + a);
} else {
    console.log("\nNo instance of integer " + intTarget);
}

intTarget = 11;
a = l.ll_remove(intTarget, compInt);
if (a !== null) {
    console.log("\nRemoved integer: " + a);
} else {
    console.log("\nNo instance of integer " + intTarget);
}

let doubleTarget = 6.75;
let d = l2.ll_remove(doubleTarget, compDouble);
if (d !== null) {
    console.log("\nRemoved double: " + d);
} else {
    console.log("\nNo instance of double " + doubleTarget);
}

doubleTarget = 10.5;
d = l2.ll_remove(doubleTarget, compDouble);
if (d !== null) {
    console.log("\nRemoved double: " + d);
} else {
    console.log("\nNo instance of double " + doubleTarget);
}

console.log("\nAfter removals");
l.ll_map(printInt);
l2.ll_map(printDouble);

l.ll_append(intTarget);
l2.ll_append(doubleTarget);

console.log("\nAfter append");
l.ll_map(printInt);
l2.ll_map(printDouble);

l.ll_clear(null);
l2.ll_clear(null);

console.log("\nAfter clear");
l.ll_map(printInt);
l2.ll_map(printDouble);

for (let i = 0; i < 5; i++) {
    l.ll_append(i);
}

for (let j = 0.5; j < 5.0; j += 0.5) {
    l2.ll_append(j);
}

console.log("\nAfter appending");
l.ll_map(printInt);
l2.ll_map(printDouble);
