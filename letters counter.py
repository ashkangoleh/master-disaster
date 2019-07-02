msg = 'hello, my dear friends!'


stats = {
    letter:msg.count(letter)
        for letter in msg
}

for item in sorted(
    stats, key = stats.get,reverse = True):
    print(f'{item} = {stats[item]}')
