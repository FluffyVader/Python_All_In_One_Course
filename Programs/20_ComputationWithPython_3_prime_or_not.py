import time

def isPrime(number):
    if number < 2:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        print('%d has factor %d' %(number, 2))
        return False

    trialUpperbound = number // 2        #sets the limit
    trialFactor = 3

    while trialFactor <= trialUpperbound:
        if number % trialFactor == 0:
            print('%d has factor %d' %(number, trialFactor)) #
            return False
        
        trialFactor += 2
    else:
        return True
    
assert isPrime(2)
assert isPrime(3)
assert not isPrime(4)
assert isPrime(5)
assert not isPrime(8)
assert not isPrime(9)

startTime = time.time()
#print('is 999998081 prime? %s'  % isPrime(999998081)) #999998081
print('is 39916801 prime? %s'  % isPrime(39916801)) #100003679
endTime = time.time()
timeUsedSeconds = endTime - startTime
print(f"the time used to calculate the number is: {timeUsedSeconds} seconds")