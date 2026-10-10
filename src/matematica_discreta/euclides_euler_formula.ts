export function euclides(p: number): number {
  const r = primo(p);
  console.log("Primo: ", r);

  if (r === 0) {
    console.log("Não é numero primo");
  }

  const n = 2 ** (p - 1) * r;
  console.log("Resultado da formula: ", n);

  return n;
}

function primo(p: number): number {
  const num = 2 ** p - 1;

  if (num <= 1) return 0;

  if (num === 2) return 0;

  if (num % 2 === 0) return 0;

  const limite = Math.sqrt(num);

  for (let i = 3; i <= limite; i += 2) {
    if (num % i === 0) {
      return 0;
    }
  }

  return num;
}
