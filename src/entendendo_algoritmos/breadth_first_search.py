from collections import deque

# fun auxiliar de validação fraca ( só para exemplo de codigo ) pois os campos mudam de ordem e vai achar qual deles é um bool para usar como parametro de condição
def is_seller(person: tuple):
    elements = list(person)
    
    for element in elements:
        if type(element) == bool:
            if element: 
                return True
            break
            
    return elements[1]

def breadth_first():
    
    grafo = {}
    
    grafo["me"] = [{"Joyce", False}, {"Victor", False}, {"Arthur", False}]
    grafo["Joyce"] = [{"Nina", False}, {"Thais", False}, {"Ellen", False}]
    grafo["Victor"] = [{"Marone", False}, {"Judeu", False}]
    grafo["Arthur"] = [{"Adriele", True}]
    
    queue_of_search = deque()
    queue_of_search += grafo["me"]
    
    # Enquanto a fila não estiver vazia
    while queue_of_search:
        # Primeira pessoa da fila
        person: tuple = queue_of_search.popleft()
        # Valida que é o vendedor a partir de um bool
        result = is_seller(person)
        
        if type(result) == bool and result:
            return True
        else:
            if result in grafo:
                queue_of_search += grafo[result]
            else:
                continue
    
    return False
        