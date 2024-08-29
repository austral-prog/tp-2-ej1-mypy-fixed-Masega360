def max_of_two(x: int, y: int) -> int:
    biggest = x
    if x >= y:
        return biggest
    else:
        biggest = y
        return biggest


# Replace the "ANSWER HERE" for your answer
def max_of_three(x: int, y: int, z: int) -> int:
    biggest = -9999999
    list = [x, y, z]
    for i in list:
        if i > biggest:
            biggest = i
    return biggest
