import os

dir_name = input('Enter the Directory name: ')
if os.path.exists('D:\\'+dir_name):
    print('Directory <{}> already exists!'.format(dir_name))
else:
    os.makedirs('D:\\'+dir_name)
    print('Directory {} created successfully!!'.format(dir_name))
