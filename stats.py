def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(book):
    with open(book) as file:
        text = file.read()
    return text

def character_count(text):
    dict = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0, " ":0, "\n":0, ".":0, ",":0, ";":0, ":":0, "!":0, "?":0, "'":0, '"':0}
    text = text.lower()
    for char in text:
        if char in dict:
            dict[char] += 1
    return dict

def list_dictionary(dict):
    liste = []
    for key, value in dict.items():
        if key.isalpha():
            x = {"char": key, "num": value}
            if x["num"] > 0:
                liste.append(x)
    return liste

def sort_on(dict):
    return dict["num"]

def liste_sorted(liste):
    liste.sort(reverse=True, key=sort_on)
    return liste