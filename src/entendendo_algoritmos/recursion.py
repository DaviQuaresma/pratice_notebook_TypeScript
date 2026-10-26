def fat(num: int) -> int:
    if num == 1:
        return 1
    else:
        return num * fat(num - 1)
