# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('--------------------- Latihan 1 ----------------------')
    print('\n 1. Penugasan')
    a = input('Nilai A = ')
    b = input('Nilai B = ')
    c = int(a) + int(b)
    print('Nilai A + B Adalah = ', c)

    print('\n 2. Logika')
    print('LOGIKA AND')
    print('True and True   :', True and True)
    print('True and False  :', True and False)
    print('False and True  :', False and True)
    print('dari False and False :', False and False)
    print('\n')
    print('LOGIKA OR')
    print('True or True   :', True or True)
    print('True or False  :', True or False)
    print('False or True  :', False or True)
    print('False or False :', False or False)
    print('\n')
    print('LOGIKA NOT')
    print('not True  :', not True)
    print('not False :', not False )

    print('\n 3. Bitwise')
    x = 10
    y = 12
    print('\n')

    print('x << 1 :', x << 1)
    print('x >> 1 :', x >> 1)
    print('x & y  :', x & y)
    print('x | y  :', x | y)
    print('x ^ y  :', x ^ y)
    print('~x     :', ~x)

    print('\n 4. Identitas')
    a = 5
    b = 5
    c = 6
    print('a IS b :', a is b)
    print('a IS NOT c :', a is not c)

    print('\n 5. Keanggotaan')

    foo = 'MFarhanul I.R'
    print('Detek Huruf Dari = :', foo)
    print('\'i\' in Huruf     :', 'a' in foo)
    print('\'k\' not in Huruf :', 'h' not in foo)
    print('\'d\' not in Huruf :', 'f' not in foo)
    print('\n')

    bar = ['a', 'b', 'c']
    print('Detek String Array Dari :', bar)
    print('\'a\' in Array     :', 'a' in bar)
    print('\'a\' not in Array :', 'a' not in bar)
    print('\'d\' not in Array :', 'd' not in bar)
    print('\n')

    baz = (12, 43, 102, 55)
    print('Detek Int Dari :', baz)
    print('102 in Int     :', 102 in baz)
    print('102 not in Int :', 102 not in baz)
    print('35 not in Int  :', 35 in baz)


