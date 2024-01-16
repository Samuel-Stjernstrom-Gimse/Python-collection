antall_sekunder = int(input('hvor mange sekunder? '))


timer = int(antall_sekunder / 3600)
minutter = int((antall_sekunder - (timer * 3600)) / 60)
sekunder = int(antall_sekunder - (timer * 3600)-(minutter * 60))

if timer >= 1:
    print(f' {timer}:timer  ', end='')
if minutter >= 1:
    print(f'{minutter}:minutter  ', end='')
if sekunder >= 1:
    print(f'{sekunder}:sekunder  ')

