try:
    file_ = open('nonexistingfile.txt')
except FileNotFoundError:
    print('Sorry that file does not exist')

try:
    file_ = open('testfile.txt')
    print(file_)
except FileNotFoundError:
    print('Sorry that file does not exist')