num = int(input('Enter: '))
for row in range(num-1, -1, -1):
    for column in range(row + 1):
        if column == 0 or column == row:
            print('*', end='')
        else:
            print(end=' ')
    print()
