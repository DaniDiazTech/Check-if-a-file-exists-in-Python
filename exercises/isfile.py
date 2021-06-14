import os

print(os.path.isfile('testfile.txt'))

print(os.path.isfile('testdirectory'))

print(os.path.isfile('i-dont-even-exist'))

print(os.path.isfile('testdirectory/otherfile.txt'))