import sys
from pickletools import byt

from anass.pythonProject3.bin2 import bytes2


def print_syntax():
      print('Syntax:')
      print(f'{sys.argv[0]} <file1> <file2>')
      sys.exit(1)

    def compare_files(file1, file2):
     with open(file1, 'rb') as myfile1, open(file2, 'rb') as myfile2:
       bytes1 = myfile1.read()
       bytes2 = myfile2.read()
    if len(sys.argv) != 3:
       print_syntax()
           
    if bytes1 != bytes2 :
        print('The files are different')
    else:
          print(" The files are iqual ")

try:
    compare_files(file1, file2)
except FileNotFoundError:
    print('One or both files not found.')
    print_syntax()
except Exception as e:
    print(f'An error occurred: {e}')
    sys.exit(1)
