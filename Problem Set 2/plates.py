def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(plate):
    if is_condition_1(plate) and is_condition_2(plate):
        if is_condition_3(plate):
            if is_condition_4(plate):
                return True
    else:
        return False
def is_condition_1(plate):
    if plate[:2].isalpha():
        return True
    else:
        return False
def is_condition_2(plate):
    if 2 <= len(plate) <= 6:
        return True
    else:
        return False
def is_condition_3(plate):
    if number_contain(plate):
        pass
    else:
        return True

    name = []
    for char in plate:
        if char.isdigit():
            name = plate.split(char, 1)
            break
    if (('0' in plate) and ('0' in name[-1])) or (not '0' in plate):
        for num in name[-1]:
            if num.isalpha():
                return False
        return True
    else:
        return False



def is_condition_4(plate):
    for char in plate:
        if not (char.isdigit() or char.isalpha()):
            return False
            break
    return True


def number_contain(plate):
    return any(number.isdigit() for number in plate)


main()
