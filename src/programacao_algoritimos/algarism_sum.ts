// 04 — Soma dos algarismos
// Dado um número inteiro positivo, calcule a soma de seus algarismos.
// 12345 → 15

// Não converta o número para string.
// Matemática: divisão inteira e módulo.


export function algarismSum(value: number): void {
  let total = 0;
  let tempNum = value;

  for (let i = 0; tempNum != 0; i++) {
    let restNum = tempNum % 10;
    tempNum = Math.floor(tempNum / 10);
    total = total += restNum;
  }

  console.log("Soma dos algarismos: ", total);
}
