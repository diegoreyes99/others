# TODO: Implementa tus funciones a continuación:

def add_comma(a_string):
    """
    returns a copy of the string with every word separated by a comma
    example: add_comma("John Peter Jude") => "John, Peter, Jude"
    """
    return ", ".join(a_string.split())
    pass

def belongs_to(a_string, a_word):
    """
    returns True if a_string contains a_word
    example: belongs_to("hey jude", "jude") => True
    """
    return a_word.lower() in a_string.lower()
    pass

def count_repetition(a_string, a_substring):
    """
    returns how many times a_substring occurs in a_string
    example: count_repetition("000123000123", "0") => 6
    """
    return a_string.count(a_substring)
    pass

def is_a_question(a_string):
    """
    returns True if a_string ends with a "?"
    example: is_a_question("How are you?") => True
    """
    return a_string.endswith("?")
    pass

def remove_surrounding_whitespaces(a_string):
    """
    returns a copy of the string with leading and trailing whitespaces removed
    example: remove_surrounding_whitespaces("  hey yo  ") => "hey yo"
    """
    return a_string.strip()
    pass

def replace(initial_string, old_letter, new_letter):
    """
    returns a copy of the string with the new letter replacing the old one
    example: replace("casanova", "a", "o") => "cosonovo"
    """
    return initial_string.replace(old_letter, new_letter)
    pass

def full_description_concatenation(first_name, last_name, age):
    """
    returns a sentence with the first_name and the last_name capitalized and
     the age using concatenation
    example: full_description_concatenation("john", "doe", 33) => "John Doe is 33"
    """
    return first_name.capitalize() + " " + last_name.capitalize() + " is " + str(age)
    pass

def full_description_formatting(first_name, last_name, age):
    """
    returns a sentence with the first_name and the last_name capitalized and
     the age using string interpolation
    example: full_description_formatting("john", "doe", 33) => "John Doe is 33"
    """
    return f"{first_name.capitalize()} {last_name.capitalize()} is {age}"
    pass


# No modifiques el código a continuación:

print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testeando funciones con estructura correcta:")

if add_comma('John Peter Jude') == 'John, Peter, Jude':
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")

if belongs_to('hey jude', 'jude') == True:
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")

if count_repetition('000123000123', '0') == 6:
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")

if is_a_question('How are you?') == True:
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")

if remove_surrounding_whitespaces('   hey  yo   ') == 'hey  yo':
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")

if replace('casanova', 'a', 'o') == 'cosonovo':
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")

if full_description_concatenation('john', 'doe', 33) == 'John Doe is 33':
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")

if full_description_formatting('john', 'doe', 33) == 'John Doe is 33':
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
	os.system("echo '\e[31mIncorrecto\e[0m'")
