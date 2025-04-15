// Tuazon, Francesca Marie A. (BCS24)

let items = [
    {
        product: "Nutella",
        quantity: 3,
        price: 500
    },
    {
        product: "Gummy Bears",
        quantity: 4,
        price: 100
    }
];

// User Input via Prompt Dialog Box; loop was used to reuse the code
for (let x = 1; x < 3; x++) { 
    let product_input = window.prompt("Product Name: ");
    let quantity_input = parseInt(window.prompt("Quantity: ")); // converts input to number
    let price_input = parseInt(window.prompt("Price: ")); // converts input to number

    items.push({
        product: product_input,
        quantity: quantity_input,
        price: price_input
    });
}

let amount_due = 0;

// Get end of the array
let last = items.length;

// Formula for Total and Amount Due
for (let y = 0; y < last; y++) {
    let total = items[y].quantity * items[y].price;
    amount_due += total;
    items[y].total = total; 
}

// Initialize variable to be printed in the Alert Dialog Box
let output = "Product  /  Quantity  /  Price  /  Total\n";
for (let z = 0; z < last; z++) {
    output += "\n" + items[z].product + " / " + items[z].quantity + " / " + items[z].price + " / " + items[z].total;
}
output += "\n"
output += "\nTotal Amount Due: " + amount_due;

alert(output);
