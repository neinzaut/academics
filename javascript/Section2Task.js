// TUAZON, FRANCESCA MARIE A.

// TASK 1: Write a code that will create variables and initialize them with values of Boolean, Number, BigInt, String, and undefined types using (when possible) literals and constructor functions.

let status1 = true;
let status2 = Boolean(true);

let rate1 = 100;
let rate2 = Number(200);

let tuition1 = 100n;
let tuition2 = BigInt(200);

let greeting1 = "Hello";
let greeting2 = String("Hello");

let temp = undefined;

// TASK 2: Print all values and all types of those values using console.log. Try to use string interpolation to display the value and type at the same time with a single console.log call, e.g. in the following form: 1000 [number].

console.log(`${status1} [${typeof status1}]`);
console.log(`${status2} [${typeof status2}]`);
console.log(`${rate1} [${typeof rate1}]`);
console.log(`${rate2} [${typeof rate2}]`);
console.log(`${tuition1} [${typeof tuition1}]`);
console.log(`${tuition2} [${typeof tuition2}]`);
console.log(`${greeting1} [${typeof greeting1}]`);
console.log(`${greeting2} [${typeof greeting2}]`);
console.log(`${temp} [${typeof temp}]`);

// TASK 3: Carry out a chain of conversions: create a Boolean from a BigInt created from a Number that was created from a String. Start with the value "1234". Is it possible?

let x = Boolean( BigInt(Number("1234")));
console.log(`${x} [${typeof x}]`);

// TASK 4: Try adding two values of the same type and check the result type. Try it for all primitive types.
let status = true + false; // boolean
let num = 100 + 200; // integer
let bi = 100n + 200n; // bigint
let greet = "He" + "llo"; // strings
let un = undefined + undefined; // undefined

console.log(`${status} [${typeof status}]`); // type turns into a number
console.log(`${num} [${typeof num}]`);
console.log(`${bi} [${typeof bi}]`);
console.log(`${greet} [${typeof greet}]`);
console.log(`${un} [${typeof un}]`); // type turns into a number

// TASK 5: Try adding two values of different types and check the results.
// TASK 5: Try adding two values of different types and check the results.

// boolean - throws errors when added with bigint
let boo_num1 = true + 100;      //int
let boo_num2 = true + "100";    //string

// int - throws errors when added to bigint
let num1 = 100 + true;          //boolean
let num2 = 100 + "200";         //string

// bigint - throws errors when added to integer and boolean
let bi1 = 100n + "200";         //string

// string - fits with any of the following data types
let s1 = "100" + 200;           //int
let s2 = "100" + 200n;          //bigint
let s3 = "100" + true;          //boolean
let s4 = "abc" + 200;           //int
let s5 = "abc" + 200n;          //bigint
let s6 = "abc" + true;          //boolean

console.log(`${boo_num1} [${typeof boo_num1}]`);   
console.log(`${boo_num2} [${typeof boo_num2}]`);   

console.log(`${num1} [${typeof num1}]`); 
console.log(`${num2} [${typeof num2}]`); 

console.log(`${bi1} [${typeof bi1}]`); 

console.log(`${s1} [${typeof s1}]`);   
console.log(`${s2} [${typeof s2}]`); 
console.log(`${s3} [${typeof s3}]`);  
console.log(`${s4} [${typeof s4}]`);   
console.log(`${s5} [${typeof s5}]`);  
console.log(`${s6} [${typeof s6}]`);    


// TASK 6: Try to modify the line const str1 = 42 + "1"; to get the result 43 (without removing the quotes around 1).
const str1 = 42 + +"1";
console.log(str1)