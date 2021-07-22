#11
num = int(input(''))
for row in range(num):
    for column in range(row + 1):
        if column == 0 or column == row:
            print('*',end='')
        else:
            print(end=' ')
    print()
