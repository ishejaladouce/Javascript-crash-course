// Use prompt-sync for local testing instead of sync-input
const prompt = require('prompt-sync')();

console.log("Welcome to Currency Converter!");
console.log("1 USD equals 1 USD");
console.log("1 USD equals 113.5 JPY");
console.log("1 USD equals 0.89 EUR");
console.log("1 USD equals 74.36 RUB");
console.log("1 USD equals 0.75 GBP");
console.log("I can convert USD to these currencies: JPY, EUR, RUB, USD, GBP");
console.log("Type the currency you wish to convert: USD");

const to = prompt("To: ").trim().toUpperCase();

const rates = {
  JPY: 113.5,
  EUR: 0.89,
  RUB: 74.36,
  USD: 1,
  GBP: 0.75
};

if (!Object.prototype.hasOwnProperty.call(rates, to)) {
  console.log("Unknown currency");
  process.exit(0);
}

const amountStr = prompt("Amount: ").trim();
const amount = Number(amountStr);

if (isNaN(amount)) {
  console.log("The amount has to be a number");
  process.exit(0);
}

if (amount < 1) {
  console.log("The amount cannot be less than 1");
  process.exit(0);
}

const converted = amount * rates[to];
console.log(`Result: ${amount} USD equals ${converted.toFixed(4)} ${to}`);
