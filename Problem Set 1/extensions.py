name = input("File Name: ")
name = name.lower().strip()

if name.endswith('gif') or name.endswith('png'):
    extension = name[-3:]
    print(f'image/{extension}')
elif name.endswith('jpeg') or name.endswith('jpg'):
    print('image/jpeg')
elif name.endswith('pdf') or name.endswith('zip'):
    extension = name[-3:]
    print(f'application/{extension}')
elif name.endswith('txt'):
    print('text/plain')
else:
    print('application/octet-stream')

