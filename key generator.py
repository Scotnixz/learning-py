import random
import string
import os

def key_generator(size: int) -> str:
    chars= string.ascii_letters + string.digits
    senha = ''.join(random.choices(chars, k=size))

    return senha

key_size = int(input("Qual a quantidade de caracteres que sua senha terá? \n"))

while key_size < 6:
    print("Sua senha será muito curta, digite um número maior que 5!")
    key_size = int(input("Digite seu número aqui\n"))

site_name = input("Digite o nome do site em que a senha será usada \n")

Key = key_generator(key_size)

archive_txt = "senhas.txt"

if not os.path.exists(archive_txt):
    open(archive_txt, "w")

with open(archive_txt, "a") as archive:
    archive.write(f"{site_name}: {Key} \n")

print("Sua senha foi criada com sucesso!")