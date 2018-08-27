def translate(phrase): #define translate function; "()"phase we want to translate
    translation = "" # final result returned to user
    for letter in phrase: #loops thru every letter of "phrase" that is passed in
        if letter.lower() in "aeiou": # checks to see if vowel and adds whatever to translation anyway
            if letter.isupper():
                tranlastion = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a Phrase: ")))

    