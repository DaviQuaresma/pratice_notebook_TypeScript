def mdc(a: int, b: int) -> int:
    
    r = a % b
    q = a // b
    
    print("=======================")
    print("Mais uma iteração")
    print(f"{a} / {b} = {q} com resto {r}")
    print("=======================")
    
    if r == 0: 
        return b
    
    if r != 0:
        a = b
        b = r
    
    return mdc(a, b)