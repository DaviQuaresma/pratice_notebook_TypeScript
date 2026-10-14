// 03 — Conversão de segundos
// Receba uma quantidade de segundos e converta para:

// horas
// minutos
// segundos

// Exemplo:
// 3671 → 1h 1min 11s

// Matemática: divisão inteira e resto.

export function conversor(timeInSeconds: number): string {
  let minuts = 0;
  let hours = 0;
  let seconds = timeInSeconds;
  let secondsLeft = 0;
  let minutsLeft = 0;

  minuts = Math.floor(seconds / 60);
  secondsLeft = Math.floor(seconds % 60);
  hours = Math.floor(minuts / 60)
  minutsLeft = Math.floor(minuts % 60);

  return `${hours}h ${minutsLeft}min ${secondsLeft}s`;
}
