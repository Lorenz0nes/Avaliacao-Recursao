#a)
def S(n):
    if n == 1:
        return 10
    else:
        return S(n - 1) + 10


#b)
def A(n):
    if n == 1:
        return 2
    else:
        return A(n - 1) - 1

#c)
def B(n):
    if n == 1:
        return 1
    else:
        return B(n - 1) + n ** 2


#d)
def P(n):
    if n == 1:
        return 1
    else:
        return n ** 2 * P(n - 1) + n - 1


#e)
def D(n):
    if n == 1:
        return 3
    elif n == 2:
        return 5
    else:
        return (n - 1) * D(n - 1) + (n - 2) * D(n - 2)


#f)
def W(n):
    if n == 1:
        return 2
    elif n == 2:
        return 5
    else:
        return W(n - 1) * W(n - 2)


#g)
def T(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        return T(n - 1) + 2 * T(n - 2) + 3 * T(n - 3)
