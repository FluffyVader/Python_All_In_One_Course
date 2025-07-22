import statisticsHelper

a = [3, 1, 4, 1, 5, 6, 2, 6]        #sorted: [1, 1, 2, 3, 4, 5, 6, 9]

print(statisticsHelper.findMedian(a))
print(a)

a.append(5)
print(statisticsHelper.findMedian(a))
print(a)