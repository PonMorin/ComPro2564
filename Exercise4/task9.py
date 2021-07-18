n = int(input('Enter: '))
for row in range(n):
  for space in range(n - row -1):
    print(end=' ')
  for column in range(2*row + 1):
    print('*', end='')
  print()
