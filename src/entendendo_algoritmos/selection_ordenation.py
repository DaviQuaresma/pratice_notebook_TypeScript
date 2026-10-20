def search_minor(arr):
    minor = arr[0]
    indice_minor = 0

    for i in range(1, len(arr)):
        if arr[i] < minor:
            minor = arr[i]
            indice_minor = i

    return indice_minor


def ordenation(arr):
    newArr = []
    for i in range(1, len(arr)):
        minor = search_minor(arr)
        newArr.append(arr.pop(minor))
    return newArr
