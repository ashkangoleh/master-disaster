import tempfile


def read(f):
    f.seek(0)
    data = f.read()
    print(data)


f = tempfile.TemporaryFile()
f.write(b'some temp data')


read(f)

f.close()