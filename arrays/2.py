import numpy as np

b = np.array([1,5,-2,10])

# iterative approach
def array_sum(numberArr):
    arrSum = 0
    for i in numberArr:
        arrSum = arrSum + i
    return arrSum

print(array_sum(b))

def array_sum_recursive(numberArr):
    if len(numberArr) == 1:
        return numberArr[0]
    
    # Recursive case
    return numberArr[0] + array_sum(numberArr[1:])

print(array_sum_recursive(b))


print(b.sum())