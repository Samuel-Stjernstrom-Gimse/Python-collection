import math
from builtins import print


# pyinstaller .\tv_kalkulator.py -F

def format_til_(ab, fs, x):
    return round(math.sqrt((ab / fs) * x), 2)


def tommer_til_cm(x):
    return round(x * 2.54, 2)


def calc_tommer():
    try:
        return int(input('Hvor stor TV i tommer: ')) ** 2
    except:
        print('Du må skrive inn et tall..\n')
        calc_tommer()


def calc_format():
    while True:
        kombinert_format = str(input('Hvilket format: '))

        if kombinert_format.__contains__(':'):
            kombinert_format = kombinert_format.split(':')
        else:
            print('Du må skrive formatet på "bredde:høyde" format, eks: 16:9\n')
            continue

        try:
            format_bredde = int(kombinert_format[0])
        except:
            print('Du må skrive inn et tall..\n')
            continue

        try:
            format_høyde = int(kombinert_format[1])
        except:
            print('Du må skrive inn et tall..\n')
            continue

        format_sum = format_høyde + format_bredde
        return format_bredde, format_høyde, format_sum


def main():
    høyde_bredde2 = calc_tommer()
    format_bredde, format_høyde, format_sum = calc_format()

    bredde = format_til_(høyde_bredde2, format_sum, format_bredde)
    høyde = format_til_(høyde_bredde2, format_sum, format_høyde)
    høyde_cm = tommer_til_cm(høyde)
    bredde_cm = tommer_til_cm(bredde)

    print(f'Bredde: {bredde}" \nHøyde:{høyde}"')
    print(f'Bredde: {bredde_cm}cm \nHøyde:{høyde_cm}cm')

    retry = str(input('Vil du prøve igjen? Skriv ja/nei:\n')).lower()
    if retry == 'ja':
        print('\n-------------------------------------------------')
        main()
    else:
        exit()


main()
