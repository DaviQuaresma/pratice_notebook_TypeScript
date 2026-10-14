// 02 — Maior de três números

// Receba três números e determine o maior sem utilizar Math.max().
// Depois faça uma segunda versão utilizando uma estrutura iterativa.
// Pratica: condicionais → generalização.

export function biggerOfThree(numbers: number[]) {
  let bigger: number = 0;

  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > bigger) {
      bigger = numbers[i];
      console.log("Novo maior da lista: ", bigger);
    } else {
      console.log(numbers[i], " não é maior que ", bigger);
    }
  }

  console.log("Maior numero da lista: ", bigger);
}
