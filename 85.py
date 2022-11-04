def c_rect_grid(x, y):
    rect = ((x ** 2 + x) * (y ** 2 + y)) // 4
    return rect

def eval (n):

    max = 2000000
    ind = 0

    X = []
    Y = []

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            X.append(c_rect_grid(x, y))
            Y.append(x * y)

    for k in range (0, len(X)):
        diff = abs(X[k] - 2000000)
        if diff < max:
            max = diff
            ind = k

    return Y[ind]

print(eval(200))
