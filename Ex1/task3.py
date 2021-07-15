#3 รับค่าตัวเลขทศนิยม 4 หลัก และให้แสดงผลแค่ 2 หลัก

float_number = float(input('Enter 4 decimal: '))
print('Display: %.2f'%float_number)

#or
decimal1 = '{:.3g}'.format(float_number)
print('Display:',decimal1)

#or
decimal2 = round(float_number,2)
print('Display:',decimal2)
