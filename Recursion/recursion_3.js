/*
Given a string, calculate the amount of mirrordromes that 
exist within a given string (including single letter mirrors).

A mirrordrome is a word that can be mirrored if cut in half and folded over on itself.

Single letters that are considered mirrors in this program include:
i, l, m, n, o, t, u, v, w, x

Letters that are considered mirrored opposites in this program include:
b <-> d, p <-> q, s <-> z

Examples:
If you ran iterativeCalculate("dob") you would get a return value of 2 ("dob" and "o" are both mirrordromes).
If you ran recursiveCalculate("totally") you would get a return value of 7 ("t", "t", "o", "l", "l", "ll", and "tot" are all mirrordromes)
*/

const singleLetterMirrors = ['i', 'l', 'm', 'n', 'o', 't', 'i', 'v', 'w', 'x'];
const mirrorOpposites = ['b', 'p', 's', 'q', 'd', 'z'];


const checkMirrors = (string, mirrorArr = singleLetterMirrors) => {
  console.log(string);
  if (string === '') return `no mirrors`;
  if (string.includes(mirrorArr[0])) {
    let indexOfLetter = string.indexOf(mirrorArr[0]);
    return checkMirrors(string.replace(indexOfLetter, ''), mirrorArr.slice(1));
  }
  return checkMirrors(string.slice(1), mirrorArr.slice(1));
};

checkMirrors('uandom')