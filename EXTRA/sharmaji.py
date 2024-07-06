name = input('enter name')
while not name.isalpha():
    print('invalid name.')
    name = input('enter name')
    print(name)