const combo = [3, 7, 2, 9, 5];
let max = combo[0];
for (let i = 1; i < combo.length; i++) {
  if (combo[i] > max) {
    max = combo[i];
  }
}
console.log(max);
