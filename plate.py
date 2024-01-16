
def main():
    plate = input('plate number? ')
    if is_valid(plate):
        print(f' {plate} Is Valid')
    else:
        print(f' {plate} Is Invalid')



def is_valid(plate):
    numbers = '1234567890'
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    komilist = [bare_tall_og_bokstaver(numbers, letters, plate),
            ikke_starte_med_null(plate, numbers),
            max_numers(plate),
            last_is_digit(plate, numbers, letters),
            ]
    if all(komilist):
        return True
    else:
        return False

def bare_tall_og_bokstaver(number, letters, plate):
    for x in plate:
        if x not in number + letters:
            return False
        else:
            return True

def ikke_starte_med_null(plate, numbers,):
    tall_i_plate = ''
    for x in plate:
        if x not in numbers:
            continue
        tall_i_plate += x
    if tall_i_plate[0:1] == '0':
        return False
    else:
        return True

def max_numers(plate):
    i = len(plate)
    if i < 4 or i >= 7:
        return False
    return True

def last_is_digit(plate, numbers, letters):
    for x in plate:
        if x in numbers and plate[-1] == letters:
            return False
        else:
            return True


main()
main()
main()

