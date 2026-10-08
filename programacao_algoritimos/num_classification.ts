// Receba um inteiro e determine:

// positivo, negativo ou zero;
// par ou ímpar;
// múltiplo de 3;
// múltiplo de 5;
// múltiplo de ambos.

// Pratica: condicionais e operadores lógicos.

export default function exe(num: bigint, multiply: bigint | bigint[]): void {
  console.log("Entrando na EXE");

  polarity(num);
  parImpar(num);
  multiplyOf(num, multiply);
}

function polarity(num: bigint): void {
  console.log("Executando polaridade");
  num < 0 ? console.log("Negativo") : console.log("Positivo");
}

function parImpar(num: bigint): void {
  console.log("Executando par ou impar");

  if (num % 2n === 0n) {
    console.log("Par: ", num);
  } else {
    console.log("Impar: ", num);
  }
}

function multiplyOf(num: bigint, multiply: bigint | bigint[]): any {
  console.log("Executando multiplos");
  const arr: string[] = num.toString().split("");
  let total: bigint = 0n;

  for (let i = 0; i < arr.length; i++) {
    let digitoAtual: bigint = BigInt(arr[i]);
    total += digitoAtual;
  }

  console.log(`Soma dos numeros para gerar o total de ${total}`);

  const multiplyArray = Array.isArray(multiply) ? multiply : [multiply];

  multiplyArray.forEach((multi, x) => {
    console.log("Iniciando ForEach com o valor: ", multi);
    for (let j: bigint = 0n; j < 20n; j++) {
      console.log(`Multiplicando: ${multi} * ${j} = ${multi * j}`);
      if (total === multi * j) {
        console.log(`${num} é um multiplo de ${multi}`);
        return;
      }
    }
    console.log(`${num} não é um multiplo de ${multi}`);
  });
}

exe(99990n, [3n, 5n]);
