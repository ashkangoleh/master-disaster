numbs = [4, 7, 1, 6, 5, 10, 50, 60, 70, 32, 0, 42, 35,-20, -1]


def quicksort(numbs):
    if len(numbs) <= 1:
        return numbs



    pi = numbs[0]
    lt = []
    rl = []

    for i in numbs[1:]:
        if i <pi:
            lt.append(i)
        else:
            rl.append(i)


    return quicksort(lt) + \
         [pi] + quicksort(rl)


d = quicksort(numbs)

print(d)