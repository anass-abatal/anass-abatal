#Write a program that takes one word and replaces it with another in a text file
import sys
if len(sys.argv) < 4 :
    print("Syntax :")
    print(sys.argv[0], "<filename> <word1> <word2>")
    sys.exit()

myfile1 = open(sys.argv[1], "r")
lines = []
for line in myfile1:
    line_copy = line.copy()
    line.replace(sys.argv[2], sys.argv[3])
    lines.append(line_copy)



myfile1.close()

myfile1 = open(sys.argv[1], "w")
myfile1 = writelines(lines)
myfile1.close()
