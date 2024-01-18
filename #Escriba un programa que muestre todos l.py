#Escriba un programa que muestre todos los números pares entre dos números que un usuario proporciona como entrada
numero_1=int(input("enter the first number:"))
numero_2=int(input("enter the segund number:"))
if(numero_1>numero_2):
 i=numero_2
 while  i<numero_1 :
        print(i)
 i += 1
