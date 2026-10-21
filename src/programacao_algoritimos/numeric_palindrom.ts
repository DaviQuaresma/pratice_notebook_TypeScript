// 06 — Palíndromo numérico
// Determine se um número é palíndromo.
// 1221 → true
// 1234 → false

import { numInvert } from "./number_invert";

export function palindrom(num: number): string {
  const originalNum = num;
  const invertedNum = numInvert(num);

  if (originalNum === invertedNum) {
    return `O numero original ${originalNum} é um palindromo`;
  } else {
    return `O numero original ${originalNum} é diferente dele invertido ${invertedNum}, portanto não é um palindromo`;
  }
}
