import io
try:
    file = io.open('.\\text.txt.hhshfjhjf.bg')
    print('File found')
except FileNotFoundError:
    print('File not found')

