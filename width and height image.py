from PIL import Image



img = Image.open('tree.jpg')

width,height = img.size

print(f'{width}x{height} pixels')