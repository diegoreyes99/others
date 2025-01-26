# TODO: primero agregar una estructura de datos con el tipo de cambio (currency rates)


# TODO: Implementa tu método convert a continuación:
def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    #Agregar diccionarios para convertir algunas monedas a euros (USDEUR, CHFEUR, GBPEUR, EURGBP )
    #rates = {'USDEUR': 0.85, 'CHFEUR': 0.86, 'GBPEUR': 1.13}
    #Identificar moneda a convertir y dividirla en dos
    #Llamar la moneda a convertir en el diccionario creado en el primer paso
    #Agregar operacion de conversion para cada cambio de moneda y sustituirla por la ingresada
    #Regresar resultado return
    rates = {'USDEUR': 0.85, 'CHFEUR': 0.86, 'GBPEUR': 1.13}
    transform = amount[1] + currency

    if transform == 'USDEUR':
        return amount[0] * rates["USDEUR"]
    elif transform == 'CHFEUR':
        return amount[0] * rates["CHFEUR"]
    elif transform == 'GBPEUR':
        return round(amount[0] * rates["GBPEUR"])
    elif transform == 'EURGBP':
        return amount[0] / rates["GBPEUR"]
    else:
        return None

print(convert((300, "GBP"), "EUR"))


# No modifiques el código a continuación:

print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testeando funcion con estructura correcta:")

amount = (100, "USD")
if convert(amount, "EUR") == 85:
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")

amount = (200, "CHF")
if convert(amount, "EUR") == 172:
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")

amount = (300, "GBP")
if convert(amount, "EUR") == 339:
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")

amount = (339, "EUR")
if convert(amount, "GBP") == 300:
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")

amount = (300, "RMB")
if convert(amount, "EUR") == None:
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")
