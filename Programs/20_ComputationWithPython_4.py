import random                                           # imports random

samples = []                                            # an empty list is made

for idx in range(0, 15):                                # makes 15 float numbers
    samples.append(round(random.gauss(85, 5)))          # add the 15 float numbers to the samples list
sampleMean = sum(samples) / len(samples)                # make a var that contains the sum of samples divided by the number of samples
print(sampleMean)                                       # prints the sampleMean var
                                                        # the lines 5-8 get the arithmetic mean of the number

sampleVariance = 0                                      # makes a var that contains 0

for sample in samples:                                  # goes through all the float numbers in the samples list
    sampleVariance += (sample - sampleMean) ** 2        # adds sample - sample mean by exponentiation in sampleVariance and saves it             
sampleVariance = sampleVariance / (len(samples) - 1)    # sampleVariance is now the past value of sampleVariance but the lenth of samples list - 1
print(sampleVariance ** 0.5)                            # then print sampleVariance exponentianoned by 0.5