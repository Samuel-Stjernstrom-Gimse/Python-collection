

def main():
    rekkevidde_km = int(input(' Rekkevidden til din elbil i kilometer: '))
    tur_lengde_km = int(input(' Lengden til kjøreturen i kilometer: '))
    minimum = int(input('Hvor mange prosent er det laveste du vil lade til? ')) * 0.01
    maximum = int(input('hvor mange prosent er det høyeste du vil lade til? ')) * 0.01

    if prosent_av_max(rekkevidde_km, tur_lengde_km,minimum):
        print(f'Du må lade {antall_ladinger(tur_lengde_km, rekkevidde_km, minimum, maximum)} ganger.')
    else:
        print('du trenger ikke å lade :)')

    vil_du_prøve_igjen = str(input('Vil du prøve igjen? skriv ja')).lower()
    if vil_du_prøve_igjen == 'ja':
        main()

def prosent_av_max(r,l,min):
    if l < (1 - min) * r:
        return False
    else:
        return True

def antall_ladinger(l,r,min,max):
    a = l - r * (1 - min)
    return a // (r * (max - min)) + 1


main()


