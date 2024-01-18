import sys

if len(sys.argv) < 3:
    print('Syntax:')
    print(sys.argv[0], '<textfile1> <textfile2>')
    sys.exit()

myfile1 = open(sys.argv[1])
myfile2 = open(sys.argv[2])
lines10 = myfile1.readlines()
lines2 = myfile2.readlines()

if len(lines10) != len(lines2):
    print('The files are different')
else:
    i = 0
    for myline1 in lines10:
        myline2 = lines2[i]
        if myline1 != myline2:
            print('The files are different')
            break
        i += 1
    print('The files are equal')
myfile1.close()
myfile2.close()
