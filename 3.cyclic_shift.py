def cyclic_shift(element):
    last = element[0]
    for i in range(len(element) - 1):
        element[i] = element[i + 1]
    element[-1] = last
    return element
