import os
import re
import webbrowser
from nltk.corpus import wordnet

uruchom = ["uruchom", "odpal", 'otwórz', "załaduj", "rozpocznij", "zacznij"]
zamknij = ["zamknij", "kill", "zakończ"]
wyszukaj = ["wyszukaj", "wygoogluj", "znajdź", "poszukaj"]

syn = wordnet.synsets('run')
run = set()
for i in syn:
    synonym = i.name().split(".")
    run.add(synonym[0])

syn = wordnet.synsets('close')
close = set()
for i in syn:
    synonym = i.name().split(".")
    close.add(synonym[0])

syn = wordnet.synsets('search')
search = set()
for i in syn:
    synonym = i.name().split(".")
    search.add(synonym[0])

print("Witaj!")

while True:
    user = input().split()

    #Urcuhom aplikacje lub dokument
    if user[0].lower() in uruchom or user[0].lower() in run:
        file = user[1]
        if "." in file:
            os.system(f'open /Users/aaa/Documents/{file}')
            print("Success")

        else:
            os.system(f"open /Applications/{file}.app")
            print("Success")

    #Zamknij aplikacje
    if user[0].lower() in zamknij or user[0].lower() in close:
        file = user[1]
        os.system(f"killall {file}")
        print(f"Success")

    #Wyszukaj strone internetowa
    if user[0].lower() in wyszukaj or user[0].lower() in search:
        file = user[1]

        if re.match(r'^http:\/\/', file) or re.match(r'^https:\/\/', file):
            print(file)
            webbrowser.open(f'{file}')
        else:
            webbrowser.open(f'http://{file}')
        print(f"Success")

    #zakoncz program
    elif user[0].lower() == "koniec":
        break
