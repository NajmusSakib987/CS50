d = {

}

while True:
    try:
        grocery = input()
        if grocery in d.keys():
            d[grocery] += 1
            continue
        d.update({grocery: 1})
    except EOFError:
        for key in sorted(d.keys()):
            print(f'{d[key]} {key.upper()}')
        break


