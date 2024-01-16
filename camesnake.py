camelcase = input('firstName ')


def making_snake(c):
    snakecase = ''
    for x in c:
        if x.isupper():
            x = x.lower()
            x = '_' + x
        snakecase += x
    print(snakecase)

making_snake(camelcase)










