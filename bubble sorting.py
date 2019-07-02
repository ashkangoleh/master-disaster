numbs = [4, 7, 1, 6, 5, 10, 50, 60, 70, 32, 0, 42, 35, -20, -1]



do = 0


while not do:
    do = 1
    for n in range(1, len(numbs)):
        #left to right
        if numbs[n-1] > numbs[n]:
            numbs[n-1], numbs[n] = \
                numbs[n], numbs[n-1]
            do = 0
print(numbs)
