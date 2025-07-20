
#compute nth term of fibonacci sequence
#F(n) = F(n-1) + F(n-2)

def computeFibonacciSequence(n):
    if n <= 0:
        raise ValueError("invalid argument")

    fn_1 = 0
    fn_2 = 1
    
    if n ==1:
        return fn_1
    
    if n == 2:
        return fn_2
    
    fn = 0
    i = 2
    while i <= n:
        fn = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = fn

        i += 1

    return fn


####################################################################

def computeFibonacciSequenceRecursion(n):
    if n <= 0:
        raise ValueError("invalid argument")

    if n ==1:
        return 0 # fn_1
    
    if n == 2:
        return 1 # fn_2
    
    return computeFibonacciSequenceRecursion(n-1) + computeFibonacciSequenceRecursion(n-2)

####################################################################

for i in range(1,16):
    print(computeFibonacciSequence(i), end = " ")

print()
for i in range(1,16):
    print(computeFibonacciSequenceRecursion(i), end = " ")

print()