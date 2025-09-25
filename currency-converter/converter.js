// Rates relative to USD
const rates = {
  USD: 1,
  JPY: 113.5,
  EUR: 0.89,
  RUB: 74.36,
  GBP: 0.75
};

// Get form and result div
const form = document.getElementById("converterForm");
const resultDiv = document.getElementById("result");

// Listen to form submit
form.addEventListener("submit", function(e) {
  e.preventDefault(); // Prevent page reload

  // Get values from input
  const from = document.getElementById("fromCurrency").value.trim().toUpperCase();
  const to = document.getElementById("toCurrency").value.trim().toUpperCase();
  const amount = Number(document.getElementById("amount").value.trim());

  // Validation
  if (!rates[from] || !rates[to]) {
    resultDiv.textContent = "Unknown currency";
    return;
  }

  if (isNaN(amount)) {
    resultDiv.textContent = "The amount has to be a number";
    return;
  }

  if (amount < 1) {
    resultDiv.textContent = "The amount cannot be less than 1";
    return;
  }

  // Conversion calculation
  const converted = (amount / rates[from]) * rates[to];

  // Display result on page
  resultDiv.textContent = `${amount} ${from} equals ${converted.toFixed(4)} ${to}`;
});
