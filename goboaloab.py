#                             legge til modify rett i input
name = input('hva heter du? ').strip().title()

#remove whitespace from str
name = name.strip()

#stor bokstav på starten av hvert ord
name = name.title()

#man kan ta mange etterhverandre
name = name.title().strip()

print('Hei ', name)

# end='' stopper den fra å gå til neste linje end='/n' er der automatisk denne får den til å gå til neste linje
print('Hei ', end='')
print(name)

# sep='XXX' hva som fyller plassen til mellomrom
print('hei', name, sep='???')

#f = format string {} inni ''
print(f'hello, {name}')



