def pascal(rowIndex):
    coef = [1]

    for index in range(1, rowIndex + 1):
        next_coef = coef[-1] * (rowIndex - index + 1) // index
        coef.append(next_coef)
    return coef

print(pascal(4))
