def recursive(n):
    if len(n) > 1:
        return n[0] + recursive(n[1:])
        #             ^^^^^^^^^
        #             recursive act

    else:
        return n[0]

print(recursive([1,2,3,4,5,6,7,8,9]))