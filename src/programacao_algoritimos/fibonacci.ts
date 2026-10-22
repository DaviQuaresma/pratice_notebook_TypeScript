// 09 — Sequência de Fibonacci
// Calcule o n-ésimo termo da sequência de Fibonacci.

// Faça inicialmente a solução recursiva simples.

// Depois investigue o comportamento para valores maiores de n.

// Aqui quero que você comece a perceber complexidade na prática.

export function fibonacci(num: number): number {
  if (num === 1) return 1;
  if (num === 0) return 0;

  return fibonacci(num - 1) + fibonacci(num - 2);
}
