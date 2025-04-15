// TUAZON, FRANCESCA MARIE A. (BCS24)

/**
Declare six variables, remembering to name them according to their purpose:
• the price of a single rose (8) and the number of roses you have (70)
• the price of a single lily (10) and the number of lilies you have (50)
• the price of a single tulip (2) and the number of tulips you have (120)
Now declare three variables, one each for the roses, lilies, and tulips you have, in which you place their total price. Insert the corresponding values into the variables using the variables declared in the previous step. Finally, declare a variable in which you store the price of all your flowers (again, use the previous variables for initialization).

Update the given program and add the following requirements:
Additional Flowers, Price per unit and Quantity
• the price of a single sampaguita (5) and the number of sampaguita you have (20)
• the price of a single gerbera (25) and the number of gerbera you have (24)

**/

const rosePrice = 8;
const lilyPrice = 10;
const tulipPrice = 2;
const sampaguitaPrice = 5;
const gerbaraPrice = 25;

let numberOfRoses = 70;
let numberOfLilies = 50;
let numberOfTulips = 120;
let numberOfSampaguita = 20;
let numberOfGerbara = 24;

let rosesValue = rosePrice * numberOfRoses;
let liliesValue = lilyPrice * numberOfLilies;
let tulipsValue = tulipPrice * numberOfTulips;
let sampaguitaValue = sampaguitaPrice * numberOfSampaguita;
let gerbaraValue = gerbaraPrice * numberOfGerbara

let total = rosesValue + liliesValue + tulipsValue + sampaguitaValue + gerbaraValue;

console.log("Rose – unit price:", rosePrice, ", quantity:", numberOfRoses, ", value:", rosesValue);
console.log("Lily – unit price:", lilyPrice, ", quantity:", numberOfLilies, ", value:", liliesValue);
console.log("Tulip – unit price:", tulipPrice, ", quantity:", numberOfTulips, ", value:", tulipsValue);
console.log("Sampaguita – unit price:", sampaguitaPrice, ", quantity:", numberOfSampaguita, ", value:", sampaguitaValue);
console.log("Gerbara – unit price:", gerbaraPrice, ", quantity:", numberOfGerbara, ", value:", gerbaraValue);
console.log("Total: ", total);

