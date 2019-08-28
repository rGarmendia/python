def string_length(word):
    if type(word) == int:
        return "It's integer"
    elif type(word) == float:
        return "It's float"
    else:
        return len(word)

word = input("put this shit in here: ")
print(string_length(word))