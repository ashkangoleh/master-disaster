import random




n = 10
numbs = 10000
max = 1000

histogram = [0] * n


for item in range(numbs):
    ran = random.randint(0,max - 1)
    bin = ran / (max / n)
    histogram[int(bin)] += 1

print(histogram)