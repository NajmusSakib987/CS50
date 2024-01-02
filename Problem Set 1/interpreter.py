exp = input('Expression: ')
index_of_first_space = exp.find(' ')
sign = exp[index_of_first_space + 1]
index_of_sign = exp.find(sign)

first_number = float(exp[0:index_of_first_space])
second_number = float(exp[index_of_sign + 2:])

if ' + ' in exp:
    result = first_number + second_number
    print(round(result, 1))

elif ' - ' in exp:
    result = first_number - second_number
    print(round(result, 1))

elif ' / ' in exp:
    result = (first_number) / (second_number)
    print(round(result, 1))
elif ' * ' in exp:
    result = first_number * second_number
    print(round(result,1))
else:
    pass






