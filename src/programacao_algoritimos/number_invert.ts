// 05 — Inversão de número
// Receba um número inteiro e produza seu reverso.
// 12345 → 54321
// Novamente, sem converter para string.

export function numInvert(number: number) {
  let invertedNum = 0;
  let tempNum = number;

  for (let i = 0; tempNum > 0; i++) {
    let last = lastDigit(tempNum);
    let totalDigitos = Math.floor(Math.log10(Math.abs(tempNum)));
    invertedNum += last * 10 ** totalDigitos;
    tempNum = Math.floor(tempNum / 10);
    console.log(`(${last} X 10 ** ${totalDigitos})`);
  }

  console.log(invertedNum);
}

function lastDigit(num: number): number {
  let last = 0;
  last = num % 10;
  return last;
}
