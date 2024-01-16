def main():
    x = int(input(' what is x?'))
    if odd_or_even(x):
        print('Even')
    else:
        print('Odd')
def odd_or_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
