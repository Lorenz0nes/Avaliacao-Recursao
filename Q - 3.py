def pertence_a_T(n):
    if n == 2:
        return True
    if n < 2:
        return False

    if pertence_a_T(n - 3):
        return True

    if n % 2 == 0 and pertence_a_T(n // 2):
        return True

    return False

numeros = [6, 7, 19, 12]
for numero in numeros:
    if pertence_a_T(numero):
        print(f"{numero} pertence a T")
    else:
        print(f"{numero} NÃO pertence a T")
