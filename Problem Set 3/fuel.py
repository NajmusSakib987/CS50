while True:
    fuel = input('Fraction: ')
    try:
        v1, v2 = fuel.split('/')
        if int(v1) > int(v2) or "." in v1 or "." in v2:
            raise ValueError
        v1 = int(v1)
        v2 = int(v2)
        percentage = v1/v2
        break
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
percentage = round(v1/v2, 2) * 100

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f'{int(percentage)}%')


