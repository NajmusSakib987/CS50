text = input('Input: ')
vowels = ['a','e','i','o','u']
empty = ''

for char in text:
    if char.lower() in vowels:
        continue
    empty += char

print(f'Output: {empty}')
