import math

def computeGeometricSeries(a0, q, epsilon = 0.01):
    if math.fabs(q) >= 1:
        raise ValueError("q must be less then one for series to converge")
    
    previosResult = 0
    result = a0
    previosTerm = a0
    termsAdded = 1

    while True:
        currentTerm = previosTerm * q
        result = result + currentTerm
        previosTerm = currentTerm
        termsAdded += 1
        
        if math.fabs(result - previosResult) <= epsilon:
            break
        else:
            previosResult = result

    return result, termsAdded

# 1 + 1/2 + 1/4 + 1/8 + 1/16 + ... => 2
print(computeGeometricSeries(1,0.5))
print("_-_-_-_-_-_-_")

# 1 + 3/10 + 9/100 + 27/1000 + ... => ~1.43
print(computeGeometricSeries(1,0.3, 0.00000001))
print("_-_-_-_-_-_-_")


# 1 - 1/2 + 1/4 - 1/8 + 1/16 + ... => 2/3
resultAsTupple = computeGeometricSeries(1,-0.5, 0.0000000000000000001)
formattedResult = format(resultAsTupple[0],  '.60g')
print(formattedResult, " ", resultAsTupple[1])