def fat(num: int) -> int:
    if num == 1:
        return 1
    else:
        return num * fat(num - 1)


# Some todos os valores do array[]
# Dica: Caso base sempre é o array vazio ou com um valor
def sum(arr: list) -> int:
    copy_arr = list(arr)
    total_value: int = 0

    if not len(copy_arr):
        return 0

    current_element = copy_arr.pop(0)
    total_value = current_element + sum(copy_arr)

    return total_value


# Conte a quantidade de itens em um array
# Dica: Caso base sempre é o array vazio ou com um valor
def count(arr: list) -> int:
    if not len(arr):
        return 0

    arr.pop(0)

    return 1 + count(arr)


# Maior valor dentro de um array
# Dica: Caso base sempre é o array vazio ou com um valor
def biggerValue(arr: list) -> int:
    bigger: int
    
    if len(arr) == 1:
        bigger = arr[0]
        print("Entrou na condição final: ", len(arr))
        return bigger
    
    if arr[0] > arr[1]:
        arr.pop(1)
        print("Entrou na condição do 0 > 1: ", arr)
    else:
        arr.pop(0)
        print("Entrou na condição 0 < 1: ", arr)
        
    return biggerValue(arr)
