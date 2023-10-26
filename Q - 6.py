def pertence_a_W(string):
    if len(string) == 1 and string in "abc":
        return True
    if len(string) < 3:
        return False

    if string[0] == "a" and string[-1] == "c":
        if pertence_a_W(string[1:-1]):
            return True

    return False

cadeias = ["a(b)c", "a(a(b)c)c", "a(abc)c", "a(a(a(a)c)c)c", "a(aacc)c"]
for cadeia in cadeias:
    if pertence_a_W(cadeia):
        print(f"'{cadeia}' pertence a W")
    else:
        print(f"'{cadeia}' NÃO pertence a W")
