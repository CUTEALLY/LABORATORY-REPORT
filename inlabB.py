
def product(m, n):
    if m < n:
        return product(m, n)

    elif n != 0:
        return (m + product(m, n - 1))

    else:
        return 0

m = 11
n = 5
print(product(m, n))

