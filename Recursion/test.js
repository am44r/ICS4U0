const doubleCountdown = (n, counter=0) => {
  if (n === counter) return 0; 
  console.log(n - counter);
  doubleCountdown(n, counter+1);
  console.log(counter);
  return 1;
}

doubleCountdown(5);