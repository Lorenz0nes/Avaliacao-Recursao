#a)
def sequencia_a(n):
    if n == 1:
        return 1
    else:
        return 3 * sequencia_a(n - 1)

#b)
def sequencia_b(n):
    if n == 1:
        return 2
    else:
        return sequencia_b(n - 1) / 2

#c)
def sequencia_c(a, b, n):
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        return sequencia_c(a, b, n - 2) + sequencia_c(a, b, n - 1)

#d)
def sequencia_d(p, q, n):
    if n == 1:
        return p
    elif n % 2 == 0:
        return sequencia_d(p, q, n - 1) + 2 * q
    else:
        return sequencia_d(p, q, n - 1) - q
