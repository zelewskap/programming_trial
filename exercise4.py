# checking which character is a wrod in KRZ
zdanie = input("Wpisz zdanie logiczne w KRZ: ")
wyrazy = ""
for character in zdanie:
    if character.isalpha() and character != "v":
        wyrazy += character
print("Wyrazami w tym zdaniu są: ", wyrazy)
