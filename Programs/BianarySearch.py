def bianarySearch(a, key):
    if len(a) == 0:
        return -1
    
    leftIdx = 0
    rightIdx = len(a) - 1

    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2

        if key == a[midIdx]:
            return midIdx
        
        if key < a[midIdx]:
            rightIdx = midIdx - 1
        else:
            leftIdx = midIdx + 1

    else:
        return - 1
# index positions
#       0   1   2    3   4    5    6    7
keys = [3 , 5 , 8 , 10 , 12 , 13 , 15 , 19]

keyIdx = bianarySearch(keys, 3)
assert keyIdx == 0

keyIdx = bianarySearch(keys, 8)
assert keyIdx == 2

keyIdx = bianarySearch(keys, 15)
assert keyIdx == 6

keyIdx = bianarySearch(keys, 19)
assert keyIdx == 7

################
#error testing if it is in list or not

keyIdx = bianarySearch(keys, 9)
assert keyIdx == -1

keyIdx = bianarySearch(keys, 20)
assert keyIdx == -1


#if any errors occur in the program an error whould have been displayed in terminal/console