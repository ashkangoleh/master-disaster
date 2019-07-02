c = 0


try:
    while 1:
        c += 1
except KeyboardInterrupt:
    print(f'The counter is {c} now')