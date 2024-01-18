import sys

  def print_syntax():
    print('Syntax:')
    print(f'{sys.argv[0]} <binaryfile1> <binaryfile2>')
    sys.exit(1)

   def compare_binary_files(file1, file2):with open(file1, 'rb') as myfile1, open(file2, 'rb') as myfile2:        bytes1 = myfile1.read()
        bytes2 = myfile2.read()        if bytes1 != bytes2:
            print('The binary files are different')
        else:
            print('The binary files are equal')

if len(sys.argv) != 3:
    print_syntax()

file1, file2 = sys.argv[1], sys.argv[2]

try:
    compare_binary_files(file1, file2)
except FileNotFoundError:
    print('One or both files not found.')
    print_syntax()
except Exception as e:
    print(f'An error occurred: {e}')
    sys.exit(1)

