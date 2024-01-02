variable = input('camelCase: ')
variable = variable.strip()
snake = ''

for char in variable:
    if char.isupper():
        snake += "_"
        char = char.lower()
    snake += char

print(f'snake_case: {snake}')
