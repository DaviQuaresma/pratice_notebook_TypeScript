// 07 — Fatorial
// Implemente:
// n! para n >= 0.
// Depois responda:
// Qual é a complexidade da solução?

export function fatorialFunc(num: number): number {
  const originalNum = num;

  if (originalNum === 0 || originalNum === 1) return 1;

  return (num = num * fatorialFunc(num - 1));
}
