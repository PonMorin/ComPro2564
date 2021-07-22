#10
n = int(input('Enter: '))
for row in range(n):
  for space in range(n - row - 1):
    print(end=' ')
  for column in range(2*row + 1):
    print('*', end='')
  print()

for row2 in range(n-1, 0, -1):
  for space in range(n - row2):
    print(end=' ')
  for column in range(2*row2 - 1):
    print('*', end='')
  print()
