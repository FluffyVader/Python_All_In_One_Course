def findMedian(a):
    print("running from stats helper")
    #making a copy before sorting
    aClone = a[:]
    aClone.sort()

    num = len(aClone)

    if num % 2 == 0:
        MedianN = (aClone[num // 2] + aClone[num // 2 - 1]) * 0.5

    else:
        MedianN = aClone[num // 2]

    return MedianN
