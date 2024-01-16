def lese_fil(antall_filer, antall_linjer):
    try:
        for fil_nummer in range(0, antall_filer):
            with open(f'filer/kegel_{fil_nummer}.txt', 'r', encoding='utf-8') as file:
                print(file.read())
    except FileNotFoundError:
        for fil_nummer in range(0, antall_filer):
            print(f'Creating kegel file: {fil_nummer}')
            with open(f'filer/kegel_{fil_nummer}.txt', 'w', encoding='utf-8') as file:
                for teller in range(0, antall_linjer):
                    file.write(f'{teller}: haaaayyyyy dette er Tim Tim!!\n')
        lese_fil()


lese_fil(antall_filer=10, antall_linjer=5)


def tiss_1():
    try:
        b = int(input('skriv ett tall'))
    except:
        print('Du må talle, ikke stringe')
        tiss_1()

    print(b)


def tiss_2():
    ikkeFerdig = True
    while ikkeFerdig:
        try:
            b = int(input('skriv ett tall'))
            ikkeFerdig = False
        except:
            print('Du må talle, ikke stringe')
    print(b)
