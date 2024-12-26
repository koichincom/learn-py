def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aiueo":
            translation += "g"
        elif letter in "AIUEO":
            translation += "G"
        else:
            translation += letter
    return translation

print(f"Translated phrase:  {translate(input("Type a phrase: "))}")