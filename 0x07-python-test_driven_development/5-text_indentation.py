#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    ch = [".", "?", ":"]
    new = ""

    for i in range(len(text)):
        new += text[i]
        if text[i] in ch:
            print(new.strip(), end="", sep="\n")
            print("\n")
            new = ""
    print(new.strip(), end="")
