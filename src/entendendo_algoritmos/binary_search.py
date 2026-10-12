def binarySearch(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        half = (low + high) // 2
        shoot = list[half]
        print("half: ", half)
        print("trying: ", shoot)

        if shoot == item:
            print("Found the number: ", half)
            return half

        if shoot > item:
            high = half - 1
            print("Much high, reducing list lenght, new high: ", high)
        else:
            print("Much low, increasing  list lenght, new low: ", low)
            low = half + 1

    return None
