const Currency = {
    USD: 1,
    JPY: 113.5,
    EUR: 74.36,
    GBP: 0.75
};

console.log("Welcome to currency convertor");

for (const k in Currency) {
    console.log(`1 USD equals ${Currency[k]} ${k}`);
}
