#4 รับค่าตัวเลข 5 ตัวและแสดงผลดังตัวอย่าง
num1 = float(input('Number1: '))
num2 = float(input('Number2: '))
num3 = float(input('Number3: '))
num4 = float(input('Number4: '))
num5 = float(input('Number5: '))

result_list = []
result_list2 = []

print('[{}, {}, {}, {}, {}]'.format(num1,num2,num3,num4,num5))

#or
result_list.append(num1)
result_list.append(num2)
result_list.append(num3)
result_list.append(num4)
result_list.append(num5)
print(result_list)
#or

result_list2.extend([num1,num2,num3,num4,num5])
print(result_list2)
