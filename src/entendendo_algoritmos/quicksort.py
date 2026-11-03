

def qsort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        minors: list = []
        majors: list = []
        
        for i in arr[1:]:
            if i <= pivo:
                print(f"Elemento {i} menor que o Pivo {pivo}")
                minors.append(i)
            if i > pivo:
                print(f"Elemento {i} maior que o Pivo {pivo}")
                majors.append(i)
    
    return qsort(minors) + [pivo] + qsort(majors)