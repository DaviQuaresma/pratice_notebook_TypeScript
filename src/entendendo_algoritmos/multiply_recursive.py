def multiply_table(numbers: list[int], i: int = 0, j: int = 0):

    if i >= len(numbers):
        return

    if j >= len(numbers):
        multiply_table(numbers, i + 1, 0)
        return

    print(f"{numbers[i]} * {numbers[j]} = {numbers[i] * numbers[j]}")

    multiply_table(numbers, i, j + 1)
