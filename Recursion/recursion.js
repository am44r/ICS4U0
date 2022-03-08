// const doubleCountdownHelper = n => {
//   if (n <= 0) return 0;
//   console.log(n);
//   return doubleCountdownHelper(n - 1);
// }

// const doubleCountdown = n => {
//   doubleCountdownHelper(n);
//   doubleCountdownHelper(n - 1);
//   console.log(0);
// }

// doubleCountdown(6);
const doubleCountdown = (n, cycle=1) => {
  if (n <= 0) return 0;
  if (cycle===0) return doubleCountdown(n-1);
  console.log(n);
  return doubleCountdown(n-1);
}

console.log(doubleCountdown(5));

