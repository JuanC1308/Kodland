import random
chars="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud=int(input("Ingrese la longitud de la contraseña "))
contra=""
for i in range(longitud):
    indice=random.randint(0,len(chars)-1)
    A=chars[indice]
    contra=contra+A

print(contra)
