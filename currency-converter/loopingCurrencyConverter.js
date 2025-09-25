const prompt = require('prompt-sync')();

// define currency rates
const rates = {
  USD: 1,
  JPY: 113.5,
  EUR: 0.89,
  RUB: 74.36,
  GBP: 0.75
};

// welcome message and exchange rates
console.log("Welcome to Currency Converter!");
console.log("1 USD equals 1 USD");
console.log("1 USD equals 113.5 JPY");
console.log("1 USD equals 0.89 EUR");
console.log("1 USD equals 74.36 RUB");
console.log("1 USD equals 0.75 GBP");

// start infinite loop to keep program running and then get user choice
while (true) {
    
    console.log("What do you want to do?");
    console.log("1-Convert currencies 2-Exit program");
    const choice = prompt("> ").trim(); 
    
    // exit the loop and program
    if (choice === "2") {
        console.log("Have a nice day!");
        break; 
    }
    
    // Step 4c: handle conversion
    else if (choice === "1") {
        // ask from which currency
        console.log("What do you want to convert?");
        const from = prompt("From: ").trim().toUpperCase();
        if (!rates[from]) {
            console.log("Unknown currency");
            continue; // go back to main menu
        }
        
        // ask to which currency
        const to = prompt("To: ").trim().toUpperCase();
        if (!rates[to]) {
            console.log("Unknown currency");
            continue; 
        }
        
        // ask amount
        const amountStr = prompt("Amount: ").trim();
        const amount = Number(amountStr);
        if (isNaN(amount)) {
            console.log("The amount has to be a number");
            continue;
        }
        if (amount < 1) {
            console.log("The amount cannot be less than 1");
            continue;
        }
        
        // calculate conversion
        const converted = (amount / rates[from]) * rates[to];
        console.log(`Result: ${amount} ${from} equals ${converted.toFixed(4)} ${to}`);
    }
    
    // unknown input: go back to the main menu
    else {
        console.log("Unknown input");
    }
}
