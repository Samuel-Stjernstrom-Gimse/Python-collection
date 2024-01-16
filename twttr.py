tekst = input('write her? ')
vowels = 'AaEeIiOoUu'
utskrift = ''

for x in tekst:
    if x in vowels:
        continue
    utskrift += x

print(utskrift)
