word = input()

if word == word.upper():
    print(True)

elif word == word.lower():
    print(True)

elif word[0].isupper() and word[1:] == word[1:].lower():
    print(True)

else:
    print(False)