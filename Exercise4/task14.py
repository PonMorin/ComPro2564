str1 = input('Enter: ')
special_character = [' ', '#', '@', '!', '%', '$', ',', ':', ';']
count_upper = 0
count_lower = 0
count_special = 0

for i in range(len(str1)):
    if str1[i].isupper():
        count_upper += 1
    elif str1[i].islower():
        count_lower += 1
    elif str1[i] in special_character:
        count_special += 1
print('Uppercase character number is',count_upper)
print('Lowercase character number is',count_lower)
print('Special character number is',count_special)
