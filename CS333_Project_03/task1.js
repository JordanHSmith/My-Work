/*
Jordan Smith
task1.js
10/03/23
Demonstrates scope in JavaScript
*/

var globalVar = "I'm a global variable"; //variables declared outside functions have global level scope

function exampleScope() {
  var localVar = "I'm a function-scoped variable"; //"var" keyword provides function level scope
  if (true) {
    // Block scope (inside if statement)
    let blockVar = "I'm a block-scoped variable"; //"let" keyword provides block level scope
    const PI = 3.14159; /*"const" keyword makes a constant, which has block level scope and cannot have
                        its value changed*/
    console.log(globalVar); 
    console.log(localVar);  
    console.log(blockVar);  
    console.log(PI);        

    localVar = "I can be reassigned within the function.";
  }
  console.log(localVar); // Can still access reassigned variable
}

exampleScope();

globalVar = "I've been reassigned globally.";
console.log(globalVar); // Can still access reassigned global variable
