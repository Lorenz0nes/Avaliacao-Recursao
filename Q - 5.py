def pertence_a_S(string):
    if string == "a" or string == "b":
        return True
    if len(string) < 2:
        return False

    if pertence_a_S(string[:-1]) and string[-1] == "b":
        return True

    return False

cadeias = ["a", "ab", "aba", "aaab", "bbbbb"]
for cadeia in cadeias:
    if pertence_a_S(cadeia):
        print(f"'{cadeia}' pertence a S")
    else:
        print(f"'{cadeia}' NÃO pertence a S")
