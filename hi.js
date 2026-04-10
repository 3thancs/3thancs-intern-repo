function calculateTotal(items) {
  let total = 0;
  const x = 10; // Unused variable
  for (let i = 0; i < items.length; i++) {
    total += items[i].price;
  }
  if (total > 100) {
    return total * 0.9; // Apply discount
  } else {
    return total;
  }
}

// Example usage
const shoppingCart = [
  { name: 'Shirt', price: 25 },
  { name: 'Jeans', price: 80 },
];

console.log(calculateTotal(shoppingCart));
