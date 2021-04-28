# counting vowels in the words
wyraz = input("Podaj dowolny wyraz ")
samogloski = ["a", "ą", "e", "ę", "i", "o", "ó", "u", "y"]
liczba_samoglosek = 0
for litera in wyraz:
    if litera in samogloski:
        liczba_samoglosek += 1

print("Liczba samogłosek w podanym wyrazie wynosi: ", liczba_samoglosek)

# saving phone number and checking if it is correct
telefon = input("Podaj numer telefonu: ")
if telefon.isdigit(): # checkicng if all characters are numbers
    print("Twój numer telefonu", telefon, "został zapisany, dzięki!") # saved!
else:
    poprawny_nr = ""
    for znak in telefon:
        if znak.isdigit(): 
            poprawny_nr += znak # writing down only numbers
    if poprawny_nr == "":
        print("Twój numer telefonu nie zawiera liczb :(")
    else:
        print("Twój numer telefonu", poprawny_nr, "został zapisany, dzięki!")

# returning the number of letters in a sentence
zdanie = input("Wpisz dowolne zdanie: ")
liczba_liter = 0
for slowo in zdanie:
    for litera in slowo:
        if litera.isalpha():
            liczba_liter += 1
print("Liczba liter wynosi ", liczba_liter)

