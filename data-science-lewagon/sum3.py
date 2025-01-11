# Implementa tu código aquí debajo

def sum3(number_1, number_2, number_3):
    return number_1 + number_2 + number_3


# No modifiques el código a continuación:

print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testeando sum3 con 0 0 0:")
if sum3(0, 0, 0) == 0:
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")
print("Testeando sum3 con 1 2 3:")
if sum3(1, 2, 3) == 6:
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")
print("Testeando sum3 con 4 5 6:")
if sum3(4, 5, 6) == 15:
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")
print("Testeando sum3 con -1 1 0:")
if sum3(-1, 1, 0) == 0:
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")
