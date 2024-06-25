"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Filip Hájek
email: filipp.hajek@gmail.com
discord: Filip filip936
"""

# Zadání
#2. Vyžádá si od uživatele přihlašovací jméno a heslo,
#3. zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
#4. pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
#5. pokud není registrovaný, upozorni jej a ukonči program.**

import sys
registered_users = [
{"user": "bob", "password": "123"},
{"user": "ann", "password": "pass123"},
{"user":"mike", "password": "password123"},
{"user": "liz", "password": "pass123"}
] 

user_name = input("Inser your user name: ")
user_password = input("Insert your password: ")
print("username:", user_name)
print("password:", user_password)
print("-" * 70)

TEXTS = ['''   
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

valid_user = False
for user_info in registered_users: 
    if user_info["user"] == user_name and user_info["password"] == user_password:
        valid_user = True
        print("Welcome to the app, ", user_name)
        print(f"We have {len(TEXTS)} texts to be analyzed")
        break
#oprava podmínky pro neplatného uživatele
if not valid_user:
    print("unregistered user, terminating the program...")
    sys.exit() 

print("-" * 70)

texts_len = len(TEXTS)
selected_number = input(f"Enter a number between 1 and {texts_len} to select:")

if not selected_number.isnumeric():  #prvně ověřuji zda je input číslo. Mám to zvlášť, protože mi to jinak nefungovalo správně
    print("You have not input a number")
    sys.exit()

selected_number = int(selected_number)
if selected_number in range(1, texts_len + 1):
    print(f"Enter a number between 1 and {texts_len} to select:", selected_number)
else:
    print("You selected a wrong number")
    sys.exit() 

print("-" * 70)
#opravení indexování
working_text = TEXTS[selected_number -1]
word_count = len(working_text.split())
word_first_upper = []
word_upper = []
word_lower = [] 
num_count = []
num_sum = []

#odstranění nežádoucích znaků
unwanted_characters = str.maketrans(" ", " ",".,;!?-")

for word in working_text.split():
    clean_word = word.translate(unwanted_characters) #očištění slov o nežádoucí znaky
    if clean_word and clean_word[0].isalpha() and clean_word[0].isupper():#kontrola zda první index je velké písmeno
        word_first_upper.append(1)
    if clean_word.isupper() and clean_word.isalpha():
        word_upper.append(1)
    if clean_word.islower():
        word_lower.append(1)
    if clean_word.isnumeric():
        num_count.append(1)
        num_sum.append(int(clean_word))

print("There are ",word_count," words in the selected text.")
print("There are ",sum(word_first_upper), " titlecase words.")
print("There are ", sum(word_upper), " uppercase words.")
print("There are ", sum(word_lower), " lowercase words.")
print("There are ", sum(num_count), " numeric strings.")
print("The sum of all the numbers ", sum(num_sum))
print("-" * 70)
print("LEN|    OCCURENCES     | NR.")
print("-" * 70)

word_len_count = {}

for word in working_text.split():
    clean_word = word.translate(unwanted_characters)
    word_len_count[len(clean_word)] = word_len_count.get(len(clean_word), 0) + 1
 
for length, count in sorted(word_len_count.items()):
    print(f"{length:>2} | {'*' * count:<17} | {count}")






