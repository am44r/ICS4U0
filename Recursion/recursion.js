function doubleCountdownHelper(n) {
  if (n <= 0) return 0;
  console.log(n);
  return doubleCountdownHelper(n - 1);
}

function doubleCountdown(n) {
  doubleCountdownHelper(n);
  doubleCountdownHelper(n - 1);
  console.log(0);
}

doubleCountdown(6);
