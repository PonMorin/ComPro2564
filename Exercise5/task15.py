#15
list1 = []
cancel = True
while cancel == True:
    str1 = input('Enter your word item: ')
    if str1 == 'pop':
        if not list1:
            print('No item inside')
        elif list1:
            list1.pop(-1)
            for i in range(len(list1)):
                print(list1[i], end=' ')
    elif str1 == 'cancel':
        cancel = False
    else:
        list1.append(str1)
        for i in range(len(list1)):
            print(list1[i], end=' ')
