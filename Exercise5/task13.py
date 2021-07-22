#13
username = 'abc'
password_user = '12dc' 
while True:
  user = input('Enter username: ')
  password = input('Enter password: ')
  if user != username or password != password_user:
    print('Your password is wrong')
    username = 'admin'
    password_user = '1234'
  elif user == username and password == password_user:
      new_user = input('Enter your new username: ')
      new_password = input('Enter your new password: ')
      print('Your new username: ',new_user)
      print('Your new password: ',new_password)
      break
